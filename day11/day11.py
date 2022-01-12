###############################################################
# Advent of Code 2021                                         #
# Day 11 https://adventofcode.com/2021/day/11                 #
# Puzzle input at https://adventofcode.com/2021/day/11/input  #
###############################################################

import numpy as np
from dataclasses import dataclass


@dataclass
class DumboOctopuses:
    data: np.array = np.array([])
    width: int = 0
    height: int = 0
    flash_count: int = 0
    step_count: int = 0

    def read_test_data(self):
        with open("test_day11.txt", "r") as fs:
            data_input = [[int(i) for i in row if i != "\n"] for row in fs]
        self.data = np.array(data_input)
        self.width, self.height = self.data.shape

    def read_input_data(self):
        with open("input_day11.txt", "r") as fs:
            data_input = [[int(i) for i in row if i != "\n"] for row in fs]
        self.data = np.array(data_input)
        self.width, self.height = self.data.shape

    def next_step(self):
        self.step_count += 1
        self.data += 1
        self.flash_count += self.flash()
        return self.continue_flashing()

    def flash(self):
        flsh_c = 0
        for idx in np.argwhere(self.data > 9):
            for (i, j) in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                if (idx[0]+i >= 0) & (idx[0]+i < self.height) & (idx[1]+j >= 0) & (idx[1]+j < self.width):
                    if self.data[idx[0]+i, idx[1]+j] > 0:
                        self.data[idx[0]+i, idx[1]+j] += 1
            self.data[idx[0], idx[1]] = 0
            flsh_c += 1
        if flsh_c > 0:
            return flsh_c + self.flash()
        else:
            return 0

    def continue_flashing(self):
        if np.all(self.data == 0):
            return False
        else:
            return True

myDumboOctopuses1 = DumboOctopuses()
myDumboOctopuses1.read_input_data()
for i in range(100):
    myDumboOctopuses1.next_step()
print("Puzzle 1:")
print(f"After step {i+1}:")
print(myDumboOctopuses1.flash_count)

myDumboOctopuses2 = DumboOctopuses()
myDumboOctopuses2.read_input_data()
while myDumboOctopuses2.next_step():
    pass
print("Puzzle 2:")
print(f"After step {myDumboOctopuses2.step_count}:")
