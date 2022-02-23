"""
p: Portrait     s: Commodity        c: Cartoon      a: Animal
d: Delete

Categorize data into the four designated categories (i.e. Portrait, Commodity, Cartoon, Animal):
If the data does not meet the project requirement, simply press 'd' to delete it.
"""

import cv2
import shutil
import os
import numpy as np

src_feature_path = "E:\image_matting\origin"
src_target_path = "E:\image_matting\cutout"

img_list = os.listdir(src_feature_path)
size = len(img_list)

for i, img_name in enumerate(img_list):
    img_path = src_feature_path + '/' + img_name
    matted_img_path = src_target_path + '/' + img_name.split('.')[0] + '.png'
    window_name = img_name + ' (' + str(i + 1) + ' / ' + str(size) + ')'
    
    # Display original and matted images
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, 800, 600)
    cv2.resizeWindow(window_name, 1580, 1320)
    cv2.imshow(window_name,
               np.concatenate((cv2.imread(img_path),
                               cv2.imread(matted_img_path)),
                               axis = 1)
               )
    
    k = chr(cv2.waitKey(0))

    if k == "p":
        dst_feature_path = r"E:\image_matting_dataset\portrait\feature"
        dst_target_path = r"E:\image_matting_dataset\portrait\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(matted_img_path, 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "s":
        dst_feature_path = r"E:\image_matting_dataset\commodity\feature"
        dst_target_path = r"E:\image_matting_dataset\commodity\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(matted_img_path, 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "c":
        dst_feature_path = r"E:\image_matting_dataset\cartoon\feature"
        dst_target_path = r"E:\image_matting_dataset\cartoon\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(matted_img_path, 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "a":
        dst_feature_path = r"E:\image_matting_dataset\animal\feature"
        dst_target_path = r"E:\image_matting_dataset\animal\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(matted_img_path, 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "d":
        os.remove(img_path)
        os.remove(matted_img_path)
        cv2.destroyAllWindows()
        print(f"{img_name} and its cutout image have been removed successfully")

    else:
        break

print("Mission Accomplished")