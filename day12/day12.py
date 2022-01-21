###############################################################
# Advent of Code 2021                                         #
# Day 12 https://adventofcode.com/2021/day/12                 #
# Puzzle input at https://adventofcode.com/2021/day/12/input  #
###############################################################

# Thanks to
# https://github.com/DenverCoder1/Advent-of-Code-2021/tree/main/Day-12

import copy
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Network:

    nodes = defaultdict(list)

    def insert_node(self, n1, n2):
        self.nodes[n1].append(n2)
        self.nodes[n2].append(n1)

    def dfs_traverse(self, visit_twice):
        return self.next_step('start', [], {'start'}, visit_twice)

    def next_step(self, n, path, already_visited, visit_twice):
        path.append(n)
        if n == 'end':
            # print(path)
            return 1
        path_count = 0
        for node in self.nodes[n]:
            if node not in already_visited or not node.islower():
                path_count += self.next_step(node, copy.deepcopy(path), already_visited | {node}, visit_twice)
            elif visit_twice and node not in {'start', 'end'}:
                path_count += self.next_step(node, copy.deepcopy(path), already_visited | {node}, False)
        return path_count

with open("input_day12.txt", "r") as fs:
    input_data = [line.strip("\n").split("-") for line in fs]

myNetwork = Network()
for i in input_data:
    myNetwork.insert_node(i[0], i[1])

print("Puzzle 1:")
print(myNetwork.dfs_traverse(visit_twice=False))
print("Puzzle 2: ")
print(myNetwork.dfs_traverse(visit_twice=True))
