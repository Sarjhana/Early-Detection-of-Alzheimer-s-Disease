import numpy as np
from PIL import Image

import pydicom as dicom
from skimage.transform import resize
import scipy.misc

import os

# List all files in a directory using os.listdir

mri_basepath = r'/Users/sarjhana/Desktop/Final Year Project/Data/AD_Final/AD_axial/'

for mri_entry in os.listdir(mri_basepath):
        #print(mri_entry)
        mri_img1=dicom.read_file(os.path.join(mri_basepath,mri_entry))
        mri_img=mri_img1.pixel_array

        IMG_PX_SIZE = 256 
        mri_img = resize(mri_img, (IMG_PX_SIZE, IMG_PX_SIZE), anti_aliasing=True)
        ### print(mri_img.shape)

        rgb = Image.fromarray(mri_img)
        rgb.save("Data/AD_tiff/axial/" + mri_entry + ".tiff")
