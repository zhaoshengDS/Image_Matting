"""
p: Portrait     s: Commodity        c: Cartoon      a: Animal
d: Delete

Categorize data into the four designated categories (i.e. Portrait, Commodity, Cartoon, Animal):
If the data does not meet the project requirement, simply press 'd' to delete it.
"""

import cv2
import shutil
import os

src_feature_path = "E:\image_matting\origin_with_trimap"
src_target_path = "E:\image_matting\cutout"

for img_name in os.listdir(src_feature_path):
    img_path = src_feature_path + '/' + img_name
    cv2.namedWindow(img_name)
    cv2.moveWindow(img_name, 800, 600)
    cv2.imshow(img_name,
               cv2.imread(img_path)
               )
    
    k = chr(cv2.waitKey(0))

    if k == "p":
        dst_feature_path = r"E:\image_matting_dataset\portrait\feature"
        dst_target_path = r"E:\image_matting_dataset\portrait\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(src_target_path + '/' + img_name.split('.')[0] + '.png', 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "s":
        dst_feature_path = r"E:\image_matting_dataset\commodity\feature"
        dst_target_path = r"E:\image_matting_dataset\commodity\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(src_target_path + '/' + img_name.split('.')[0] + '.png', 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "c":
        dst_feature_path = r"E:\image_matting_dataset\cartoon\feature"
        dst_target_path = r"E:\image_matting_dataset\cartoon\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(src_target_path + '/' + img_name.split('.')[0] + '.png', 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "a":
        dst_feature_path = r"E:\image_matting_dataset\animal\feature"
        dst_target_path = r"E:\image_matting_dataset\animal\target"
        shutil.move(img_path, 
                    dst_feature_path + '/' + img_name)
        shutil.move(src_target_path + '/' + img_name.split('.')[0] + '.png', 
                    dst_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
    
    elif k == "d":
        os.remove(img_path)
        os.remove(src_target_path + '/' + img_name.split('.')[0] + '.png')
        cv2.destroyAllWindows()
        print(f"{img_name} and its cutout image have been removed successfully")

    else:
        break

print("Mission Accomplished")