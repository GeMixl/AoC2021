###############################################################
# Advent of Code 2021                                         #
# Day 13 https://adventofcode.com/2021/day/12                 #
# Puzzle input at https://adventofcode.com/2021/day/13/input  #
###############################################################

def print_page(lst: [], print_to_terminal: bool) -> int:
    width = max(i[0] for i in lst)+1
    height = max(i[1] for i in lst)+1
    count = 0
    for i in range(height):
        if print_to_terminal: print(f'{i}--> ', end='')
        for j in range(width):
            if [j, i] in lst:
                if print_to_terminal: print("#", end='')
                count += 1
            else:
                if print_to_terminal: print(".", end='')
        if print_to_terminal: print()
    return count



with open("input_day13.txt", "r") as fs:
    coord_input, instr_input = fs.read().split("\n\n")

coord = [[int(i.split(',')[0]), int(i.split(',')[1])] for i in coord_input.split('\n')]
instr = [(i.split('=')[0].strip("fold along "), int(i.split('=')[1])) for i in instr_input.split('\n')]

for orientation, axis in instr[0:1]:
    if orientation == "y":
        for c in range(len(coord)):
            if coord[c][1] > axis:
                coord[c][1] = axis - coord[c][1] + axis
    if orientation == "x":
        for c in range(len(coord)):
            if coord[c][0] > axis:
                coord[c][0] = axis - coord[c][0] + axis

print("Puzzle 1:")
print(print_page(coord, False))

for orientation, axis in instr[1:]:
    if orientation == "y":
        for c in range(len(coord)):
            if coord[c][1] > axis:
                coord[c][1] = axis - coord[c][1] + axis
    if orientation == "x":
        for c in range(len(coord)):
            if coord[c][0] > axis:
                coord[c][0] = axis - coord[c][0] + axis

print("Puzzle 2:")
print(print_page(coord, True))

