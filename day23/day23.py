###############################################################
# Advent of Code 2021                                         #
# Day 23 https://adventofcode.com/2021/day/23                 #
# Puzzle input at https://adventofcode.com/2021/day/23/input  #
###############################################################

abc_string = """
#############
#ij.k.l.m.np#
###a#c#e#g###
  #b#d#f#h#
  #########
"""

abc_map = [[s for s in line.strip()] for line in abc_string.strip().split('\n')]

relations = """
    a -> b: 1
    a -> j: 2
    a -> k: 2
    j -> i: 1
    j -> k: 2
    k -> l: 2
    c -> d: 1
    c -> k: 2
    c -> l: 2
    l -> m: 2
    e -> f: 1
    e -> l: 2
    e -> m: 2
    m -> n: 2
    g -> h: 1
    g -> m: 2
    g -> n: 2
    n -> p: 1
    """

abc_to_pos = {abc: pos for pos, abc in enumerate('abcdefghijklmnp')}
pos_to_abc = {pos: abc for pos, abc in enumerate('abcdefghijklmnp')}

print(abc_to_pos)
print(pos_to_abc)

size = 15

tree = {line.strip().split(":")[0]: int(line.strip().split(":")[1])
        for line in relations.strip().split("\n")}
network = [[tree[row + " -> " + col] if row + " -> " + col in tree.keys()
            else tree[col + " -> " + row] if col + " -> " + row in tree.keys()
            else 0
            for col in "abcdefghijklmnp"] for row in "abcdefghijklmnp"]
for i in network:
    print(i)
print()

def read_input(filename = "test_day23.txt"):
    with open(filename, "r") as fs:
        m = [[i for i in line.strip()] for line in fs]
    return m

amphi_map = read_input()

amphi_positions = [(a, abc_to_pos[abc])
                   for line_abc, line_a in zip(abc_map, amphi_map)
                   for abc, a in zip(line_abc, line_a) if a in "ABDC"]
amphi_positions = list(zip(*amphi_positions))
print(amphi_positions)
print()

def dijkstra(src, network, size):
    dist = [999] * size
    dist[src] = 0
    visited = [False] * size
    nextNode = src
    for node in range(size):
        minDist = 999
        for nxt in range(size):
            if dist[nxt] < minDist and not visited[nxt]:
                minDist = dist[nxt]
                nextNode = nxt
        visited[nextNode] = True
        for target in range(size):
            if network[nextNode][target] > 0 and not visited[target] and dist[target] > dist[nextNode] + network[nextNode][target]:
                dist[target] = dist[nextNode] + network[nextNode][target]
    return dist
print()

cost = [dijkstra(i, network, 15) for i in range(size)]
for i in cost:
    print(i)
print()

next_positions = [{'amphi': amphi,
                   'next_pos': {pos_to_abc[d_idx]: d for d_idx, d in enumerate(network[i]) if d_idx not in amphi_positions[1]}
                   }
                  for amphi, i in zip(*amphi_positions)]
print(next_positions[0])
print()

network = [[i for idx_i, i in enumerate(line) if idx_i in next_positions[0]['next_pos'].values()]
           for idx_line, line in enumerate(network) if idx_line in next_positions[0]['next_pos'].values()]
print(network)

#cost = [dijkstra(i, network, len(network[0])) for i in range(len(network[0]))]

c_fct = {"A": 1,
         "B": 10,
         "C": 100,
         "D": 1000}



def test_find_possible_configurations():
    test_maze_str = """ #############
                        #...........#
                        ###B#C#B#D###
                          #A#D#C#A#
                          #########"""
    pass

def find_possible_configurations(maze):
    pass

def solve(part2 = False):
    maze = read_input()
    print(maze)

#solve()
