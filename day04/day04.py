###############################################################
# Advent of Code 2021                                         #
# Day 4 https://adventofcode.com/2021/day/4                   #
# Puzzle input at https://adventofcode.com/2021/day/4/input   #
###############################################################

import numpy as np


def check_if_won(b):
    lng, wid = b.shape
    return np.any([np.all(b[:, i] == -999) for i in range(lng)]) | np.any([np.all(b[i, :] == -999) for i in range(wid)])


def get_bingo_score(b, num):
    return sum([sum([i for i in row if i != -999]) for row in b]) * num


with open("input_day04.txt", "r") as fs:
    instructions = [int(i) for i in fs.readline().strip("\n").split(",")]
    game_input = [[[int(i) for i in fs.readline().strip("\n").strip(" ").split(" ") if i != ''] for j in range(5)] for i in fs]

boards = [np.array(i) for i in game_input]
board_count = [[i, 0, 0] for i in range(len(boards))]
rank = 0

for m, instruction in enumerate(instructions):
    remaining_boards = [i[0] for i in board_count if i[1] == 0]
    for board_num in remaining_boards:
        np.place(boards[board_num], boards[board_num] == instruction, -999)
        if check_if_won(boards[board_num]):
            rank += 1
            board_count[board_num][1] = rank
            board_count[board_num][2] = get_bingo_score(boards[board_num], instruction)

print("Puzzle 1:")
print("{}".format([i[2] for i in board_count if i[1] == 1]))
print()
print("Puzzle 2:")
print("{}".format([i[2] for i in board_count if i[1] == rank]))



