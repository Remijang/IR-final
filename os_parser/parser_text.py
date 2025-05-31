import os
import re
import markdown
from bs4 import BeautifulSoup

def remove_latex_math(text):
  text = re.sub(r'(?<!\\)\$.*?(?<!\\)\$', '', text)
  text = re.sub(r'\\\(.*?\)', '', text, flags=re.DOTALL)
  text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
  text = re.sub(r'\\\[.*?\\\]', '', text, flags=re.DOTALL)
  math_environments = [
      'equation', 'align', 'eqnarray', 'gathered', 'multline', 'cases', 'array',
      'pmatrix', 'bmatrix', 'vmatrix', 'Vmatrix', 'Bmatrix', 'smallmatrix', 'matrix',
      'split', 'subequations', 'flalign', 'alignat'
  ]
  for env in math_environments:
      pattern = r'\\begin{' + re.escape(env) + r'}.*?\\end{' + re.escape(env) + r'}'
      text = re.sub(pattern, '', text, flags=re.DOTALL)

  return text

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

def process_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "content.md" in filenames:
            markdown_md_path = os.path.join(dirpath, "content.md")
            text_md_path = os.path.join(dirpath, "content.txt")

            with open(markdown_md_path, 'r', encoding='utf-8') as f_in:
                markdown_content = f_in.read()

            cleaned_content = md_to_text(markdown_content)

            # cleaned_content = remove_latex_math(cleaned_content)

            with open(text_md_path, 'w', encoding='utf-8') as f_out:
                f_out.write(cleaned_content)

if __name__ == "__main__":
    root_directory_to_scan = 'os_clean'
    process_directories(root_directory_to_scan)
