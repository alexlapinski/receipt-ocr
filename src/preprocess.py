from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

def main():
    input_dir_path = join("images","input")
    output_dir_path = join("images", "output")

    for file in listdir(input_dir_path):
        input_file_path = join(input_dir_path, file)
        if isfile(input_file_path) and file.endswith(".png"):
            output_file_path = join(output_dir_path, file)
            image = Image.open(input_file_path)
            processed_image = preprocess(image)
            # processed_image.show()
            processed_image.save(output_file_path)


def preprocess(image):
    upscale_factor = 2
    large_img = image.resize((image.size[0] * upscale_factor, image.size[1] * upscale_factor))
    greyscale_img = large_img.convert('L')
    normalized_img = ImageOps.autocontrast(greyscale_img, 0.75)
    #blurred_img = normalized_img.filter(ImageFilter.GaussianBlur)
    singlebit_img = normalized_img.point(lambda x: 0 if x < 100 else 255, '1')
    return singlebit_img
    sharpened_img = singlebit_img.filter(ImageFilter.EDGE_ENHANCE)

    return sharpened_img


if __name__ == "__main__":
    main()