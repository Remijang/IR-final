import json
import numpy as np
import gc
import random
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import os
import math

from utils import load_all_documents

# --- Configuration ---
BOOK_LIST = ["Biology2e", "ca", "calculus_full", "Chemistry2e", "College_Physics_2e", "os"]
BOOK_NAME = BOOK_LIST[2]
MODEL_NAME = 'Snowflake/snowflake-arctic-embed-l-v2.0' # Keep your actual model
EMBEDDINGS_DIR = f"embeddings_cache/{BOOK_NAME}"
EMBEDDINGS_FILE = os.path.join(EMBEDDINGS_DIR, "doc_embeddings.npy")
METADATA_FILE = os.path.join(EMBEDDINGS_DIR, "doc_metadata.json")

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

def generate_and_save_embeddings(documents, model_instance, embeddings_path, metadata_path):
    print(f"Generating embeddings for {len(documents)} documents (will save at the end)...")
    if not documents:
        print("No documents to process. Saving empty files.")
        np.save(embeddings_path, np.array([]).astype(np.float32))
        with open(metadata_path, 'w') as f:
            json.dump([], f)
        return

    embedding_dim = -1
    try:
        first_valid_content = None
        for doc_content_check in documents:
            if doc_content_check.get('content','').strip():
                first_valid_content = doc_content_check['content']
                break
        if first_valid_content:
            dummy_emb = model_instance.encode([first_valid_content])[0]
        else:
            dummy_emb = model_instance.encode(["test sentence for dimension"])[0]
        embedding_dim = dummy_emb.shape[0]
        del dummy_emb
        gc.collect()
    except Exception as e:
        print(f"CRITICAL ERROR: Could not determine embedding dimension: {e}. Cannot proceed.")
        if not os.path.exists(embeddings_path): np.save(embeddings_path, np.array([]).astype(np.float32))
        if not os.path.exists(metadata_path):
            with open(metadata_path, 'w') as f: json.dump([], f)
        return


    doc_embeddings_list = []
    doc_metadata_list = []

    for idx, doc in tqdm(enumerate(documents), total=len(documents), desc="Embedding documents"):
        current_doc_metadata = {
            'id': doc.get('id', f"doc_{idx}_unknown"),
            'section': doc.get('section', 'N/A_PRE_ENCODE'),
            'chapter': doc.get('chapter', 'N/A_PRE_ENCODE')
        }
        embedding_to_add = np.zeros(embedding_dim, dtype=np.float32)

        try:
            content_to_encode = doc.get('content', '')
            current_doc_metadata['id'] = doc.get('id', f"doc_{idx}")
            current_doc_metadata['section'] = doc.get('section', 'N/A')


            if not isinstance(content_to_encode, str):
                print(f"Warning: Doc content for ID {current_doc_metadata['id']} is not str, using zeros.")
                current_doc_metadata['section'] += '_TYPE_ERROR'
            elif not content_to_encode.strip():
                print(f"Warning: Doc content for ID {current_doc_metadata['id']} is empty, using zeros.")
                current_doc_metadata['section'] += '_EMPTY_CONTENT'
            else:
                embedding = model_instance.encode([content_to_encode])[0]
                embedding_to_add = embedding.astype(np.float32)
                del embedding

            gc.collect()

        except Exception as e:
            print(f"Error encoding document at index {idx} (ID: {current_doc_metadata['id']}): {e}")
            current_doc_metadata['section'] += '_ENCODING_ERROR'

        finally:
            doc_embeddings_list.append(embedding_to_add)
            doc_metadata_list.append(current_doc_metadata)

    if doc_embeddings_list:
        final_embeddings_array = np.array(doc_embeddings_list, dtype=np.float32)
    else:
        final_embeddings_array = np.empty((0, embedding_dim), dtype=np.float32) if embedding_dim > 0 else np.array([], dtype=np.float32)


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
        doc_embeddings = np.load(embeddings_path)
        with open(metadata_path, 'r') as f:
            doc_metadata = json.load(f)
        
        if doc_embeddings.shape[0] == 0 and len(doc_metadata) == 0:
            print("Loaded empty (but valid) embeddings and metadata.")
            return doc_embeddings, doc_metadata
        
        if doc_embeddings.shape[0] != len(doc_metadata):
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


if __name__ == "__main__":
    print("Loading SentenceTransformer model...")
    model = SentenceTransformer(MODEL_NAME)
    print("Model loaded successfully.")

    if os.path.exists(EMBEDDINGS_FILE) and os.path.exists(METADATA_FILE):
        print(f"Attempting to load existing embedding files: {EMBEDDINGS_FILE}, {METADATA_FILE}")
        document_embeddings, document_metadata = load_embeddings_and_metadata(EMBEDDINGS_FILE, METADATA_FILE)
        if document_embeddings is None or document_metadata is None:
            print("Failed to load existing embeddings/metadata or files are problematic. Regenerating...")
            all_documents_data = load_all_documents(BOOK_NAME)
            generate_and_save_embeddings(all_documents_data, model, EMBEDDINGS_FILE, METADATA_FILE)
            document_embeddings, document_metadata = load_embeddings_and_metadata(EMBEDDINGS_FILE, METADATA_FILE)
    else:
        print(f"No existing embedding files found. Generating...")
        all_documents_data = load_all_documents(BOOK_NAME)
        generate_and_save_embeddings(all_documents_data, model, EMBEDDINGS_FILE, METADATA_FILE)
        document_embeddings, document_metadata = load_embeddings_and_metadata(EMBEDDINGS_FILE, METADATA_FILE)

    if document_embeddings is None or document_metadata is None :
        print("Could not load or generate document embeddings. Exiting.")
        exit()
    
    if document_embeddings.shape[0] == 0:
        print("No document embeddings available for querying (dataset might be empty or all documents failed processing).")
    else:
        print(f"{document_embeddings.shape[0]} documents ready for querying.")
        print(f"Embedding shape of first document: {document_embeddings[0].shape}")
    
    problem_json_path = f"parsed_output/{BOOK_NAME}/problems_no_math.json"
    try:
        with open(problem_json_path, 'r') as f:
            problem_data = json.load(f)
    except FileNotFoundError:
        print(f"Problem file not found: {problem_json_path}. Using dummy queries.")
        problem_data = [
            {'problem': 'What is a basic concept in chemistry?', 'subchapter': 'Intro_1', 'chapter': '1'},
            {'problem': 'Describe an element.', 'subchapter': 'Elements_1', 'chapter': '1'}
        ]

    random.seed(157)
    # sample_k = min(10, len(problem_data))
    sample_k = len(problem_data)
    if sample_k == 0 and len(problem_data) == 0:
        queries = []
        query_subchapters = []
        query_chapters = []
        print("No problems found to create queries.")
    elif sample_k > 0 :
        sample_problems = random.sample(problem_data, k=sample_k)
        queries = [problem['problem'] for problem in sample_problems]
        query_subchapters = [problem['subchapter'] for problem in sample_problems]
        query_chapters = [problem['chapter'] for problem in sample_problems]
    else:
        queries = []
        query_subchapters = []
        query_chapters = []
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
            match_section_query_num = 0
            match_chapter_query_num = 0

            # Lists to store scores for averaging later
            all_ap_sections = []
            all_ap_chapters = []
            all_ndcg_at_5_sections = []
            all_ndcg_at_5_chapters = []

            k_eval = 5 # The number of top results to consider for metrics (matches your existing top 5)

            print("\n--- Query Results ---")
            for i, query_text in enumerate(queries):
                query_id_subchapter_orig = query_subchapters[i] # Keep original for print
                query_id_chapter = str(query_chapters[i])
                current_query_scores = scores[i]

                doc_score_pairs = []
                for doc_idx, score_val in enumerate(current_query_scores):
                    meta = document_metadata[doc_idx]
                    doc_score_pairs.append({
                        'id': meta.get('id', 'Unknown ID'),
                        'section': meta.get('section', 'Unknown Section'),
                        'chapter': meta.get('chapter', 'Unknown Chapter'),
                        # Handle potential tensor score values
                        'score': score_val.item() if hasattr(score_val, 'item') else score_val
                    })

                # Sort by score descending
                doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x['score'], reverse=True)

                # Normalize query_id_subchapter once for consistent comparison
                query_id_subchapter_norm = query_id_subchapter_orig.replace('.', '-')

                # --- Calculate Metrics for this Query (within top k_eval results) ---

                # SECTION metrics
                relevant_section_ranks = [] # Store 1-based ranks where target section is found
                section_gains = []          # Store relevance (1 or 0) for the top k_eval documents

                for rank_idx, doc in enumerate(doc_score_pairs[:k_eval]):
                    rank = rank_idx + 1 # 1-based rank
                    is_relevant_section = (doc['section'] == query_id_subchapter_norm)
                    if is_relevant_section:
                        relevant_section_ranks.append(rank)
                    section_gains.append(1.0 if is_relevant_section else 0.0) # Binary relevance gain

                # Average Precision (AP) for Section
                # For a single relevant item, AP is the precision at the rank where the first relevant item is found.
                # If not found, AP is 0.
                ap_section = 0.0
                if relevant_section_ranks:
                    # The first relevant item found determines the AP for a single-relevant-item query
                    first_relevant_rank = relevant_section_ranks[0] # Assuming the target is unique and we count the first hit
                    # Precision at the first relevant rank: (Number of relevant items found up to this rank) / (Rank)
                    # Since it's the first relevant item, num_relevant_found_so_far = 1
                    ap_section = 1.0 / first_relevant_rank
                    # Note: If you had MULTIPLE relevant items for a query, AP would sum precision at *each* relevant rank
                    # and divide by the total number of relevant items. Here, total relevant items for section = 1.

                all_ap_sections.append(ap_section)

                # NDCG@k_eval for Section
                dcg_section = 0.0
                for rank_idx, gain in enumerate(section_gains): # section_gains is already for top k_eval documents
                    rank = rank_idx + 1 # 1-based rank
                    dcg_section += gain / math.log2(rank + 1) # Discounted gain

                # Ideal DCG@k_eval: For a single relevant item (gain=1), ideal rank is 1.
                # IDCG@k_eval = 1.0 / math.log2(1 + 1) = 1.0 for k_eval >= 1
                # Handle case where query_id_subchapter_norm might be invalid (though unlikely with your setup)
                idcg_section = 1.0 / math.log2(1 + 1) if query_id_subchapter_norm else 0.0

                ndcg_section = dcg_section / idcg_section if idcg_section > 0 else 0.0 # Normalize DCG
                all_ndcg_at_5_sections.append(ndcg_section)


                # CHAPTER metrics (Repeat the same logic for chapters)
                relevant_chapter_ranks = []
                chapter_gains = []

                for rank_idx, doc in enumerate(doc_score_pairs[:k_eval]):
                    rank = rank_idx + 1 # 1-based rank
                    is_relevant_chapter = (doc['chapter'] == query_id_chapter)
                    if is_relevant_chapter:
                        relevant_chapter_ranks.append(rank)
                    chapter_gains.append(1.0 if is_relevant_chapter else 0.0) # Binary relevance gain

                # Average Precision (AP) for Chapter
                ap_chapter = 0.0
                if relevant_chapter_ranks:
                    first_relevant_rank = relevant_chapter_ranks[0]
                    ap_chapter = 1.0 / first_relevant_rank # Precision at the first relevant rank

                all_ap_chapters.append(ap_chapter)

                # NDCG@k_eval for Chapter
                dcg_chapter = 0.0
                for rank_idx, gain in enumerate(chapter_gains):
                    rank = rank_idx + 1
                    dcg_chapter += gain / math.log2(rank + 1)

                # Ideal DCG@k_eval for chapter (same as section logic)
                idcg_chapter = 1.0 / math.log2(1 + 1) if query_id_chapter else 0.0

                ndcg_chapter = dcg_chapter / idcg_chapter if idcg_chapter > 0 else 0.0
                all_ndcg_at_5_chapters.append(ndcg_chapter)


                # --- Original match counting (using the calculated gains) ---
                # Check if ANY relevant section was found in the top k_eval
                if any(s_gain > 0 for s_gain in section_gains):
                    match_section_query_num += 1
                # Check if ANY relevant chapter was found in the top k_eval
                if any(c_gain > 0 for c_gain in chapter_gains):
                    match_chapter_query_num += 1

                # --- Print Results for this Query ---
                # Corrected print to show subchapter ground truth
                print(f"\nQuery (Relevant chapter and subchapter: {query_id_chapter}, {query_id_subchapter_orig}): {query_text}")
                for result_doc in doc_score_pairs[:k_eval]: # Print top k_eval results
                    print(f"  - Retrieved Section: {result_doc['section']} (ID: {result_doc['id']}) / Score: {result_doc['score']:.4f}")
                    # Assuming you meant to print the retrieved chapter here, not section again
                    print(f"  - Retrieved Chapter: {result_doc['chapter']} (ID: {result_doc['id']}) / Score: {result_doc['score']:.4f}")

                # Print the calculated metrics for this specific query
                print(f"  Metrics for this query (evaluated @{k_eval}):")
                print(f"    AP (Section): {ap_section:.4f}, NDCG@{k_eval} (Section): {ndcg_section:.4f}")
                print(f"    AP (Chapter): {ap_chapter:.4f}, NDCG@{k_eval} (Chapter): {ndcg_chapter:.4f}")


            # --- Print Overall Metrics ---
            print(f"\n--- Summary (evaluated @{k_eval}) ---")
            print(f"Total queries: {len(queries)}")
            print(f"Total queries matched with relevant sections (in top {k_eval}): {match_section_query_num}/{len(queries)}")
            print(f"Total queries matched with relevant chapters (in top {k_eval}): {match_chapter_query_num}/{len(queries)}")


            # Calculate and print MAP and Mean NDCG
            # Handle case where queries might be empty to avoid division by zero
            num_queries = len(queries)

            map_sections_score = sum(all_ap_sections) / num_queries if num_queries > 0 else 0.0
            map_chapters_score = sum(all_ap_chapters) / num_queries if num_queries > 0 else 0.0
            mean_ndcg_sections_score = sum(all_ndcg_at_5_sections) / num_queries if num_queries > 0 else 0.0
            mean_ndcg_chapters_score = sum(all_ndcg_at_5_chapters) / num_queries if num_queries > 0 else 0.0

            print(f"\n--- Overall Metrics (evaluated @{k_eval}) ---")
            print(f"MAP (Sections): {map_sections_score:.4f}")
            print(f"MAP (Chapters): {map_chapters_score:.4f}")
            print(f"Mean NDCG@{k_eval} (Sections): {mean_ndcg_sections_score:.4f}")
            print(f"Mean NDCG@{k_eval} (Chapters): {mean_ndcg_chapters_score:.4f}")

    print("\nScript finished.")