"""
The trimap in Oxford IIIT Pet Dataset only contains pixel values of {1,2,3}, and has the following correspondence:

Class 1: Pixels belonging to the pet. 

Class 2: Pixels belonging to the background.

Class 3: Pixels belonging to the outline of the pet.

This codework converts the raw trimap to grayscale image so that the trimap can be used in machine leanring model training.
"""

import numpy
from PIL import Image 
from tqdm import tqdm
import os
import shutil

original_image_path = "./images/"
original_trimap_path = "./annotations/trimaps/"

destination_image_path = "./img/"
destination_trimap_path = "./gt/"

for _, image_name in enumerate(tqdm(os.listdir(original_trimap_path))):

    im_trimap = Image.open(original_trimap_path + image_name)

    pix = numpy.array(im_trimap)

    pix[pix == 3] = 128
    pix[pix == 2] = 0
    pix[pix == 1] = 255

    trimap_to_be_saved = Image.fromarray(pix)
    
    trimap_to_be_saved.save(destination_trimap_path + image_name)

    shutil.move(original_image_path + image_name.split('.')[0] + '.jpg', 
                destination_image_path + image_name.split('.')[0] + '.jpg')