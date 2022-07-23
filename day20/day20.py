###############################################################
# Advent of Code 2021                                         #
# Day 20 https://adventofcode.com/2021/day/18                 #
# Puzzle input at https://adventofcode.com/2021/day/20/input  #
###############################################################

import numpy as np

N = 2

with open("input_day20.txt", "r") as fs:
    filter, image = fs.read().split("\n\n")

filter = filter.replace('\n', '')
filter = filter.replace('.', '0')
filter = filter.replace('#', '1')
image = image.replace('.', '0')
image = image.replace('#', '1')
image = np.array([[entry for entry in line] for line in image.split('\n')])

def filter_N_times(img, ftr, N, padding = '0'):
    for n in range(N):
        img = np.pad(img, pad_width=2, mode='constant', constant_values=padding)
        img_ = np.full_like(img, padding)
        for i in range(1, img.shape[0]-1):
            for j in range(1, img.shape[1]-1):
                part = img[i - 1:i + 2, j - 1:j + 2]
                part = part.reshape(9)
                s = int("".join(part), 2)
                img_[i,j] = ftr[s]
        if ftr[0] == '1':
            padding = '1' if ftr[-1] == '1' or n%2==0 else '0'
        img = img_[1:-1,1:-1]
    return img


filtered = filter_N_times(image, filter, 2)
print(np.count_nonzero(filtered == '1'))

filtered = filter_N_times(image, filter, 50)
print(np.count_nonzero(filtered == '1'))

