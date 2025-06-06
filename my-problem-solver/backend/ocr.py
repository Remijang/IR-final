import os

from magic_pdf.data.data_reader_writer import FileBasedDataWriter
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
from magic_pdf.data.read_api import read_local_images

def image_to_text(image_path):

    local_image_dir, local_md_dir = "mineru-output/images", "mineru-output"
    image_dir = str(os.path.basename(local_image_dir))

    os.makedirs(local_image_dir, exist_ok=True)

    image_writer, md_writer = FileBasedDataWriter(local_image_dir), FileBasedDataWriter(
        local_md_dir
    )

    # input_file = "image_9-3.png"

    ds = read_local_images(image_path)[0]

    result = ds.apply(doc_analyze, ocr=True, formula_enable=False, table_enable=False).pipe_ocr_mode(image_writer).get_markdown(image_dir)
    
    # remove all image tags with the image path in the markdown
    start = result.find("![")
    while start != -1:
        end = result.find(")", start)
        if end == -1:
            break
        result = result[:start] + result[end + 1:]
        start = result.find("![")

    os.system(f"rm -rf {local_md_dir}")

    # print(result, type(result))
    return result

if __name__ == "__main__":
    result = image_to_text("image_9-3.png")