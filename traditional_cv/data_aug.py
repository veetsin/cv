import os
cur_path = os.getcwd()
new_folder = 'augmented_data'
import transform
import sys
import cv2

 

if __name__ == "__main__":
    arg = sys.argv##arg[0]: data_aug.py arg[1]:folder name of data arg[2]:number of repeated times for various transform
    if arg[1] and os.path.exists(new_folder) == 0:
        os.mkdir(new_folder)
    data_path = os.path.join(cur_path, str(arg[1]))
    save_path = os.path.join(cur_path, new_folder)
    for root, dirs, files in os.walk(data_path):
        for file in files:
            img_path = os.path.join(data_path, str(file))
            img = cv2.imread(img_path)
            if arg[2]:
                repetition = arg[2]
            else:
                repetition = 1
            for i in range(int(repetition)):
                transform.get_crop(img, save_path + '/crop_' + str(file) + str(i) + '.jpg')
                transform.get_color_shift(img, save_path + '/color_shift_' + str(file) + str(i) + '.jpg')
                transform.get_rotation(img, save_path + '/rotation_' + str(file) + str(i) + '.jpg')
                transform.get_perspective(img, save_path + '/perspective_' + str(file) + str(i) + '.jpg')