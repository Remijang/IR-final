import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

from utils import load_all_documents, load_all_embeddings, get_almost_top15


app = Flask(__name__)

# Global variable to hold the model
model = None
doc_embeddings = None
doc_metadata = None
MODEL_NAME = "Snowflake/snowflake-arctic-embed-l-v2.0"
# EMBEDDINGS_PATH = "embeddings_cache/calculus_full/doc_embeddings.npy"
# METADATA_PATH = "embeddings_cache/calculus_full/doc_metadata.json"
BOOK_NAME_MAP = {
    "calculus_full": "Calculus",
    "Chemistry2e": "Chemistry",
    "Biology2e": "Biology",
    "College_Physics_2e": "Physics",
    "os": "Operating Systems",
    "ca": "Computer Architecture",
}


def load_model_and_embeddings():
    global model, doc_embeddings, doc_metadata

    try:
        print("Loading SentenceTransformer model...")
        model = SentenceTransformer(MODEL_NAME)
        print("Model loaded successfully.")

        print("Loading pre-computed embeddings and metadata...")
        # doc_embeddings, doc_metadata = load_embeddings_and_metadata(EMBEDDINGS_PATH, METADATA_PATH)
        doc_embeddings, doc_metadata = load_all_embeddings()
        print("Embeddings and metadata loaded successfully.")

        if doc_embeddings is None or doc_metadata is None:
            print("Failed to load embeddings or metadata.")
            return None

        return model, doc_embeddings, doc_metadata
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def load_embeddings_and_metadata(embeddings_path, metadata_path):
    print("Loading pre-computed embeddings and metadata...")
    if not os.path.exists(embeddings_path) or not os.path.exists(metadata_path):
        print(
            f"Embedding or metadata file not found ({embeddings_path} or {metadata_path})."
        )
        return None, None

    try:
        doc_embeddings = np.load(embeddings_path)
        with open(metadata_path, "r") as f:
            doc_metadata = json.load(f)

        # Check for empty arrays explicitly if that's a valid state after generation errors
        if doc_embeddings.shape[0] == 0 and len(doc_metadata) == 0:
            print("Loaded empty (but valid) embeddings and metadata.")
            return doc_embeddings, doc_metadata

        if doc_embeddings.shape[0] != len(doc_metadata):
            print(
                f"Error: Mismatch between number of embeddings ({doc_embeddings.shape[0]}) and metadata entries ({len(doc_metadata)})."
            )
            return None, None

        print(f"{doc_embeddings.shape[0]} embeddings and metadata entries loaded.")
        return doc_embeddings, doc_metadata
    except ValueError as ve:
        print(
            f"ValueError loading embeddings/metadata: {ve}. Likely indicates a corrupted file or object array issue."
        )
        print("Consider deleting the .npy and .json files in the cache to regenerate.")
        return None, None
    except Exception as e:
        print(f"Generic error loading embeddings/metadata: {e}")
        return None, None


def get_book_name():
    # This function can be modified to dynamically determine the book name if needed
    return "calculus_full"


def get_book_markdown_path(book_name, chapter, section):
    return f"parsed_output/{book_name}/{book_name}-{chapter}/{book_name}-{section}/content.md"


def get_book_content(book_name, chapter, section):
    file_path = get_book_markdown_path(book_name, chapter, section)
    print(
        f"Retrieving content for chapter: {chapter}, section: {section} from {file_path}"
    )
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        data = f.read()
        data = data.replace("# ", "### ")
        return data


def get_section_name(book_name, section):
    toc_path = f"parsed_output/{book_name}/toc.csv"
    print(f"Retrieving section name for section: {section} from {toc_path}")
    if not os.path.exists(toc_path):
        return "Unknown Section"
    section = section.replace("-", ".")
    with open(toc_path, "r") as f:
        for line in f:
            if line.startswith(section + ","):
                return line.split(",")[1].strip().replace('"', "")
    return "Unknown Section"


def get_top5_documents(problem_query):
    global model, doc_embeddings, doc_metadata
    # Encode the query
    query_embedding = model.encode(problem_query)

    # Compute cosine similarities
    scores = model.similarity(query_embedding, doc_embeddings)[0]

    doc_score_pairs = []
    for doc_idx, score in enumerate(scores):
        meta = doc_metadata[doc_idx]
        doc_score_pairs.append(
            {
                "id": meta.get("id", "Unknown ID"),
                "section": meta.get("section", "Unknown Section"),
                "chapter": meta.get("chapter", "Unknown Chapter"),
                "textbook": meta.get("textbook", "Unknown Textbook"),
                "score": score.item() if hasattr(score, "item") else score,
            }
        )

    # Sort by score descending
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x["score"], reverse=True)

    # Get top 5 results
    doc_score_pairs = doc_score_pairs[:5]
    print(type(doc_score_pairs))
    print(type(doc_score_pairs[0]))
    print(doc_score_pairs[0])

    return doc_score_pairs


@app.route("/api/retrieve-documents", methods=["POST"])
def retrieve():
    global model, doc_embeddings, doc_metadata

    if model is None:
        return jsonify({"error": "Model not loaded or failed to load"}), 500

    if doc_embeddings is None or doc_metadata is None:
        return (
            jsonify({"error": "Embeddings or metadata not loaded or failed to load"}),
            500,
        )

    if len(doc_metadata) == 0:
        return jsonify({"documents": []}), 200

    data = request.json
    problem_query = data.get("problem")
    if not problem_query:
        return jsonify({"error": "Query cannot be empty"}), 400

    doc_score_pairs = get_top5_documents(problem_query)
    if not doc_score_pairs:
        return jsonify({"documents": []}), 200

    # results = [{"chapter": doc_metadata[i]["chapter"], "section": doc_metadata[i]["section"], "similarity": float(scores[i])} for i in top_indices]
    results = {
        "documents": [
            {
                "content": get_book_content(
                    doc["textbook"], doc["chapter"], doc["section"]
                ),
                "filename": f"[{BOOK_NAME_MAP[doc['textbook']]}] "
                + f"Chapter {doc['section']} - "
                + get_section_name(doc["textbook"], doc["section"]),
            }
            for doc in doc_score_pairs
        ]
    }
    # print(results)

    return jsonify(results), 200


@app.route("/api/similar-problems", methods=["POST"])
def similar_problems():
    global model
    # print("Surprisingly, this is the similar_problem endpoint")

    if model is None:
        return jsonify({"error": "Model not loaded or failed to load"}), 500

    if doc_embeddings is None or doc_metadata is None:
        return (
            jsonify({"error": "Embeddings or metadata not loaded or failed to load"}),
            500,
        )

    if len(doc_metadata) == 0:
        return jsonify({"documents": []}), 200

    data = request.json
    problem_query = data.get("problem")
    if not problem_query:
        return jsonify({"error": "Query cannot be empty"}), 400

    # Get similar problem from top 5
    doc_score_pairs = get_top5_documents(problem_query)
    top15_docs = get_almost_top15(doc_score_pairs)
    # print("Top 15 documents retrieved for similar problems:")
    # print(top15_docs)
    top15_doc_embeddings = model.encode(top15_docs)

    # Encode the query
    query_embedding = model.encode(problem_query)

    # Compute cosine similarities

    scores = model.similarity(query_embedding, top15_doc_embeddings)[0]

    doc_score_pairs = []
    for doc_idx, score in enumerate(scores):
        meta = top15_docs[doc_idx]
        # print("Meta information for document:")
        # print(meta)
        doc_score_pairs.append(
            {
                "id": meta.get("id", "Unknown ID"),
                "section": meta.get("subchapter", "Unknown Section"),
                "chapter": meta.get("chapter", "Unknown Chapter"),
                "problem": meta.get("problem", "Unknown Textbook"),
                "textbook": meta.get("textbook", "Unknown Textbook"),
                "score": score.item() if hasattr(score, "item") else score,
            }
        )
    # Sort by score descending
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x["score"], reverse=True)
    # Get top 5 results
    doc_score_pairs = doc_score_pairs[:5]

    results = {
        "documents": [
            {
                "content": doc["problem"],
                "filename": f"[{BOOK_NAME_MAP[doc['textbook']]}] "
                + f"Chapter {doc['section']} - "
                + get_section_name(doc["textbook"], doc["section"]),
            }
            for doc in doc_score_pairs
        ]
    }
    # print(results)

    return jsonify(results), 200


# Enable CORS for the Flask app
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow all origins for API routes

# Load the model when the Flask app starts
with app.app_context():
    load_model_and_embeddings()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=5001, debug=True
    )  # Set debug=True for development purposes
