###############################################################
# Advent of Code 2021                                         #
# Day 1 https://adventofcode.com/2021/day/1                   #
# Puzzle input at https://adventofcode.com/2021/day/1/input   #
###############################################################
with open("input_day01.txt", "r") as fs:
    data = [int(x) for x in fs]
averaged_data = [i + j + k for (i, j, k) in zip(data[:-2], data[1:-1], data[2:])]
print("First Puzzle:")
print(sum([1 for (i, j) in zip(data[:-1], data[1:]) if i < j]))
print("")
print("Second Puzzle:")
print(sum([1 for (i, j) in zip(averaged_data[:-1], averaged_data[1:]) if i < j]))

