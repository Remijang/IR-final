import os

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

if __name__ == "__main__":
    book_name = "Chemistry2e"
    documents = load_all_documents(book_name)
    print(f"Total Documents Loaded: {len(documents)}")
    for doc in documents[:5]:  # Print first 5 documents for verification
        print(f"Chapter: {doc['chapter']}, Section: {doc['section']}, Content Length: {len(doc['content'])}")