import json
import numpy as np
import gc
import random
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import os

from utils import load_all_documents

# --- Configuration ---
BOOK_NAME = "Chemistry2e"
MODEL_NAME = 'Snowflake/snowflake-arctic-embed-l-v2.0' # Keep your actual model
EMBEDDINGS_DIR = f"embeddings_cache/{BOOK_NAME}"
EMBEDDINGS_FILE = os.path.join(EMBEDDINGS_DIR, "doc_embeddings.npy")
METADATA_FILE = os.path.join(EMBEDDINGS_DIR, "doc_metadata.json")

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

def generate_and_save_embeddings(documents, model_instance, embeddings_path, metadata_path):
    print(f"Generating embeddings for {len(documents)} documents (will save at the end)...")
    if not documents:
        print("No documents to process. Saving empty files.")
        np.save(embeddings_path, np.array([]).astype(np.float32)) # Save an empty typed numpy array
        with open(metadata_path, 'w') as f:
            json.dump([], f)
        return

    # Determine embedding dimension once
    embedding_dim = -1
    try:
        # Find first non-empty document to get embedding dimension
        first_valid_content = None
        for doc_content_check in documents:
            if doc_content_check.get('content','').strip():
                first_valid_content = doc_content_check['content']
                break
        if first_valid_content:
            dummy_emb = model_instance.encode([first_valid_content])[0]
        else: # All docs are empty or only whitespace
            dummy_emb = model_instance.encode(["test sentence for dimension"])[0]
        embedding_dim = dummy_emb.shape[0]
        del dummy_emb
        gc.collect()
    except Exception as e:
        print(f"CRITICAL ERROR: Could not determine embedding dimension: {e}. Cannot proceed.")
        # Create empty files if an error occurs to prevent load failures later
        if not os.path.exists(embeddings_path): np.save(embeddings_path, np.array([]).astype(np.float32))
        if not os.path.exists(metadata_path):
            with open(metadata_path, 'w') as f: json.dump([], f)
        return # Exit if dimension cannot be determined


    doc_embeddings_list = [] # Accumulate embeddings in a Python list
    doc_metadata_list = []

    for idx, doc in tqdm(enumerate(documents), total=len(documents), desc="Embedding documents"):
        current_doc_metadata = {
            'id': doc.get('id', f"doc_{idx}_unknown"),
            'section': doc.get('section', 'N/A_PRE_ENCODE'),
        }
        embedding_to_add = np.zeros(embedding_dim, dtype=np.float32) # Default to zeros

        try:
            content_to_encode = doc.get('content', '')
            # Update metadata with actuals before potential error
            current_doc_metadata['id'] = doc.get('id', f"doc_{idx}")
            current_doc_metadata['section'] = doc.get('section', 'N/A')


            if not isinstance(content_to_encode, str):
                print(f"Warning: Doc content for ID {current_doc_metadata['id']} is not str, using zeros.")
                current_doc_metadata['section'] += '_TYPE_ERROR'
            elif not content_to_encode.strip():
                print(f"Warning: Doc content for ID {current_doc_metadata['id']} is empty, using zeros.")
                current_doc_metadata['section'] += '_EMPTY_CONTENT'
            else:
                # model.encode returns a list of embeddings; we take the first (and only) one.
                embedding = model_instance.encode([content_to_encode])[0]
                embedding_to_add = embedding.astype(np.float32)
                del embedding # Attempt to free memory of the raw model output

            gc.collect() # Collect garbage after each embedding

        except Exception as e:
            print(f"Error encoding document at index {idx} (ID: {current_doc_metadata['id']}): {e}")
            current_doc_metadata['section'] += '_ENCODING_ERROR'
            # embedding_to_add remains zeros if an error occurred

        finally:
            doc_embeddings_list.append(embedding_to_add)
            doc_metadata_list.append(current_doc_metadata)

    # Convert the list of embeddings to a single NumPy array
    if doc_embeddings_list:
        final_embeddings_array = np.array(doc_embeddings_list, dtype=np.float32)
    else: # Handle case where all documents failed or the list was empty
        final_embeddings_array = np.empty((0, embedding_dim), dtype=np.float32) if embedding_dim > 0 else np.array([], dtype=np.float32)


    # Save the final array and metadata
    try:
        np.save(embeddings_path, final_embeddings_array)
        print(f"All embeddings saved to {embeddings_path}")
        with open(metadata_path, 'w') as f:
            json.dump(doc_metadata_list, f, indent=2)
        print(f"Metadata saved to {metadata_path}")
    except Exception as e:
        print(f"Error during final save of embeddings or metadata: {e}")


def load_embeddings_and_metadata(embeddings_path, metadata_path):
    print("Loading pre-computed embeddings and metadata...")
    if not os.path.exists(embeddings_path) or not os.path.exists(metadata_path):
        print(f"Embedding or metadata file not found ({embeddings_path} or {metadata_path}).")
        return None, None

    try:
        doc_embeddings = np.load(embeddings_path) # Should be fine now
        with open(metadata_path, 'r') as f:
            doc_metadata = json.load(f)
        
        # Check for empty arrays explicitly if that's a valid state after generation errors
        if doc_embeddings.shape[0] == 0 and len(doc_metadata) == 0:
            print("Loaded empty (but valid) embeddings and metadata.")
            return doc_embeddings, doc_metadata
        
        if doc_embeddings.shape[0] != len(doc_metadata): # doc_embeddings is now a numpy array
            print(f"Error: Mismatch between number of embeddings ({doc_embeddings.shape[0]}) and metadata entries ({len(doc_metadata)}).")
            return None, None

        print(f"{doc_embeddings.shape[0]} embeddings and metadata entries loaded.")
        return doc_embeddings, doc_metadata
    except ValueError as ve:
        print(f"ValueError loading embeddings/metadata: {ve}. Likely indicates a corrupted file or object array issue.")
        print("Consider deleting the .npy and .json files in the cache to regenerate.")
        return None, None
    except Exception as e:
        print(f"Generic error loading embeddings/metadata: {e}")
        return None, None


# --- Main Script ---
if __name__ == "__main__":
    print("Loading SentenceTransformer model...")
    # Forcing CPU. If your Mac's MPS has enough RAM for Arctic and small batches, you can try removing device='cpu'
    # but for consistency during debugging, CPU is safer.
    model = SentenceTransformer(MODEL_NAME)
    print("Model loaded successfully.")

    if os.path.exists(EMBEDDINGS_FILE) and os.path.exists(METADATA_FILE):
        print(f"Attempting to load existing embedding files: {EMBEDDINGS_FILE}, {METADATA_FILE}")
        document_embeddings, document_metadata = load_embeddings_and_metadata(EMBEDDINGS_FILE, METADATA_FILE)
        # Check if loading failed or returned empty but valid structures that might need regeneration
        if document_embeddings is None or document_metadata is None:
            print("Failed to load existing embeddings/metadata or files are problematic. Regenerating...")
            all_documents_data = load_all_documents(BOOK_NAME)
            generate_and_save_embeddings(all_documents_data, model, EMBEDDINGS_FILE, METADATA_FILE)
            document_embeddings, document_metadata = load_embeddings_and_metadata(EMBEDDINGS_FILE, METADATA_FILE)
    else:
        print(f"No existing embedding files found. Generating...")
        all_documents_data = load_all_documents(BOOK_NAME) # Contains {'id': ..., 'content': ..., 'section': ...}
        generate_and_save_embeddings(all_documents_data, model, EMBEDDINGS_FILE, METADATA_FILE)
        document_embeddings, document_metadata = load_embeddings_and_metadata(EMBEDDINGS_FILE, METADATA_FILE)

    if document_embeddings is None or document_metadata is None :
        print("Could not load or generate document embeddings. Exiting.")
        exit()
    
    # Handle case where generation resulted in empty embeddings (e.g., all input docs were bad)
    if document_embeddings.shape[0] == 0:
        print("No document embeddings available for querying (dataset might be empty or all documents failed processing).")
    else:
        print(f"{document_embeddings.shape[0]} documents ready for querying.")
        print(f"Embedding shape of first document: {document_embeddings[0].shape}")
    
    # Load problems for queries
    problem_json_path = f"parsed_output/{BOOK_NAME}/problems_no_math.json" # Adjust path as needed
    try:
        with open(problem_json_path, 'r') as f:
            problem_data = json.load(f)
    except FileNotFoundError:
        print(f"Problem file not found: {problem_json_path}. Using dummy queries.")
        problem_data = [
            {'problem': 'What is a basic concept in chemistry?', 'subchapter': 'Intro_1'},
            {'problem': 'Describe an element.', 'subchapter': 'Elements_1'}
        ]

    random.seed(157)
    # Ensure k is not larger than the population if problem_data is small
    sample_k = min(10, len(problem_data))
    if sample_k == 0 and len(problem_data) == 0: # No problems to sample
        queries = []
        query_subchapters = []
        print("No problems found to create queries.")
    elif sample_k > 0 :
        sample_problems = random.sample(problem_data, k=sample_k)
        queries = [problem['problem'] for problem in sample_problems]
        query_subchapters = [problem['subchapter'] for problem in sample_problems]
    else: # Should not happen if sample_k logic is correct
        queries = []
        query_subchapters = []
        print("Warning: query list is empty due to sampling logic.")


    if not queries:
        print("No queries to process. Exiting.")
        exit()

    print(f"\nComputing embeddings for {len(queries)} queries...")
    query_embeddings = model.encode(queries, prompt_name="query", show_progress_bar=True)
    print("Query embeddings computed.")

    if document_embeddings.shape[0] == 0:
        print("No document embeddings to compare against. Skipping similarity computation.")
    else:
        print("\nComputing cosine similarity scores...")
        if not isinstance(document_embeddings, np.ndarray) or document_embeddings.ndim != 2:
             print(f"Error: document_embeddings is not a 2D NumPy array. Shape: {document_embeddings.shape if hasattr(document_embeddings, 'shape') else 'N/A'}")
        else:
            scores = model.similarity(query_embeddings, document_embeddings)
            print("Similarity scores computed.")

            print("\n--- Query Results ---")
            for i, query_text in enumerate(queries):
                query_id = query_subchapters[i]
                current_query_scores = scores[i]

                doc_score_pairs = []
                for doc_idx, score_val in enumerate(current_query_scores):
                    meta = document_metadata[doc_idx]
                    doc_score_pairs.append({
                        'id': meta.get('id', 'Unknown ID'),
                        'section': meta.get('section', 'Unknown Section'),
                        'score': score_val.item() 
                    })
                
                doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x['score'], reverse=True)
                
                print(f"\nQuery (Relevant Subchapter: {query_id}): {query_text}")
                for result_doc in doc_score_pairs[:5]:
                    print(f"  - Retrieved Section: {result_doc['section']} (ID: {result_doc['id']}) / Score: {result_doc['score']:.4f}")

    print("\nScript finished.")