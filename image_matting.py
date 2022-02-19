"""
Remove background and save foreground from an image.
The output image is expected to have '.png' as extension in order to maintain transparent background 
"""

# rembg.bg is adapted from https://github.com/danielgatis/rembg
from rembg.bg import remove
import numpy as np
import io
import os
from PIL import Image, ImageFile
from tqdm import tqdm

origin_path = 'origin'
image_list = os.listdir(origin_path)
size = len(image_list)

cutout_path = 'cutout'

# Set True if working with trucated image formats (ex. JPEG / JPG)
ImageFile.LOAD_TRUNCATED_IMAGES = True

for i, img_name in enumerate(tqdm(image_list)):
    input_path = origin_path + '/' + img_name
    output_path  = cutout_path + '/' + img_name.split('.')[0] + '.png'

    f = np.fromfile(input_path)
    result = remove(f)

    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)

print("Mission Accomplished")