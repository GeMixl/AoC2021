###############################################################
# Advent of Code 2021                                         #
# Day 23 https://adventofcode.com/2021/day/23                 #
# Puzzle input at https://adventofcode.com/2021/day/23/input  #
###############################################################

import sys
from collections import deque

MAX = sys.maxsize
class AmphipodHouse():
    abc_string = """
    #############
    #ij.k.l.m.np#
    ###a#c#e#g###
      #b#d#f#h#
      #########
    """
    final_config_string = """
    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########
    """
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
    burrows = [True]*8 + [False]*7
    hallway = [False]*8 + [True]*7
    lower_burrow = [1, 2] * 4 + [0] * 7
    HASH_LEN = 3
    size = 15
    amphi_to_num = {amphi: num for num, amphi in enumerate('.ABCD')}
    num_to_amphi = {num: amphi for num, amphi in enumerate('.ABCD')}
    aisle = ('i', 'j', 'k', 'l', 'm', 'n', 'p')
    caves = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    def __init__(self):
        amphi_map_string = self.read_input()
        amphi_map = self.read_input_string(amphi_map_string)
        final_amphi_map = self.read_input_string(self.final_config_string)
        # amphi_map: [#, #, ... , A, B, ., C, ...]
        abc_map = self.read_input_string(self.abc_string)
        # abc_map: [#, #, ... , i, j, ., k, ...]
        self.initial_amphi_configuration = self.generate_configuration_from_map_string(abc_map, amphi_map)
        self.initial_amphi_config_hash = self.get_hash(self.initial_amphi_configuration)
        self.final_amphi_configuration = self.generate_configuration_from_map_string(abc_map, final_amphi_map)
        self.final_amphi_config_hash = self.get_hash(self.final_amphi_configuration)
        self.aisle_idx = tuple(self.abc_to_pos[i] for i in self.aisle)
        self.adjacency_matrix = self.generate_adjacency_matrix_from_relation_string()
        self.initial_network_matrix = self.generate_network_matrix_from_config(self.adjacency_matrix, self.initial_amphi_configuration)

    def read_input_string(self, inp: str) -> [[str]]:
        return [[s for s in line.strip()] for line in inp.strip().split('\n')]

    def read_input(self, filename="input_day23.txt"):
        with open(filename, "r") as fs:
            m = fs.read()
        return m

    def generate_adjacency_matrix_from_relation_string(self) -> [[int]]:
        """
        Parses the relation string of the AmphipodHouse class, which has to be in the following format:
                X -> Y: N
                ...
            X, Y are two nodes
            N is the cost to come from X to Y resp. from Y to X
        Returns the adjacency matrix (list of lists) where each line/column represent a source/destination node.
        The matrix indicates all relations between nodes and their transfer costs. Since costs between nodes do not
        depend on direction the matrix is symmetric.
                [[...  N ], <- X
                 [... ...],
                 [ N  ...]] <- Y
                   ^   ^
                   X   Y
        """
        tree = {line.strip().split(":")[0]: int(line.strip().split(":")[1])
                for line in self.relations.strip().split("\n")}
        return  [[tree[row + " -> " + col] if row + " -> " + col in tree.keys()
                  else tree[col + " -> " + row] if col + " -> " + row in tree.keys() else 0
                  for col in "abcdefghijklmnp"]
                 for row in "abcdefghijklmnp"]

    def generate_configuration_from_map_string(self, ref_map, pos_map):
        conf = [(self.abc_to_pos[ref], pos)
                for line_ref, line_pos in zip(ref_map, pos_map)
                for ref, pos in zip(line_ref, line_pos)
                if ref in 'abcdefghijklmnp']
        conf.sort(key=lambda x: x[0])
        return [i for _, i in conf]

    def get_hash(self, conf: [int]) -> str:
        """
        Calculates a unique Hash for a configuration.
        Configuration has to be given as list of integers. List value indicate the member number and list index show the
        member position.
                [... M, N, ...]
                     ^
                 amphipod sort
        The output value is an interger hash that encodes each list value in a 3-bit number. Bits are aggregated and
        converted into hex format.
        """
        num_conf = [self.amphi_to_num[c] for c in conf]
        return hex(int(''.join([f'{c:03b}' for c in num_conf]), 2))

    def de_hash(self, hsh: str) -> [int]:
        res = bin(int(hsh, 16))[2:].zfill(self.HASH_LEN*self.size)
        num_conf = [int(res[i-self.HASH_LEN:i],2) for i in range(self.HASH_LEN, len(res)+1, self.HASH_LEN)]
        return [self.num_to_amphi[c] for c in num_conf]

    def dijkstra(self, src, network, size):
        """
        Calculates the minimum distance of one node to all the others based on the adjacency matrix *network*
        The input parameter *src* is the index of the source node and *size* is the size of the nxn matrix.

        The function returns a list of integers, that represent the distances from the source.
        """
        dist = [MAX] * size
        dist[src] = 0
        visited = [False] * size
        nextNode = src
        for node in range(size):
            minDist = MAX
            for nxt in range(size):
                if dist[nxt] < minDist and not visited[nxt]:
                    minDist = dist[nxt]
                    nextNode = nxt
            visited[nextNode] = True
            for target in range(size):
                if network[nextNode][target] > 0 and not visited[target] and dist[target] > dist[nextNode] + network[nextNode][target]:
                    dist[target] = dist[nextNode] + network[nextNode][target]
        return dist

    def generate_network_matrix_from_config(self, adj_mat: [[int]], config: [int]):
        ntw_mat = [[adj if config[c_idx] not in 'ABCD' else 0
                    for c_idx, adj in enumerate(adj_row)]
                   for r_idx, adj_row in enumerate(adj_mat)]
        return [self.dijkstra(idx, ntw_mat, self.size) for idx, _ in enumerate(ntw_mat)]

    def find_nex_possible_positions(self, netw: [[int]], amphi_config: []) -> [dict()]:
        """
        The function calculates all the possible moves for all amphipods.
        The parameter *amphi_config* is a list that contains the current ampipod positions as indices of the grid.
                [... X ...]
                     ^
                 amphipod N

        The function return value is a list of dicts, which contain the amphpod name (as str), its current position
        (as given in the input) and the possible next positions as list of their position incides.  Positions and paths
        that are blocked by other amphipods are not considered. The corresponding positions are not returned.
        Also, the function considers the rule, that amphipods only move once to the aisle.
        """
        def lower_burrows_are_settled(amphi, level, amphi_config):
           # check if all lower burrows contain already the right amphipods
           return all([a==self.final_amphi_configuration[i]
                       for i, a in enumerate(amphi_config)
                       if self.final_amphi_configuration[i] == amphi and self.lower_burrow[i] > level])

        def amphi_is_in_its_burrow(amphi, a_pos, amphi_config):
            # check if amphi is already in its burrow
            amphi_lower_burrows = [b if a==amphi else 0 for a, b in zip(self.final_amphi_configuration, self.lower_burrow)]
            return self.final_amphi_configuration[a_pos]==amphi and all([c==amphi for l,c in zip(amphi_lower_burrows, amphi_config) if l>amphi_lower_burrows[a_pos]])

        def amphi_is_in_hallway(a_pos):
            # check if amphi sits in hallway
            return self.hallway[a_pos]

        def get_free_hallway_pos(netw_row):
            # make sure amphi goes from hallway to right burrow
            return [i for i, (r, h) in enumerate(zip(netw_row, self.hallway)) if h and 0<r<MAX]

        def get_free_burrow_pos(netw_row, amphi, amphi_config):
            return [i
                    for i, (r, c) in enumerate(zip(netw_row, self.final_amphi_configuration))
                    if c==amphi and 0<r<MAX and lower_burrows_are_settled(amphi, self.lower_burrow[i], amphi_config)]

        next_pos =[{'amphi': amphi,
                    'curr_pos': a_pos,
                    'in_hallway': amphi_is_in_hallway(a_pos),
                    'in_burrow': amphi_is_in_its_burrow(amphi, a_pos, amphi_config),
                    'burrow_lvl': self.lower_burrow[a_pos],
                    'free_burrow_pos': get_free_burrow_pos(netw_r, amphi, amphi_config),
                    'next_pos': [] if amphi_is_in_its_burrow(amphi, a_pos, amphi_config)
                                    else get_free_burrow_pos(netw_r, amphi, amphi_config) if amphi_is_in_hallway(a_pos)
                                    else get_free_hallway_pos(netw_r),
                    'next_cost': [] if amphi_is_in_its_burrow(amphi, a_pos, amphi_config)
                                    else [netw_r[i] * 10 ** (self.amphi_to_num[amphi] - 1) for i in get_free_burrow_pos(netw_r, amphi, amphi_config)] if amphi_is_in_hallway(a_pos)
                                    else [netw_r[i] * 10 ** (self.amphi_to_num[amphi] - 1) for i in get_free_hallway_pos(netw_r)]
                    }
                   for a_pos, (amphi, netw_r) in enumerate(zip(amphi_config, netw)) if amphi in 'ABDC']
        return next_pos

    def get_configuration(self, conf, old_pos, new_pos):
        return ['.' if p==old_pos else conf[old_pos] if p==new_pos else i  for p, i in enumerate(conf)]

    def generate_network_from_next_position(self, nx_pos: {}, netw: [[int]]) -> [[int]]: # OBSOLETE???
        """
        Generates the follow-up adjacency matrix based on an adjacency matrix and a single entry of the next_position list.
        *netw* is a list of lists, that contains all correspondences between nodes including the distance of neighboring
        relations.
        *nx_pos* is a dict that contains the following items:
            'amphi' is the sort of amphipod
            'curr_pos' is its current position index
            'next_pos' is a list of all possible next positions in the grid (numerical indices)
        """
        set_of_possible_positions = set(nx_pos['next_pos']) | set([nx_pos['curr_pos']])
        return [[i
                 if idx_i in set_of_possible_positions
                    and idx_line in set_of_possible_positions
                 else 0
                 for idx_i, i in enumerate(line)]
                for idx_line, line in enumerate(netw)]

    def print_amphi_config_string(self, config):
        print("#############")
        print("#" + config[8] + config[9] + "." + config[10] + "." + config[11] + "." +
              config[12] + "." + config[13] + config[14] + "#")
        print("###" +  config[0] + "#" + config[2] + "#" + config[4] + "#" + config[6] + "###")
        print("  #" +  config[1] + "#" + config[3] + "#" + config[5] + "#" + config[7] + "#")
        print("  #########")
    def solve(self):
        # initialize the adjacency list of all states
        myAdjacencyList = {self.initial_amphi_config_hash: {"next_config": [], "cost": 0, "visited": True}}
        # initialize the hash stack that will hold all currently open configurations
        myHashStack = deque()
        # add the initial configuration to the hash stack
        myHashStack.append(self.initial_amphi_config_hash)
        n = 0
        while len(myHashStack) > 0 and n < 40000:
            n += 1
            # get the last hash from the stack --> DFS!
            myCurrentHash = myHashStack.popleft()
            # find the cheapest node from all unvisited nodes:
            myCurrentNode = min(myAdjacencyList.items(), key=lambda x:x[1]['cost'] if not x[1]['visited'] else MAX)
            myCurrentHash = myCurrentNode[0]
            myAdjacencyList[myCurrentHash]['visited'] = True
            # add the current hash to the adjacency list
            # de-hash to obtain the configuration
            myCurrentConfiguration = self.de_hash(myCurrentHash)
            #self.print_amphi_config_string(myCurrentConfiguration)
            # get the new network matrix from the current configuration and the static adjacency matrix
            myNetwork = self.generate_network_matrix_from_config(self.adjacency_matrix, myCurrentConfiguration)
            # get the next possible positions from the network matrix and the current configuration
            myNextPositions = self.find_nex_possible_positions(myNetwork,
                                                               myCurrentConfiguration)
            #for i in myNextPositions: print(i)
            # iterate over all next positions, get the new configurations, add those to the hash stack and the adjaceny list
            for d in myNextPositions:
                for p, s in zip(d['next_pos'], d['next_cost']):
                    c = self.get_configuration(myCurrentConfiguration, d['curr_pos'], p)
                    myNewHash = self.get_hash(c)
                    # if the node is still unkonwn:
                    if myNewHash not in myAdjacencyList.keys():
                        myHashStack.append(myNewHash)
                        myAdjacencyList[myCurrentHash]['next_config'].append((myNewHash))
                        myAdjacencyList[myNewHash] = {"next_config": [],
                                                      "cost": myAdjacencyList[myCurrentHash]['cost'] + s,
                                                      "visited": False}
                    # if the node is already known: check if the new route is cheaper and replace if so...
                    elif  myAdjacencyList[myNewHash]['cost'] > myAdjacencyList[myCurrentHash]['cost'] + s:
                        myAdjacencyList[myNewHash]['cost'] = myAdjacencyList[myCurrentHash]['cost'] + s
                    if all((f == i for (f, i) in zip(self.final_amphi_configuration, c))):
                        myAdjacencyList[myNewHash]["next_config"] = []
                        myAdjacencyList[myNewHash]["visited"] = True


        for i, (k, v) in enumerate(myAdjacencyList.items()):
            print(self.print_amphi_config_string(self.de_hash(k)), v)
            if i >10:
                break

        print(myAdjacencyList[self.final_amphi_config_hash]['cost'])

if __name__ == "__main__":
    myAmphipodHouse = AmphipodHouse()
    myAmphipodHouse.solve()