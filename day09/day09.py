###############################################################
# Advent of Code 2021                                         #
# Day 7 https://adventofcode.com/2021/day/7                   #
# Puzzle puzzle_input at https://adventofcode.com/2021/day/7/input   #
###############################################################
# https://github.com/plan-x64/advent-of-code-2021/blob/main/advent/day09.py

import numpy as np


def getBasin(x, y, N, L, arr):
    r = 1
    arr[x, y] = N
    if arr[x, y + 1] < L:
        r += getBasin(x, y + 1, N, L, arr)
    if arr[x + 1, y] < L:
        r += getBasin(x + 1, y, N, L, arr)
    if arr[x, y - 1] < L:
        r += getBasin(x, y - 1, N, L, arr)
    if arr[x - 1, y] < L:
        r += getBasin(x - 1, y, N, L, arr)
    return r


with open("input_day09.txt", "r") as fs:
    puzzle_input = [[int(j) for j in i.strip('\n')] for i in fs]

l = len(puzzle_input[0])
h = len(puzzle_input)

data = np.array([[9 if (i == 0) | (i == l+1) | (j == 0) | (j == h+1) else puzzle_input[j - 1][i - 1]
                  for i in range(l + 2)]
                 for j in range(h + 2)])
sinks = []
risk_level = 0
sink_count = 9

grad = np.zeros((data.shape[0]-2, data.shape[1]-2, 4))

grad[:, :, 0] = data[:-2, 1:-1] - data[1:-1, 1:-1]
grad[:, :, 1] = data[1:-1, 2:] - data[1:-1, 1:-1]
grad[:, :, 2] = data[2:, 1:-1] - data[1:-1, 1:-1]
grad[:, :, 3] = data[1:-1, :-2] - data[1:-1, 1:-1]

sinks = (grad[:, :, 0] > 0) & (grad[:, :, 1] > 0) & (grad[:, :, 2] > 0) & (grad[:, :, 3] > 0)

low_points = np.where(sinks)
low_points = list(zip(low_points[0], low_points[1]))
risk_level_1 = sum([data[i[0]+1, i[1]+1]+1 for i in low_points])
risk_level_2 = [getBasin(i[0]+1, i[1]+1, 11, 9, data) for i in low_points]
risk_level_2.sort()

print("First Puzzle:")
print(risk_level_1)
print("")
print("Second Puzzle:")
print(np.prod(risk_level_2[-3:]))


