###############################################################
# Advent of Code 2021                                         #
# Day 2 https://adventofcode.com/2021/day/2                   #
# Puzzle input at https://adventofcode.com/2021/day/2/input   #
###############################################################
with open("input_day02.txt", "r") as fs:
    data = [(i.split(sep=" ")[0], int(i.split(sep=" ")[1])) for i in fs]

propulsion = [j for [i, j] in data if i == "forward"]
dive = [j if i == 'down' else -j for [i, j] in data if i != "forward"]
print("First Puzzle:")
print(sum(propulsion)*sum(dive))
print("")
dive = 0
aim = 0
for i, val in enumerate(data):
    if val[0] == 'forward':
        dive += val[1]*aim
    if val[0] == 'up':
        aim -= val[1]
    if val[0] == 'down':
        aim += val[1]
print("Second Puzzle:")
print(dive * sum(propulsion))