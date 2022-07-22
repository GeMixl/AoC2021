###############################################################
# Advent of Code 2021                                         #
# Day 20 https://adventofcode.com/2021/day/18                 #
# Puzzle input at https://adventofcode.com/2021/day/20/input  #
###############################################################

import numpy as np

N = 2

with open("test_day20.txt", "r") as fs:
    filter, image = fs.read().split("\n\n")

filter = filter.replace('\n', '')
filter = filter.replace('.', '0')
filter = filter.replace('#', '1')
image = image.replace('.', '0')
image = image.replace('#', '1')
image = np.array([[entry for entry in line] for line in image.split('\n')])
image = np.pad(image, pad_width=2, mode='constant', constant_values='0')

def filter_N_times(img, ftr, N, padding = '0'):
    for n in range(N):
        padding = ftr[0] if padding == '0' else ftr[-1]
#       img_ = np.full_like(img, padding)
        img_ = np.pad(img, pad_width=2, mode='constant', constant_values=padding)
#        img = np.pad(img, pad_width=2, mode='constant', constant_values=padding)
        for i in range(1, img.shape[0]-1):
            for j in range(1, img.shape[1]-1):
                part = img[i - 1:i + 2, j - 1:j + 2].reshape(9)
                s = int("".join(part), 2)
                img_[i+n+1,j+n+1] = ftr[s]
        img = img_[1:-2,1:-2]
        print(img[1:-2,1:-2])
    return img


filtered = filter_N_times(image, filter, 2)
print(np.count_nonzero(filtered == '1'))

