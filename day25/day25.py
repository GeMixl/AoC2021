###############################################################
# Advent of Code 2021                                         #
# Day 25 https://adventofcode.com/2021/day/25                 #
# Puzzle input at https://adventofcode.com/2021/day/25/input  #
###############################################################

def test_move_eastbound_only():
    grid_step_zero = ["...>>>>>..."]
    grid_step_one = ["...>>>>.>.."]
    grid_step_two = ["...>>>.>.>."]
    assert move_herd(grid_step_zero) == grid_step_one
    assert move_herd(grid_step_one) == grid_step_two

def test_move_eastbound_turnover():
    grid_step_zero = ["...>>>>>"]
    grid_step_one =  [">..>>>>."]
    assert move_herd(grid_step_zero) == grid_step_one
    grid_step_zero = ["...>>>>."]
    grid_step_one =  ["...>>>.>"]
    assert move_herd(grid_step_zero) == grid_step_one
    grid_step_zero = [">..>>>>."]
    grid_step_one =  [".>.>>>.>"]
    assert move_herd(grid_step_zero) == grid_step_one

with open("./test_day25.txt", "r") as fs:
    grid = [line[:-1] for line in fs]

def move_herd(grid):
    new_grid = [line.replace(">.", ".>") for line in grid]
    new_grid = ['>'+new_grid[idx][1:-1]+'.' if line[-1]+line[0] == ">." else new_grid[idx] for idx, line in enumerate(grid)]
    return new_grid

def test_transpose_grid():
    my_grid = [".v.", ".v.", ".v."]
    tr_grid = ["...", "vvv", "..."]
    assert transpose_grid(my_grid) == tr_grid
    assert transpose_grid(transpose_grid(my_grid)) == my_grid

def transpose_grid(grid):
    return ["".join(line) for line in zip(*grid)]
