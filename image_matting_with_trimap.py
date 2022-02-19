"""
@ Inputs: Original Image, Trimap
@ Output: Cutout Image
This codework is adpated from https://github.com/pymatting/pymatting
"""

from pymatting import cutout
import os
from tqdm import tqdm

origin_path = 'origin_with_trimap'
image_list = os.listdir(origin_path)
size = len(image_list)

cutout_path = 'cutout'

for i, img_name in enumerate(tqdm(image_list)):
    input_path = origin_path + '/' + img_name
    trimap_path = 'trimap' + '/' + img_name.split('.')[0] + '.png'
    output_path  = cutout_path + '/' + img_name.split('.')[0] + '.png'
    
    cutout(input_path, trimap_path, output_path)

print("Mission Accomplished")