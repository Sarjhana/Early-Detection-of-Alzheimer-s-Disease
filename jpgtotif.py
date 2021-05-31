from PIL import Image
import os

folderpath = '/Users/sarjhana/Desktop/Final Year Project/Data/set3/AD'

count = 0

for entry in os.listdir(folderpath):
    im = Image.open(os.path.join(folderpath,entry))
    count += 1
    im.save('/Users/sarjhana/Desktop/Final Year Project/Data/set3/sagittal_train/AD/'+ str(count) + '.tif')