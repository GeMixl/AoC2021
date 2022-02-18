###############################################################
# Advent of Code 2021                                         #
# Day 15 https://adventofcode.com/2021/day/15                 #
# Puzzle input at https://adventofcode.com/2021/day/15/input  #
###############################################################

import numpy as np
from dataclasses import dataclass
import heapq

@dataclass
class Network:
    counter: int = 0
    nodes = []
    queue = []

    class Node:
        def __init__(self, idx, cost, neigh):
            self.idx = idx
            self.cost = cost
            self.neighbor = [i for i in neigh]
            self.predecessor = None
            self.path_cost = 99999
            self.not_visited = True

    def set_up_nodes(self, arr):
        width, height = arr.shape
        self.queue.append([0, 0])
        for i in range(height):
            for j in range(width):
                n = [i*height+x for x in range(max(0, j - 1), min(width, j + 2)) if x != j] + [y*height+j for y in range(max(0, i - 1), min(height, i + 2)) if y != i]
                self.nodes.append(self.Node(i*width+j, arr[i][j], n))


with open("input_day15.txt", "r") as fs:
    data1 = np.array([[int(j) for j in i.strip()] for i in fs])

data2 = np.tile(data1, (5,5))
mul = data1.shape[0]
for i in range(5):
    for j in range(5):
        data2[mul*i:mul+mul*i, mul*j:mul+mul*j] += i+j
        data2[data2>9] = data2[data2>9] % 10 + 1

myNetwork = Network()
myNetwork.set_up_nodes(data2)

myNetwork.nodes[0].path_cost = 0

while myNetwork.queue:
    min_dist, next_node = heapq.heappop(myNetwork.queue)
    if next_node == myNetwork.nodes[-1].idx:
        break
    if myNetwork.nodes[next_node].not_visited:
        myNetwork.nodes[next_node].not_visited = False
        for n in myNetwork.nodes[next_node].neighbor:
            if myNetwork.nodes[next_node].path_cost + myNetwork.nodes[n].cost < myNetwork.nodes[n].path_cost and myNetwork.nodes[n].not_visited:
                myNetwork.nodes[n].path_cost = myNetwork.nodes[next_node].path_cost + myNetwork.nodes[n].cost
                heapq.heappush(myNetwork.queue, [myNetwork.nodes[n].path_cost, n])

print("Puzzle 2:")
print(myNetwork.nodes[-1].path_cost)




