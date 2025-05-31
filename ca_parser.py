import os
import json
import pandas as pd

# base_path = 'textbooks_output'
book_name = "ca"
# book_base_path = os.path.join(base_path, book_name)
# book_base_path = os.path.join(book_base_path, 'auto')

# print(book_base_path)

# list all files in the directory
book_base_path = os.path.join(os.getcwd(), "textbooks_output", book_name, "auto")
output_path = os.path.join(os.getcwd(), "parsed_output", book_name)
if not os.path.exists(output_path):
    os.makedirs(output_path)


def get_content_list_json():
    with open(os.path.join(book_base_path, f"{book_name}_content_list.json"), "r") as f:
        content_list_json = json.load(f)
    return content_list_json


def get_toc_list():
    content_list_json = get_content_list_json()

    toc_list = []
    for content in content_list_json:
        if content["page_idx"] < 3:
            continue
        if content["page_idx"] >= 15:
            break
        if content["type"] != "text":
            continue
        toc_list.extend(content["text"].split("\n"))

    return toc_list


def save_toc_to_txt():
    toc_list = get_toc_list()
    toc_path = os.path.join(output_path, "toc.txt")
    with open(toc_path, "w") as f:
        toc_list = list(map(lambda x: x.strip(), toc_list))
        toc_list = list(filter(lambda x: len(x) > 0, toc_list))
        toc_list = list(map(lambda x: x.replace(". ", ""), toc_list))
        toc_list = list(map(lambda x: x.replace(" $^ *$", "\\*"), toc_list))

        # Uncomment this line with caution, will clear the file
        print(*toc_list, file=f, sep="\n")


def toc_txt_to_csv():
    toc_path = os.path.join(output_path, "toc.txt")
    with open(toc_path, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    chapters = []
    sections = []
    pages = []
    for line in lines:
        line_list = line.split(" ")
        chapter = line_list[0]
        chapters.append(chapter)
        page = line_list[-1]
        pages.append(page)
        section = " ".join(line_list[1:-1])
        sections.append(section)
    toc_csv_path = os.path.join(output_path, "toc.csv")
    with open(toc_csv_path, "w") as f:
        print("Chapter,Section,Page", file=f)
        for i in range(len(chapters)):
            print(f'{chapters[i]},"{sections[i]}",{pages[i]}', file=f)
    return chapters, sections, pages


def page_to_page_idx(page):
    return page + 2


def init_new_toc():
    content_list_json_path = os.path.join(
        book_base_path, f"{book_name}_content_list.json"
    )
    content_list_df = pd.read_json(content_list_json_path)
    toc_path = os.path.join(output_path, "toc.csv")
    df = pd.read_csv(toc_path)
    content_list_idx = 0
    content_list_results = []

    for index, row in df.iterrows():
        chapter = row["Chapter"]
        section = row["Section"]
        page = int(row["Page"])
        page_idx = page_to_page_idx(page)
        not_found = False
        while content_list_df.iloc[content_list_idx]["page_idx"] < page_idx:
            content_list_idx += 1

        temp_idx = content_list_idx
        while True:
            content = content_list_df.iloc[content_list_idx]
            if content["type"] != "text":
                content_list_idx += 1
                continue
            text = content_list_df.iloc[content_list_idx]["text"]
            text = text.strip()

            chapter_name = chapter + " " + section
            if chapter_name[0] == "I":
                # Chapter name using Roman numerals, e.g. I, II, III
                chapter_name = section

            if chapter in ["3", "4", "8", "9", "B"]:
                # Chapter 3, 8, 9, B are not detected by OCR
                content_list_idx = temp_idx - 1
                not_found = True
                break

            if chapter_name in text:
                # print("Found chapter and section")
                break

            if section in text and len(chapter) == 1:
                # Some sections are not detected by OCR, but chapter is detected
                break

            content_list_idx += 1
            if content_list_df.iloc[content_list_idx]["page_idx"] != page_idx:
                try:
                    # Try using text_level
                    content_list_idx = temp_idx
                    while (
                        content_list_df.iloc[content_list_idx]["page_idx"] == page_idx
                    ):
                        if content_list_df.iloc[content_list_idx]["text_level"] == 1:
                            break
                        content_list_idx += 1
                    if content_list_df.iloc[content_list_idx]["page_idx"] == page_idx:
                        break

                    # print(f"Chapter: {chapter}, Section: {section}, Page: {page} not found in page_idx: {page_idx}")
                    not_found = True
                    assert (
                        False
                    ), f"Chapter: {chapter}, Section: {section}, Page: {page} not found in page_idx: {page_idx}"
                except:
                    content_list_idx = temp_idx - 1  # reset to the last found index
                    not_found = True
                    break

        # print(f"{chapter} {section}, Page: {page}")
        # print(content_list_df.iloc[content_list_idx]['text'])
        if not not_found:
            content_list_results.append(
                {
                    "chapter": chapter,
                    "section": section,
                    "page": page,
                    "json_idx": content_list_idx,
                }
            )
        else:
            content_list_results.append(
                {
                    "chapter": chapter,
                    "section": section,
                    "page": page,
                    "json_idx": content_list_idx + 1,
                }
            )

        if (not not_found) and (
            f"{chapter} {section}" in content_list_df.iloc[content_list_idx]["text"]
        ):
            pass
            # print(f"{chapter} {section}, Page: {page}")
            # print(content_list_df.iloc[content_list_idx]['text'])
            # print()
        elif not not_found:
            print(f"{chapter} {section}, Page: {page}")
            print(content_list_df.iloc[content_list_idx]["text"])
            print()
        else:
            print(
                f"Chapter: {chapter}, Section: {section}, Page: {page} not found in page_idx: {page_idx}"
            )
            print()
        content_list_idx += 1

    df = pd.DataFrame(content_list_results)
    toc_new_path = os.path.join(output_path, "toc_new.csv")
    df.to_csv(toc_new_path, index=False)

    return content_list_results


def load_toc_new_csv():
    toc_new_path = os.path.join(output_path, "toc_new.csv")
    toc_new = pd.read_csv(toc_new_path)
    return toc_new


def get_chapter_output_path(chapter):
    chapters = chapter.split(".")
    chapter_name = book_name
    chapter_path = output_path
    for chap in chapters:
        if chapter_name:
            chapter_name += "-"
        chapter_name += chap
        chapter_path = os.path.join(chapter_path, chapter_name)

    return chapter_path


def remove_math_symbols(text):
    import re
    return re.sub(r'\$[^\$]*\$', '', text)  # Remove inline math symbols


def json_to_text(json_data):
    content = ""
    for item in json_data:
        if not item["type"] == "text":
            continue
        text = item["text"].strip()
        text = remove_math_symbols(text)
        if not text:
            continue
        content += text + "\n\n"
    return content.strip()


def parse_content_list_json():
    toc_new_df = load_toc_new_csv()
    content_list_json = get_content_list_json()

    for index, row in toc_new_df.iterrows():
        chapter = row["chapter"]
        section = row["section"]
        page = row["page"]
        json_idx = row["json_idx"]
        if index < len(toc_new_df) - 1:
            next_json_idx = toc_new_df.iloc[index + 1]["json_idx"]
        else:
            next_json_idx = len(content_list_json)

        chapter_path = get_chapter_output_path(chapter)
        if not os.path.exists(chapter_path):
            os.makedirs(chapter_path)

        # Create content.json and content.txt for each chapter
        content_list = []
        for i in range(json_idx, next_json_idx):
            content_list.append(content_list_json[i])

        json_file_path = os.path.join(chapter_path, f"content.json")
        with open(json_file_path, "w") as json_file:
            json.dump(content_list, json_file, indent=4)

        text_file_path = os.path.join(chapter_path, f"content.txt")
        with open(text_file_path, "w") as text_file:
            content = json_to_text(content_list)
            text_file.write(content)


if __name__ == "__main__":
    # DON'T CALL THE BELOW FUNCTIONS, AS THE FILE HAS BEEN MANUALLY MODIFIED
    # ---
    # Create toc.txt
    # save_toc_to_txt()
    # # Convert toc.txt to toc.csv
    # toc_txt_to_csv()
    # ---

    # Call this if either toc.txt or toc.csv is modified
    # init_new_toc()

    # Call this to parse the content_list_json into separate chapter files
    parse_content_list_json()
