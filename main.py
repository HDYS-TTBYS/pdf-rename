from tesserocr import PyTessBaseAPI
import os
import glob
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import sys
import pyocr
import pyocr.builders
import pprint
import shutil


def list_pdfs():
    files = glob.glob("./*.pdf")
    return files


def convert_pdf_to_image(pdf_path: str):
    images = convert_from_path(pdf_path, dpi=400, fmt="jpg")
    images[0].save(os.path.splitext(os.path.basename(pdf_path))[0]+".jpg")
    return images[0]


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)


tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))


pdfs = list_pdfs()
lang = 'eng+jpn'

# H S 座標((200, 350, 300, 450))
# 20230426-0　座標((2500, 355, 2900, 450))

for pdf in pdfs:
    image = convert_pdf_to_image(pdf)

    # id取得
    id = image.crop((200, 350, 300, 450))  # 座標指定
    id_text = tool.image_to_string(
        id,
        lang=lang,
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    print(id_text)

    # 日時取得
    date = image.crop((2500, 355, 2900, 450))  # 座標指定
    date_text = tool.image_to_string(
        date,
        lang=lang,
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    print(date_text)

    # ファイルコピー
    shutil.copyfile(pdf, f"dist/{date_text}-{id_text}.pdf")
