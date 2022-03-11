###############################################################
# Advent of Code 2021                                         #
# Day 17 https://adventofcode.com/2021/day/17                 #
# Puzzle input at https://adventofcode.com/2021/day/17/input  #
###############################################################
from parse import *
import numpy as np
from collections import namedtuple

with open("input_day17.txt", "r") as fs:
    data = parse("target area: x={x0:d}..{x1:d}, y={y0:d}..{y1:d}", fs.readline())

# print(calcTrajectory1(18, 147, 303))

trajectory = namedtuple("trajectory", ["reach", "v_init", "n_step"])

resX, resY = [], []
# i ranges over all possible x and y target coordinates
for i in {*range(data['x0'], data['x1'] + 1), *range(-data['y1'], -data['y0'] + 1)}:
    # k counts from 1 (minimum # of steps) up and helps to get the incrementing/decrementing step size
    for k in range(1, i + 1):
        # r is set to the current reach this can be below the target behind the target or exactly at the target
        # l is the length of the next step
        r, l = 0, k
        while r < i:
            r += l
            if r == i:
                resX.append(trajectory(i, l, l - k + 1))
                resY.append(trajectory(i, k, l - k + 1))
                resY.append(trajectory(i, -(k - 1), l + k))
            l += 1

counter = set()
for n in range(data['x0'], data['x1'] + 1):
    x_traj = [i for i in filter(lambda x: x.reach == n, resX)]
    for m in x_traj:
        for y_reach in range(-data['y1'], -data['y0'] + 1):
            smp = [(m.v_init, j.v_init) for j in filter(lambda x: (x.reach == y_reach) & (x.n_step == m.n_step), resY)]
            if smp:
                counter = counter.union(smp)
            if m.n_step == m.v_init:
                smp = [(m.v_init, j.v_init) for j in filter(lambda x: (x.reach == y_reach) & (x.n_step > m.n_step), resY)]
                counter = counter.union(smp)

print("Puzzle 1:")
v_y_min = min([j for (i, j) in counter])
print(-v_y_min * (-v_y_min + 1) // 2)

print("Puzzle 2:")
print(len(counter))
