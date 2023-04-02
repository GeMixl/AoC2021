###############################################################
# Advent of Code 2021                                         #
# Day 25 https://adventofcode.com/2021/day/25                 #
# Puzzle input at https://adventofcode.com/2021/day/25/input  #
###############################################################
import pytest
import unittest.mock as mock

def test_move_eastbound_only():
    grid_step_zero = ["...>>>>>..."]
    grid_step_one = ["...>>>>.>.."]
    grid_step_two = ["...>>>.>.>."]
    assert move_herd(grid_step_zero) == grid_step_one
    assert move_herd(grid_step_one) == grid_step_two

def test_move_eastbound():
    grid_step_zero = ["...>>>>>.v."]
    grid_step_one =  ["...>>>>.>v."]
    grid_step_two =  ["...>>>.>>v."]
    assert move_herd(grid_step_zero) == grid_step_one
    assert move_herd(grid_step_one) == grid_step_two

def test_move_eastbound_2d():
    grid_step_zero =  ["...>>>>>...",
                       "...>>>>>..."]
    grid_step_one = ["...>>>>.>..",
                     "...>>>>.>.."]
    grid_step_two = ["...>>>.>.>.",
                     "...>>>.>.>."]
    assert move_herd(grid_step_zero) == grid_step_one
    assert move_herd(grid_step_one) == grid_step_two

def test_move_eastbound_turnover_2d():
    grid_step_zero = ["...>>>>>",
                      "...>>>>>"]
    grid_step_one =  [">..>>>>.",
                      ">..>>>>."]
    assert move_herd(grid_step_zero) == grid_step_one
    grid_step_zero = ["...>>>>.",
                      "...>>>>."]
    grid_step_one =  ["...>>>.>",
                      "...>>>.>"]
    assert move_herd(grid_step_zero) == grid_step_one
    grid_step_zero = [">..>>>>.",
                      ">..>>>>."]
    grid_step_one =  [".>.>>>.>",
                      ".>.>>>.>"]
    assert move_herd(grid_step_zero) == grid_step_one

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

def move_herd(grid):
    new_grid = [line.replace(">.", ".>") for line in grid]
    new_grid = ['>'+new_grid[idx][1:-1]+'.' if line[-1]+line[0] == ">." else new_grid[idx] for idx, line in enumerate(grid)]
    return new_grid

def test_transpose_grid():
    my_grid = [".v.", ".v.", ".v."]
    tr_grid = ["...", ">>>", "..."]
    assert transpose_grid(my_grid) == tr_grid
    assert transpose_grid(transpose_grid(my_grid)) == my_grid

def transpose_grid(grid):
    return ["".join(">" if i=="v" else "v" if i==">" else "." for i in line) for line in zip(*grid)]

def test_solve():
    st_one_str = """v...>>.vv>
                    .vv>>.vv..
                    >>.>v>...v
                    >>v>>.>.v.
                    v>v.vv.v..
                    >.>>..v...
                    .vv..>.>v.
                    v.v..>>v.v
                    ....v..v.>"""
    step_two = ["....>.>v.>",
                "v.v>.>v.v.",
                ">v>>..>v..",
                ">>v>v>.>.v",
                ".>v.v...v.",
                "v>>.>vvv..",
                "..v...>>..",
                "vv...>>vv.",
                ">.v.v..v.v"]

    with mock.patch("builtins.open", mock.mock_open(read_data=st_one_str)) as mock_file:
        assert solve() == step_two

def solve(filename = "test_day25.txt"):
    with open(filename, 'r') as fs:
        grid = [line.strip() for line in fs]
    new_grid = []
    i = 1
    while True:
        new_grid = transpose_grid(move_herd(transpose_grid(move_herd(grid))))
        if new_grid==grid: break
        i += 1
        grid = new_grid
    return i

print(solve(filename="input_day25.txt"))
