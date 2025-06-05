import json
import numpy as np
import gc
import random
from tqdm import tqdm
import bm25s
import os
import math
import nltk

from utils import load_all_documents

# --- Configuration ---
BOOK_LIST = ["Biology2e", "ca", "calculus_full", "Chemistry2e", "College_Physics_2e", "os"]
BOOK_NAME = BOOK_LIST[2]
EMBEDDINGS_DIR = f"embeddings_cache/{BOOK_NAME}"
METADATA_FILE = os.path.join(EMBEDDINGS_DIR, "doc_metadata.json")

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

# It's good practice to check library versions if you suspect issues
# print(f"NLTK version: {nltk.__version__}")
# if hasattr(bm25s, '__version__'):
#    print(f"bm25s version: {bm25s.__version__}")
# else:
#    print("bm25s version: (unable to determine, consider adding __version__ to the library or check setup.py)")


def generate_and_save_metadata(documents, metadata_path):
    print(f"Generating metadata for {len(documents)} documents...")
    if not documents:
        print("No documents to process. Saving empty metadata file.")
        with open(metadata_path, 'w') as f:
            json.dump([], f)
        return []

    doc_metadata_list = []

    for idx, doc in tqdm(enumerate(documents), total=len(documents), desc="Processing document metadata"):
        current_doc_metadata = {
            'id': doc.get('id', f"doc_{idx}_unknown_meta"),
            'section': doc.get('section', 'N/A_META'),
            'chapter': doc.get('chapter', 'N/A_META')
        }

        content_for_check = doc.get('content', '')

        if not isinstance(content_for_check, str):
            print(f"Warning: Doc content for ID {current_doc_metadata['id']} is not str.")
        elif not content_for_check.strip():
            print(f"Warning: Doc content for ID {current_doc_metadata['id']} is empty.")

        doc_metadata_list.append(current_doc_metadata)

    try:
        with open(metadata_path, 'w') as f:
            json.dump(doc_metadata_list, f, indent=2)
        print(f"Metadata saved to {metadata_path}")
    except Exception as e:
        print(f"Error during save of metadata: {e}")
        return []

    return doc_metadata_list


def load_metadata(metadata_path):
    print("Loading pre-computed metadata...")
    if not os.path.exists(metadata_path):
        print(f"Metadata file not found ({metadata_path}).")
        return None

    try:
        with open(metadata_path, 'r') as f:
            doc_metadata = json.load(f)

        if len(doc_metadata) == 0:
            print("Loaded empty (but valid) metadata.")

        print(f"{len(doc_metadata)} metadata entries loaded.")
        return doc_metadata
    except json.JSONDecodeError as ve:
        print(f"JSONDecodeError loading metadata: {ve}. Likely indicates a corrupted JSON file.")
        print("Consider deleting the .json file in the cache to regenerate.")
        return None
    except Exception as e:
        print(f"Generic error loading metadata: {e}")
        return None


if __name__ == "__main__":
    all_documents_data = load_all_documents(BOOK_NAME)
    document_metadata = None

    if os.path.exists(METADATA_FILE):
        print(f"Attempting to load existing metadata file: {METADATA_FILE}")
        document_metadata = load_metadata(METADATA_FILE)

    if document_metadata is None or (all_documents_data and len(document_metadata) != len(all_documents_data)):
        if document_metadata is None:
            print("Failed to load existing metadata or file is problematic. Regenerating...")
        else:
            print(f"Metadata count ({len(document_metadata)}) mismatch with document count ({len(all_documents_data)}). Regenerating...")
        if not all_documents_data:
             print("No documents loaded from source. Cannot generate metadata. Ensure 'utils.load_all_documents' provides data.")
             if not os.path.exists(METADATA_FILE):
                 generate_and_save_metadata([], METADATA_FILE)
                 document_metadata = []
        else:
            document_metadata = generate_and_save_metadata(all_documents_data, METADATA_FILE)

    if not all_documents_data and (document_metadata is None or not document_metadata):
        print("No documents found from source and no metadata available. Exiting.")
        exit()
    elif all_documents_data and (document_metadata is None or len(document_metadata) != len(all_documents_data)):
        print("CRITICAL: Mismatch between loaded documents and metadata even after regeneration attempt. Exiting.")
        exit()
    elif not all_documents_data and document_metadata:
        print("Warning: No documents loaded from source, but existing metadata was found. Proceeding with empty corpus for BM25.")

    print(f"{len(document_metadata if document_metadata else [])} documents and metadata entries loaded/generated.")

    print("Initializing BM25 ranker...")
    ranker = None
    try:
        try:
            nltk.data.find('tokenizers/punkt')
            print("NLTK 'punkt' resource found.")
        except LookupError:
            print("NLTK 'punkt' resource not found. Attempting to download...")
            try:
                nltk.download('punkt', quiet=False)
                print("NLTK 'punkt' resource downloaded successfully.")
                nltk.data.find('tokenizers/punkt')
                print("NLTK 'punkt' resource verified after download.")
            except Exception as download_e:
                print(f"Failed to download or verify NLTK 'punkt' resource after attempt: {download_e}")
                print("Please ensure you have an internet connection and try manually in a Python interpreter: import nltk; nltk.download('punkt')")
                exit()

        ranker = bm25s.BM25()
    except ImportError:
        print("NLTK is not installed, which is required by the default bm25s.BM25() tokenizer.")
        print("Please install NLTK: pip install nltk")
        exit()
    except Exception as e:
        print(f"Error initializing BM25 or checking NLTK resources: {e}")
        exit()

    print("Preparing corpus for BM25...")
    corpus_contents = [doc.get('content', '') for doc in all_documents_data] if all_documents_data else []

    if not corpus_contents and all_documents_data:
        print("Warning: All documents loaded have empty or missing content. BM25 index will be empty or ineffective.")
    elif not all_documents_data:
        print("No document content found to index with BM25 (corpus is empty based on source data).")

    print(f"Tokenizing {len(corpus_contents)} documents for BM25...")
    tokenized_corpus = bm25s.tokenize(corpus_contents)
    print("Indexing tokenized documents with BM25...")
    ranker.index(tokenized_corpus)
    # The line below is where the AttributeError occurred.
    # `corpus_size` is the correct attribute for bm25s v0.2.13.
    # If this line fails after renaming your script, the bm25s installation or environment is suspect.

    # Updated line to handle potential API changes in bm25s
    if hasattr(ranker, 'corpus_size'):
        print(f"BM25 indexing complete for {ranker.corpus_size} documents.")
    elif hasattr(ranker, 'ndocs'): # Fallback for older versions if corpus_size isn't found
        print(f"BM25 indexing complete for {ranker.ndocs} documents.")
    else:
        print("BM25 indexing complete, but unable to determine corpus size (attribute not found).")


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
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {problem_json_path}. Using dummy queries.")
        problem_data = [
            {'problem': 'What is a basic concept in chemistry?', 'subchapter': 'Intro_1', 'chapter': '1'},
            {'problem': 'Describe an element.', 'subchapter': 'Elements_1', 'chapter': '1'}
        ]

    random.seed(157)
    queries = []
    query_subchapters = []
    query_chapters = []

    if not problem_data:
        print("No problems found to create queries.")
    else:
        if isinstance(problem_data, list) and len(problem_data) > 0:
            sample_k = len(problem_data) # Process all problems
            # sample_k = min(10, len(problem_data)) # Or a subset for faster testing
            sample_problems = random.sample(problem_data, k=sample_k) if sample_k > 0 and sample_k <= len(problem_data) else []

            queries = [problem.get('problem', '') for problem in sample_problems]
            query_subchapters = [problem.get('subchapter', 'N/A') for problem in sample_problems]
            query_chapters = [str(problem.get('chapter', 'N/A')) for problem in sample_problems]
        else:
            print("Problem data is empty or not in the expected list format. No queries will be processed.")

    # Filter out empty/invalid queries to ensure valid strings
    queries = [q for q in queries if isinstance(q, str) and q.strip()]

    if not queries:
        print("No queries to process. Exiting.")
        exit()

    print(f"\nTokenizing {len(queries)} queries for BM25 (using NLTK)...")
    # Manually tokenize queries using NLTK to ensure correct list of lists format
    tokenized_queries_list = []
    for query_text in queries:
        # Convert to lowercase for consistent tokenization with corpus
        tokenized_queries_list.append(nltk.word_tokenize(query_text.lower()))
    print("Query tokenization for BM25 complete.")

    # --- Debug prints for tokenized_queries_list ---
    print(f"Type of tokenized_queries_list: {type(tokenized_queries_list)}")
    if isinstance(tokenized_queries_list, list):
        print(f"Length of tokenized_queries_list: {len(tokenized_queries_list)}")
        if len(tokenized_queries_list) > 0:
            print(f"Type of first element in tokenized_queries_list: {type(tokenized_queries_list[0])}")
            if isinstance(tokenized_queries_list[0], list):
                print(f"Length of first inner list: {len(tokenized_queries_list[0])}")
                if len(tokenized_queries_list[0]) > 0:
                    print(f"Type of first token: {type(tokenized_queries_list[0][0])}")
                    print(f"Example of first token: {tokenized_queries_list[0][0]}")
            else:
                print("First element of tokenized_queries_list is NOT a list (EXPECTED LIST).")
        else:
            print("tokenized_queries_list is an empty list.")
    else:
        print("tokenized_queries_list is NOT a list (EXPECTED LIST).")
    # --- End debug prints ---


    if (hasattr(ranker, 'corpus_size') and ranker.corpus_size == 0) or \
       (hasattr(ranker, 'ndocs') and ranker.ndocs == 0):
        print("No documents in BM25 index to compare against. Skipping similarity computation.")
    else:
        print("\nComputing BM25 scores...")
        # Pass the manually extracted list of tokens
        scores = []
        for tokenized_query in tokenized_queries_list:
            score = ranker.get_scores(tokenized_query)
            scores.append(score)

        print("BM25 scores computed.")

        match_section_query_num = 0
        match_chapter_query_num = 0

        all_ap_sections = []
        all_ap_chapters = []
        all_ndcg_at_5_sections = []
        all_ndcg_at_5_chapters = []

        k_eval = 5

        print("\n--- Query Results ---")
        for i, query_text in enumerate(queries):
            query_id_subchapter_orig = query_subchapters[i]
            query_id_chapter = str(query_chapters[i])
            current_query_scores = scores[i]

            doc_score_pairs = []
            for doc_idx, score_val in enumerate(current_query_scores):
                if doc_idx < len(document_metadata):
                    meta = document_metadata[doc_idx]
                    doc_score_pairs.append({
                        'id': meta.get('id', 'Unknown ID'),
                        'section': meta.get('section', 'Unknown Section'),
                        'chapter': meta.get('chapter', 'Unknown Chapter'),
                        'score': score_val.item() if hasattr(score_val, 'item') else score_val
                    })
                else:
                    print(f"Warning: doc_idx {doc_idx} out of bounds for document_metadata (len {len(document_metadata)}). Score: {score_val}")

            doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x['score'], reverse=True)
            query_id_subchapter_norm = query_id_subchapter_orig.replace('.', '-')

            relevant_section_ranks = []
            section_gains = []
            for rank_idx, doc in enumerate(doc_score_pairs[:k_eval]):
                rank = rank_idx + 1
                is_relevant_section = (doc.get('section') == query_id_subchapter_norm)
                if is_relevant_section:
                    relevant_section_ranks.append(rank)
                section_gains.append(1.0 if is_relevant_section else 0.0)

            ap_section = 0.0
            if relevant_section_ranks:
                first_relevant_rank = relevant_section_ranks[0]
                ap_section = 1.0 / first_relevant_rank
            all_ap_sections.append(ap_section)

            dcg_section = 0.0
            for rank_idx, gain in enumerate(section_gains):
                rank = rank_idx + 1
                dcg_section += gain / math.log2(rank + 1)

            ideal_gain_at_rank_1 = 1.0 / math.log2(1 + 1)
            target_section_exists_in_corpus = False
            if document_metadata:
                target_section_exists_in_corpus = any(
                    doc_meta.get('section') == query_id_subchapter_norm for doc_meta in document_metadata
                )
            idcg_section = ideal_gain_at_rank_1 if target_section_exists_in_corpus else 0.0

            ndcg_section = dcg_section / idcg_section if idcg_section > 0 else 0.0
            all_ndcg_at_5_sections.append(ndcg_section)

            relevant_chapter_ranks = []
            chapter_gains = []
            for rank_idx, doc in enumerate(doc_score_pairs[:k_eval]):
                rank = rank_idx + 1
                is_relevant_chapter = (doc.get('chapter') == query_id_chapter)
                if is_relevant_chapter:
                    relevant_chapter_ranks.append(rank)
                chapter_gains.append(1.0 if is_relevant_chapter else 0.0)

            ap_chapter = 0.0
            if relevant_chapter_ranks:
                first_relevant_rank = relevant_chapter_ranks[0]
                ap_chapter = 1.0 / first_relevant_rank
            all_ap_chapters.append(ap_chapter)

            dcg_chapter = 0.0
            for rank_idx, gain in enumerate(chapter_gains):
                rank = rank_idx + 1
                dcg_chapter += gain / math.log2(rank + 1)

            target_chapter_exists_in_corpus = False
            if document_metadata:
                target_chapter_exists_in_corpus = any(
                    doc_meta.get('chapter') == query_id_chapter for doc_meta in document_metadata
                )
            idcg_chapter = ideal_gain_at_rank_1 if target_chapter_exists_in_corpus else 0.0

            ndcg_chapter = dcg_chapter / idcg_chapter if idcg_chapter > 0 else 0.0
            all_ndcg_at_5_chapters.append(ndcg_chapter)

            if any(s_gain > 0 for s_gain in section_gains):
                match_section_query_num += 1
            if any(c_gain > 0 for c_gain in chapter_gains):
                match_chapter_query_num += 1

            print(f"\nQuery (Relevant chapter and subchapter: {query_id_chapter}, {query_id_subchapter_orig}): {query_text}")
            for result_doc_idx, result_doc in enumerate(doc_score_pairs[:k_eval]):
                print(f"  Rank {result_doc_idx+1}:")
                print(f"    - Retrieved Section: {result_doc.get('section')} (ID: {result_doc.get('id')}) / Score: {result_doc.get('score'):.4f}")
                print(f"    - Retrieved Chapter: {result_doc.get('chapter')} (ID: {result_doc.get('id')}) / Score: {result_doc.get('score'):.4f}")


            print(f"  Metrics for this query (evaluated @{k_eval}):")
            print(f"    AP (Section): {ap_section:.4f}, NDCG@{k_eval} (Section): {ndcg_section:.4f}")
            print(f"    AP (Chapter): {ap_chapter:.4f}, NDCG@{k_eval} (Chapter): {ndcg_chapter:.4f}")

        print(f"\n--- Summary (evaluated @{k_eval}) ---")
        print(f"Total queries: {len(queries)}")
        print(f"Total queries matched with relevant sections (in top {k_eval}): {match_section_query_num}/{len(queries)}")
        print(f"Total queries matched with relevant chapters (in top {k_eval}): {match_chapter_query_num}/{len(queries)}")

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