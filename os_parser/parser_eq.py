import os
import json

def process_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "content.json" in filenames:
            content_json_path = os.path.join(dirpath, "content.json")
            text_eq_path = os.path.join(dirpath, "equation.json")

            with open(content_json_path, 'r', encoding='utf-8') as f_in:
                 data = json.load(f_in)

            split_result = []

            for entry in data:
                if entry["type"] == "equation":
                    split_result.append(entry)

            json_str = json.dumps(split_result, indent=4)

            with open (text_eq_path, 'w') as f:
                f.write(json_str)
            

if __name__ == "__main__":
    root_directory_to_scan = '.'
    process_directories(root_directory_to_scan)
