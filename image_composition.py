"""
Composite cutout image on a new background, which generates a new original image.
"""

import os
from PIL import Image
from tqdm import tqdm

cutout_folder_path = 'cutout'
cutout_image_list = os.listdir(cutout_folder_path)
cutout_size = len(cutout_image_list)

background_folder_path = 'new_background'
background_image_list = os.listdir(background_folder_path)
background_size = len(background_image_list)

generated_path = 'generated'

for i, background_img_name in enumerate(tqdm(background_image_list, desc = "Background")):
    background_image_path = background_folder_path  + '/' + background_img_name

    for j, cutout_img_name in enumerate(tqdm(cutout_image_list, desc = "Cutout")):
        cutout_image_path = cutout_folder_path + '/' + cutout_img_name
        
        cutout = Image.open(cutout_image_path)
        new_background = Image.open(background_image_path).resize(cutout.size)
        
        # Alpha channel of cutout image, working as a mask in this code
        alpha = cutout.split()[-1]

        generated_image = Image.composite(cutout, new_background, alpha)

        output_path = generated_path + '/' + cutout_img_name.split('.')[0] + '_' + 'newbackground_' + str(i) + '.jpg'

        generated_image.save(output_path)

        print(f"Cutout image {j + 1} is composited with background {i + 1}.")

print("Mission Accomplished")