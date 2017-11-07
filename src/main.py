import tesserocr
from PIL import Image

from preprocess import read_image, preprocess, save_image

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

print("Raw Image Output")
image = Image.open('images/input/wegmans_20170912.png')
print(tesserocr.image_to_text(image))  # print ocr text from image

print("Processed Image Output")
image = read_image('images/output/wegmans_20170912.png')
processed_image = preprocess(image)
save_image(processed_image, 'images/output/wegmans_20170912.png')
processed_image = Image.open('images/output/wegmans_20170912.png')
print(tesserocr.image_to_text(processed_image))  # print ocr text from image
