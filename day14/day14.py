###############################################################
# Advent of Code 2021                                         #
# Day 13 https://adventofcode.com/2021/day/12                 #
# Puzzle input at https://adventofcode.com/2021/day/13/input  #
###############################################################

from collections import Counter, defaultdict

with open("input_day14.txt", "r") as fs:
    (input_data, instr_data) = (i.strip() for i in fs.read().split("\n\n"))

instructions = {line.split("->")[0].strip(): (line.split("->")[0].strip()[0] + line.split("->")[1].strip(), line.split("->")[1].strip()+line.split("->")[0].strip()[1])
                for line
                in instr_data.split("\n")}


def polymerize(inp, instr, steps):
    polymer = Counter([i+j for (i, j) in zip(inp[:-1], inp[1:])])
    for i in range(steps):
        # new_polymer = Counter({instr[j][k]: polymer[j] for j in instr for k in (0, 1)})
        new_polymer = defaultdict(int)
        for j in instr:
            for k in (0, 1):
                new_polymer[instr[j][k]] += polymer[j]
        polymer = new_polymer
    return polymer


def get_polymer_score(inp, poly):
    input_counter = Counter({'C': 0, 'B': 0, 'H': 0, 'N': 0})
    input_counter[inp[0]] += 1
    input_counter[inp[-1]] += 1
    for key, item in poly.items():
        input_counter[key[0]] += item
        input_counter[key[1]] += item
    return input_counter.most_common()[0][1]//2 - input_counter.most_common()[-1][1]//2

print("Puzzle 1")
my_polymer = polymerize(input_data, instructions, 10)
print(get_polymer_score(input_data, my_polymer))
print("Puzzle 2")
my_polymer = polymerize(input_data, instructions, 40)
print(get_polymer_score(input_data, my_polymer))
