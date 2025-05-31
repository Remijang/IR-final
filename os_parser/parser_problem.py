import os
import re
import markdown
from bs4 import BeautifulSoup
import json

def remove_math_symbols(text):
    import re
    return re.sub(r'\$[^\$]*\$', '', text)  # Remove inline math symbols

def process_directories(root_dir, out_path, out_path_no_math):
    ret = []
    ret_no_math = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "question_raw.json" in filenames:
            question_path = os.path.join(dirpath, "question_raw.json")
            s = dirpath.replace('os-', '').replace('-', '.').split('/')[1:]
            if len(s) == 1:
                s.append("")
            with open(question_path, 'r') as of:
                qq = json.load(of)
            for row in qq:
                txt = row['text']
                txt_no_math = remove_math_symbols(row['text'])
                dic = {
                    "chapter": s[0],
                    "subchapter": s[1],
                    "problem": txt,
                    "page_idx": row['page_idx']
                }
                dic_no_math = {
                    "chapter": s[0],
                    "subchapter": s[1],
                    "problem": txt_no_math,
                    "page_idx": row['page_idx']
                }
                ret.append(dic)
                ret_no_math.append(dic_no_math)

    ret.sort(key=lambda x: (int(x['chapter']), int(x['subchapter'].split('.')[1]) if x['subchapter'] else 0, x['page_idx']))
    ret_no_math.sort(key=lambda x: (int(x['chapter']), int(x['subchapter'].split('.')[1]) if x['subchapter'] else 0, x['page_idx']))

    with open(out_path, 'w') as f:
        json.dump(ret, f, indent=4)
    with open(out_path_no_math, 'w') as f_no_math:
        json.dump(ret_no_math, f_no_math, indent=4)

if __name__ == "__main__":
    root_directory_to_scan = 'os_clean'
    output_path = 'problem.json'
    output_path_no_math = 'problem_no_math.json'
    process_directories(
        root_directory_to_scan, 
        output_path,
        output_path_no_math
        )
