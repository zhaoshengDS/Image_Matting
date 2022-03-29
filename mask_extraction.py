"""
Extracting alpha mask from the matted image in .png format
"""

from tqdm import tqdm
import cv2
import os

dataset = "./portrait/"
source_folder = "target/"
destination_folder = "matte/"

image_list = os.listdir(dataset + source_folder)

for i, img_name in enumerate(tqdm(image_list)):
    image = cv2.imread(dataset + source_folder + img_name, cv2.IMREAD_UNCHANGED)  
    alpha_matte = image[:,:,3]
    cv2.imwrite(dataset + destination_folder + img_name, alpha_matte)

print("Mission Accomplished")