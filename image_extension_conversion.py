"""
Convert image from .png to .jpg extension, or vice versa.
Delete the image before conversion.
"""

from PIL import Image
from tqdm import tqdm
import os

convert_to = ".jpg"

path = 'origin_with_trimap'
image_list = os.listdir(path)

for i, img_name in enumerate(tqdm(image_list)):
    img = Image.open(path + '/' + img_name)
    img.save(path + '/' + img_name.split('.')[0] + convert_to)
    os.remove(path + '/' + img_name)

print("Mission Accomplished")