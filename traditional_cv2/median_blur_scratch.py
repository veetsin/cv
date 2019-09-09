import cv2
import numpy as np
import math

img_path = '/Users/mc/Documents/python/cv/traditional_cv/xxm.jpeg'
img = cv2.imread(img_path, 0)
# cv2.imwrite('/Users/mc/Documents/python/cv/traditional_cv/gray.jpg',img)        


# cv2.imshow('xxm', img)
# key = cv2.waitKey(0)
# cv2.destroyAllWindows()

shape = img.shape
kernel_size = 11
padding_size = math.ceil((kernel_size - 1) / 2)

def padding_replica(img, padding_size):
    padding_matrix_vert_ceil = np.array([img[:][0] for _ in range(padding_size)])
    padding_matrix_vert_floor = np.array([img[:][-1] for _ in range(padding_size)])
    img = np.concatenate((img, padding_matrix_vert_floor))
    img = np.concatenate((padding_matrix_vert_ceil, img))
    
    padding_matrix_hori = np.zeros((img.shape[0], padding_size))
    padding_matrix_hori_left = np.array([img.T[:][0] for _ in range(padding_size)]).T
    padding_matrix_hori_right = np.array([img.T[:][-1] for _ in range(padding_size)]).T

    img = np.concatenate((img, padding_matrix_hori_right), axis = 1)
    img = np.concatenate((padding_matrix_hori_left, img), axis = 1)
    return img 

def padding_zero(img, padding_size):
    padding_matrix_vert = np.zeros((padding_size, img.shape[1]))
    img = np.concatenate((img, padding_matrix_vert))
    img = np.concatenate((padding_matrix_vert, img))
    padding_matrix_hori = np.zeros((img.shape[0], padding_size))
    img = np.concatenate((img, padding_matrix_hori), axis = 1)
    img = np.concatenate((padding_matrix_hori, img), axis = 1)
    return img


def get_pixel_value(matrix):
    matrix = matrix.flatten()
    index = math.ceil(len(matrix)/2)
    return np.sort(matrix)[index]


def median_blur(img, padding_size, kernel_size, **kw):
    shape_ori = img.shape
    if 'padding_way' in kw:
        way = kw['padding_way']
    else:
        way = None
    if way == 'zero':
        img = padding_zero(img, padding_size)  
    elif way == 'replica':
        img = padding_replica(img, padding_size)  
    shape = img.shape
    pixel_list = []
    col_bound = shape[1] - kernel_size + 1
    rang = (shape[0] - kernel_size + 1) * (shape[1] - kernel_size + 1)
    for i in range( rang ):
        times = i + 1
        row_index = i // col_bound
        col_index = i % col_bound
        cov_matrix = np.array( [ img[j][col_index:col_index+kernel_size] for j in range(row_index, row_index+kernel_size) ] )
        pixel_list.append(get_pixel_value(cov_matrix))
    return np.array(pixel_list).reshape(shape_ori)

if __name__ == "__main__":
    blured_img = median_blur(img, padding_size, kernel_size, **{'padding_way':'replica'})
    cv2.imwrite('/Users/mc/Documents/python/cv/traditional_cv2/blured_xxm_replica_kernel11.jpg',blured_img)        
    

# t = np.array([ [1,2,3,4],[2,3,4,5],[3,4,5,6] ])
# pd = padding_zero(t,1)

