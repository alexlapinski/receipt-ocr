from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
import skimage.filters as filters
import skimage.transform as transform
import skimage.io as io
import matplotlib
import matplotlib.pyplot as plt
import skimage.restoration as restoration
import skimage.color as color
import skimage.exposure as exposure
import skimage.util as skutil
from toolz.functoolz import compose, pipe
from functools import partial

io.use_plugin('pil')

# preprocess_library = 'Pillow'
preprocess_library = 'skimage'


def main():
    input_dir_path = join("images", "input")
    output_dir_path = join("images", "output")

    for file in listdir(input_dir_path):
        input_file_path = join(input_dir_path, file)
        if isfile(input_file_path) and file.endswith(".png"):
            print("Processing {file}".format(file=file))
            output_file_path = join(output_dir_path, file)
            image = read_image(input_file_path)
            processed_image = preprocess(image)
            save_image(processed_image, output_file_path)


def save_image(image, image_file_path):
    print('Saving Image')
    if preprocess_library == 'Pillow':
        return image.save(image_file_path)
    elif preprocess_library == 'skimage':
        return io.imsave(image_file_path, image)
    else:
        raise ValueError("Invalid preprocess library: ${library}".format(library=preprocess_library))


def read_image(image_file_path):
    print('Reading Image')
    if preprocess_library == 'Pillow':
        return Image.open(image_file_path)
    elif preprocess_library == 'skimage':
        return io.imread(image_file_path)
    else:
        raise ValueError("Invalid preprocess library: ${library}".format(library=preprocess_library))


def preprocess(image):
    print('Preprocessing Image')
    if preprocess_library == 'Pillow':
        return preprocess_pillow(image)
    elif preprocess_library == 'skimage':
        return preprocess_skimage(image)
    else:
        raise ValueError("Invalid preprocess_library: '${library}'".format(library=preprocess_library))


def preprocess_skimage(image):
    return pipe(image,
                color.rgb2gray,
                #partial(restoration.denoise_bilateral, multichannel=False),
                #exposure.equalize_hist,
                partial(exposure.adjust_gamma, gamma=0.75),
                #lambda img: img > filters.threshold_local(img, block_size=11, method='mean'),
                #lambda img: img > filters.threshold_otsu(img),
                #lambda img: img > filters.threshold_local(img, block_size=7),
                #skutil.img_as_int,
                partial(transform.pyramid_expand, upscale=2)
                )


def preprocess_pillow(image):
    upscale_factor = 2
    large_img = image.resize((image.size[0] * upscale_factor, image.size[1] * upscale_factor))
    greyscale_img = large_img.convert('L')
    return greyscale_img


if __name__ == "__main__":
    main()
