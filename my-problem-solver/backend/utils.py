import os
import numpy as np
import json
import random

def load_all_documents(book_name):
    book_path = f"parsed_output/{book_name}"
    documents = []

    total_length = 0
    total_documents = 0

    for chapter in os.listdir(book_path):
        chapter_path = os.path.join(book_path, chapter)
        chapter_total_length = 0
        chapter_documents = 0
        if os.path.isdir(chapter_path):
            for section in os.listdir(chapter_path):
                section_path = os.path.join(chapter_path, section)
                if not os.path.isdir(section_path):
                    continue
                file_path = os.path.join(section_path, "content.txt")
                with open(file_path, 'r') as f:
                    data = f.read()
                    documents.append({
                        'chapter': chapter.replace(book_name + "-", ""),
                        'section': section.replace(book_name + "-", ""),
                        'content': data
                    })
                    chapter_total_length += len(data)
                    chapter_documents += 1
        else:
            continue

        # print("Chapter:", chapter, "Total Length:", chapter_total_length)
        # print("Chapter Documents:", chapter_documents)
        # print("Chatper Average Length:", chapter_total_length / chapter_documents if chapter_documents > 0 else 0)
        # print()
        total_length += chapter_total_length
        total_documents += chapter_documents
    
    documents.sort(key=lambda x: (x['chapter'], x['section']))
    return documents

def _load_embeddings_and_metadata(embeddings_path, metadata_path, book_name):
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
        
        for data in doc_metadata:
            data['textbook'] = book_name

        print(f"{doc_embeddings.shape[0]} embeddings and metadata entries loaded.")
        return doc_embeddings, doc_metadata
    except ValueError as ve:
        print(f"ValueError loading embeddings/metadata: {ve}. Likely indicates a corrupted file or object array issue.")
        print("Consider deleting the .npy and .json files in the cache to regenerate.")
        return None, None
    except Exception as e:
        print(f"Generic error loading embeddings/metadata: {e}")
        return None, None

def load_all_embeddings():
    embeddings = []
    metadatas = []
    for textbook in os.listdir("embeddings_cache"):
        embedding_dir = f"embeddings_cache/{textbook}"
        embedding_file = os.path.join(embedding_dir, "doc_embeddings.npy")
        metadata_file = os.path.join(embedding_dir, "doc_metadata.json")
        doc_embeddings, doc_metadata = _load_embeddings_and_metadata(embedding_file, metadata_file, textbook)
        embeddings.extend(doc_embeddings)
        metadatas.extend(doc_metadata)
    return np.array(embeddings), metadatas

def _get_content_under_dir(dir_path: str):
    ret = ""
    lis = sorted(os.listdir(dir_path))
    if "content.md" in lis:
        file_path = os.path.join(dir_path, "content.md")
        with open(file_path, 'r') as f:
            text = f.read()
        f.close()
        ret += text
    for sub in lis:
        sub_path = os.path.join(dir_path, sub)
        if os.path.isdir(sub_path):
            ret += _get_content_under_dir(sub_path)
    return ret

def get_textbook(textbook: str, chapter: str, subchapter: str):
    if subchapter == "":
        dir_path = f"parsed_output/{textbook}/{textbook}-{chapter}/"
    else:
        subchapter.replace('.', '-')
        dir_path = f"parsed_output/{textbook}/{textbook}-{chapter}/{textbook}-{subchapter}"
    return _get_content_under_dir(dir_path=dir_path)
    
PROBLEM_NO_MATH = False

def get_almost_top15(top5_docs: list):
    candidate = []
    for doc in top5_docs:
        subchapter = str(doc['section']).replace('-', '.')
        chapter = str(doc['chapter'])
        textbook = doc['textbook']
        if PROBLEM_NO_MATH:
            problem_path = f"parsed_output/{textbook}/problems_no_math.json"
        else:
            problem_path = f"parsed_output/{textbook}/problems.json"

        with open(problem_path, 'r') as f:
            problems = json.load(f)
        if subchapter == "":
            filtered = [p for p in problems if p['chapter'] == chapter]
        else:
            filtered = [p for p in problems if p['subchapter'] == subchapter]
            if len(filtered) == 0:
                filtered = [p for p in problems if p['chapter'] == chapter]
        
        for p in filtered:
            p['textbook'] = textbook
            p['chapter'] = chapter
            p['section'] = subchapter

        num_to_sample = min(3, len(filtered))
        sample = random.sample(filtered, num_to_sample)
        candidate += sample
    s = set()
    ret = []
    for p in candidate:
        if p["problem"] in s:
            continue
        s.add(p["problem"])
        ret.append(p)
    return ret


if __name__ == "__main__":
    book_name = "Chemistry2e"
    documents = load_all_documents(book_name)
    print(f"Total Documents Loaded: {len(documents)}")
    for doc in documents[:5]:  # Print first 5 documents for verification
        print(f"Chapter: {doc['chapter']}, Section: {doc['section']}, Content Length: {len(doc['content'])}")

    a, b = load_all_embeddings()
    print(len(a))
    print(len(b))

    c = []
    for bb in b:
        if bb['textbook'] == "Chemistry2e":
            c.append(bb)

    print(c[:10])
    text = get_textbook("os", "2", "")
    print(text)

    doc = [
        {'textbook': "os", "chapter": "4", "section": "4.1"},
        {'textbook': "os", "chapter": 5, "section": "5.1"},
    ]
    top15 = get_almost_top15(doc)
    for i in top15:
        print(i)