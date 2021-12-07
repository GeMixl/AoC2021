###############################################################
# Advent of Code 2021                                         #
# Day 6 https://adventofcode.com/2021/day/6                   #
# Puzzle input at https://adventofcode.com/2021/day/6/input   #
###############################################################

with open("input_day06.txt", "r") as fs:
    swarm = [int(i) for i in fs.readline().split(",")]

my_generation = [0] * 9

for i in swarm:
    my_generation[i] += 1

print(swarm)
print(my_generation)


def grow(generation):
    new_generation = [0]*9
    new_generation[6] = generation[0]
    new_generation[1] = generation[2]
    new_generation[2] = generation[3]
    new_generation[3] = generation[4]
    new_generation[4] = generation[5]
    new_generation[5] = generation[6]
    new_generation[6] += generation[7]
    new_generation[7] = generation[8]
    new_generation[8] = generation[0]
    new_generation[0] = generation[1]
    return new_generation


for i in range(256):
    my_generation = grow(my_generation)
    print(my_generation, sum(my_generation))
