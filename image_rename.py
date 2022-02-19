"""
Rename a series of image files in a specific folder.
This codework is adpated from 
https://www.geeksforgeeks.org/rename-multiple-files-using-python/
"""

import os
from tqdm import tqdm

header = "Product_AlarmClock"
image_extension = ".jpg"    # [".jpg", ".jpeg", ".png"]

folder = "origin"   # ["origin", "cutout", "generated"]
image_list = os.listdir(folder)
size = len(image_list)

for i, img_name in enumerate(tqdm(image_list)):
    src = f"{folder}/{img_name}"

    new_img_name = header + "_" + img_name
    dst = f"{folder}/{new_img_name}"

    os.rename(src, dst)

print("Mission Accomplished")