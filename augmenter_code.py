import random
from scipy import ndarray
import skimage as sk
from skimage import io
from skimage import transform
from skimage import util
import cv2
from PIL import Image

def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)

def horizontal_flip(imageObject):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return imageObject.transpose(Image.FLIP_LEFT_RIGHT)

# dictionary of the transformations functions we defined earlier
available_transformations = {
    'rotate': random_rotation,
    'horizontal_flip': horizontal_flip
}


import random
import os

# our folder path containing some images
folder_path = '/Users/sarjhana/Desktop/Final Year Project/Data/NC_tiff/axial/'
# the number of file to generate
num_files_desired = 1350

# loop on all files of the folder and build a list of files paths
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

num_generated_files = 1
while num_generated_files <= num_files_desired:
    # random image from the folder
    image_path = random.choice(images)
    # read image as an two dimensional array of pixels
    imageObject = Image.open(folder_path)

    # random num of transformations to apply
    num_transformations_to_apply = 2
    num_transformations = 1
    transformed_image = None
    while num_transformations <= num_transformations_to_apply:
        # choose a random transformation to apply for a single image
        key = random.choice(list(available_transformations))
        transformed_image = available_transformations[key](imageObject)

        # define a name for our new file
        new_file_path = '/Users/sarjhana/Desktop/Final Year Project/Data/%s_%s.tif' % (num_generated_files, num_transformations)

        # write image to the disk
        transformed_image.save(new_file_path)

        num_transformations += 1

    num_generated_files += 1
