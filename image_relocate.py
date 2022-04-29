import shutil
import os
from tqdm import tqdm

image_list = os.listdir('cutout_3')

for i, img_name in enumerate(tqdm(image_list)):
    shutil.move('origin_2/' + img_name.split('.')[0] + '.jpg', 
                'origin_3/' + img_name.split('.')[0] + '.jpg')

print("Mission Accomplished")