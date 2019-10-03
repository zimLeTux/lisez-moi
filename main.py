from PIL import Image
import pytesseract
import pdf2image

def read_pdf(pdf_path):
    images = pdf2image.convert_from_path(pdf_path)
    for image in images:
        yield image


for test in read_pdf("test/test.pdf"):
    print(pytesseract.image_to_string(test, lang='fra'))
