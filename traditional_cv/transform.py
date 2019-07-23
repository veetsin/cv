import cv2
import random
import numpy as np
from matplotlib import pyplot as plt
from math import floor as fl

#random crop
def get_crop(img, path):
    factor_ceil = random.uniform(0.4, 1)
    factor_floor = random.uniform(0, 0.4)
    l1, l2 = img.shape[0], img.shape[1]
    img_crop = img[fl(l1 * factor_floor) : fl(l2 * factor_ceil), fl(l1 * factor_floor) : fl(l2 * factor_ceil)]
    cv2.imwrite(path, img_crop)


# change color
def get_color_shift(img, path):
    # brightness
    B, G, R = cv2.split(img)

    b_rand = random.randint(-75, 75)
    if b_rand == 0:
        pass
    elif b_rand > 0:
        lim = 255 - b_rand
        B[B > lim] = 255
        B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)
    elif b_rand < 0:
        lim = 0 - b_rand
        B[B < lim] = 0
        B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)

    g_rand = random.randint(-75, 75)
    if g_rand == 0:
        pass
    elif g_rand > 0:
        lim = 255 - g_rand
        G[G > lim] = 255
        G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)
    elif g_rand < 0:
        lim = 0 - g_rand
        G[G < lim] = 0
        G[G >= lim] = (g_rand + G[G >= lim]).astype(img.dtype)

    r_rand = random.randint(-75, 75)
    if r_rand == 0:
        pass
    elif r_rand > 0:
        lim = 255 - r_rand
        R[R > lim] = 255
        R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)
    elif r_rand < 0:
        lim = 0 - r_rand
        R[R < lim] = 0
        R[R >= lim] = (r_rand + R[R >= lim]).astype(img.dtype)

    img_merge = cv2.merge((B, G, R))
    #img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite(path, img_merge)

#similarity transform
def get_rotation(img, path):
    center = (img.shape[0] / random.randint(1, 5), img.shape[1] / random.randint(1, 5))
    angle = random.randint(0, 360)
    scale = random.uniform(0.5, 1.5)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    img_rotation = cv2.warpAffine(img, M, (img.shape[0], img.shape[1]))
    cv2.imwrite(path, img_rotation)


#perspective transform
def get_perspective(img, path):
    height, width, channels = img.shape

    # warp:
    random_margin = random.randint(60, 200)
    x1 = random.randint(-random_margin, random_margin)
    y1 = random.randint(-random_margin, random_margin)
    x2 = random.randint(width - random_margin - 1, width - 1)
    y2 = random.randint(-random_margin, random_margin)
    x3 = random.randint(width - random_margin - 1, width - 1)
    y3 = random.randint(height - random_margin - 1, height - 1)
    x4 = random.randint(-random_margin, random_margin)
    y4 = random.randint(height - random_margin - 1, height - 1)

    dx1 = random.randint(-random_margin, random_margin)
    dy1 = random.randint(-random_margin, random_margin)
    dx2 = random.randint(width - random_margin - 1, width - 1)
    dy2 = random.randint(-random_margin, random_margin)
    dx3 = random.randint(width - random_margin - 1, width - 1)
    dy3 = random.randint(height - random_margin - 1, height - 1)
    dx4 = random.randint(-random_margin, random_margin)
    dy4 = random.randint(height - random_margin - 1, height - 1)

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
    M_warp = cv2.getPerspectiveTransform(pts1, pts2)
    img_warp = cv2.warpPerspective(img, M_warp, (width, height))
    cv2.imwrite(path, img_warp)


    

