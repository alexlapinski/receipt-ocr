import tesserocr
from PIL import Image

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

print("Raw Image Output")
image = Image.open('images/input/wegmans_20170912.jpg')
print(tesserocr.image_to_text(image))  # print ocr text from image

print("Processed Image Output")
image = Image.open('images/output/wegmans_20170912.jpg')
print(tesserocr.image_to_text(image))  # print ocr text from image
