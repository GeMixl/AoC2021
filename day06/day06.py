###############################################################
# Advent of Code 2021                                         #
# Day 6 https://adventofcode.com/2021/day/6                   #
# Puzzle input at https://adventofcode.com/2021/day/6/input   #
###############################################################

class Fish:
    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return str(self.age)

    def grow(self):
        self.age -= 1
        if self.age == -1:
            self.age = 6
            return -1
        else:
            return self.age


with open("input_day06.txt", "r") as fs:
    swarm = [[Fish(int(i)) for i in fs.readline().split(",")]]

print(swarm[0])

for day in range(0, 18):
    swarm.append(swarm[day])
    for fish in swarm[-1]:
        if fish.grow() == -1:
            swarm[-1].append(Fish(9))
    print(swarm[-1])

print(len(swarm[-1]))
