###############################################################
# Advent of Code 2021                                         #
# Day 21 https://adventofcode.com/2021/day/5                  #
# Puzzle input at https://adventofcode.com/2021/day/5/input   #
###############################################################

import numpy as np
from parse import *
import pytest


def test_simple_line_ho():
    tst = (simple_line(0, 0, 0, 5))
    ref = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
    assert len(tst) == len(ref)
    assert [(i1 == i2) & (j1 == j2) for ((i1, j1), (i2, j2)) in zip(tst, ref)]


def test_simple_line_ve():
    tst = (simple_line(0, 0, 5, 0))
    ref = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
    assert len(tst) == len(ref)
    assert [(i1 == i2) & (j1 == j2) for ((i1, j1), (i2, j2)) in zip(tst, ref)]


def test_simple_line_q1():
    tst = (simple_line(0, 0, 5, 5))
    ref = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    assert len(tst) == len(ref)
    assert [(i1 == i2) & (j1 == j2) for ((i1, j1), (i2, j2)) in zip(tst, ref)]


def test_simple_line_q3():
    tst = (simple_line(5, 5, 0, 0))
    ref = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    assert len(tst) == len(ref)
    assert [(i1 == i2) & (j1 == j2) for ((i1, j1), (i2, j2)) in zip(tst, ref)]


def test_simple_line_q2():
    tst = (simple_line(0, 5, 5, 0))
    ref = [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
    assert len(tst) == len(ref)
    assert [(i1 == i2) & (j1 == j2) for ((i1, j1), (i2, j2)) in zip(tst, ref)]


def test_simple_line_q4():
    tst = (simple_line(5, 0, 0, 5))
    ref = [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)]
    assert len(tst) == len(ref)
    assert [(i1 == i2) & (j1 == j2) for ((i1, j1), (i2, j2)) in zip(tst, ref)]


def simple_line(x1, y1, x2, y2):
    dx = x2 - x1
    if dx == 0:
        (y1, y2) = (y1, y2) if y1 < y2 else (y2, y1)
        return [(x1, j) for j in range(y1, y2+1)]
    dy = y2 - y1
    if dy == 0:
        (x1, x2) = (x1, x2) if x1 < x2 else (x2, x1)
        return [(i, y1) for i in range(x1, x2+1)]
    if dy == dx:
        (x1, x2) = (x1, x2) if x1 < x2 else (x2, x1)
        (y1, y2) = (y1, y2) if y1 < y2 else (y2, y1)
        return [(i, j) for (i, j) in zip(range(x1, x2+1, 1), range(y1, y2+1, 1))]
    if dy == -dx:
        (x1, x2) = (x1, x2) if x1 > x2 else (x2, x1)
        (y1, y2) = (y1, y2) if y1 < y2 else (y2, y1)
        return [(i, j) for (i, j) in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1, 1))]


with open("input_day05.txt", "r") as fs:
    input_data = [parse("{x1},{y1} -> {x2},{y2}", i.strip('\n')) for i in fs]

data = np.array([[int(i['x1']), int(i['y1']), int(i['x2']), int(i['y2'])] for i in input_data])
grid = np.zeros((max([max(data[:, 1]), max(data[:, 3])]) + 1,
                 max([max(data[:, 0]), max(data[:, 2])]) + 1))

for i in data:
    if (i[0] == i[2]) | (i[1] == i[3]):
        for (k, l) in simple_line(i[0], i[1], i[2], i[3]):
            grid[l, k] += 1
print("Puzzle 1:")
print(len(grid[grid > 1]))

for i in data:
    if abs(i[2] - i[0]) == abs(i[3] - i[1]):
        for (k, l) in simple_line(i[0], i[1], i[2], i[3]):
            grid[l, k] += 1
print("Puzzle 2:")
print(len(grid[grid > 1]))




