"""
Since the Oxford IIIT Pet Dataset contains some empty trimap (i.e., all the pixels on the trimap have a value of 0),
and those images may not be used to train machine learning models,
those images should be removed.

This codework just removes all the empty trimaps and the corresponding original images.
"""

import numpy
from PIL import Image 
from tqdm import tqdm
import os

original_image_path = "./img/"
original_trimap_path = "./gt/"

for _, image_name in enumerate(tqdm(os.listdir(original_trimap_path))):

    im_trimap = Image.open(original_trimap_path + image_name)

    pix = numpy.array(im_trimap)

    if numpy.sum(pix) == 0:
        # Remove empty trimap and its corresponding original image
        os.remove(original_trimap_path + image_name)
        os.remove(original_image_path + image_name.split('.')[0] + '.jpg')