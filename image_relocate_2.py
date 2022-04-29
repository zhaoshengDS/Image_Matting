"""
Relocate large amount of image files from one directory to another
"""

import os
import shutil
import winsound

duration = 2000  # milliseconds
freq = 440  # Hz

source_directory = r"E:\raw_data\Matting Human Datasets\matting"
destination_directory = r"E:\image_matting_dataset\portrait\target"

for root, subdirectories, files in os.walk(source_directory):
    for file in files:
        try:
            shutil.move(os.path.join(root, file), 
                        os.path.join(destination_directory, file))
        
        except Exception as e:
            print("Type of error: " + str(e))
            print(os.path.join(root, file))

print("Mission Accomplished")
winsound.Beep(freq, duration)