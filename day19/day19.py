###############################################################
# Advent of Code 2021                                         #
# Day 23 https://adventofcode.com/2021/day/23                 #
# Puzzle input at https://adventofcode.com/2021/day/23/input  #
###############################################################

import numpy as np
from itertools import combinations, product, permutations
from math import sqrt

# 1. read the scanners  in, bring them in the form sensor_0 = [[x, y, z], [x, y, z], ...]
#    search_set = set([[x, y, z], [x, y, z], ...] ...)

with open("./test_day19.txt", "r") as fs:
   scanners = [ np.array([[int(i) for i in ln.split(",")] for ln in sc.split("\n") if not ln[0:3] == "---"]) for sc in fs.read().split("\n\n")]

# 2. get the distances between each two points in the form [from, to, dist], [from, to, dist], ...
#    (27 * 26 / 2 = 351 point combinations)

def get_scanner_adjacency_list(sc):
   """
   Generates a list, where each list item represents the vector between two items.
   Each list item contains beacon indices and distances, all combinations of beacons are evaluated
   Ex.:  [...
          (1, 2, 10), <-- beacon 1 to beacon 3 has distance 20
          (1, 3, 20), <-- beacon 1 to beacon 3 has distance 20
          ...
         ]
   """
   def get_distance(bc_0, bc_1):
      return sqrt((bc_1[0] - bc_0[0])**2 + (bc_1[1] - bc_0[1])**2 + (bc_1[2] - bc_0[2])**2)

   from_to_list =  list(combinations(range(len(sc)), 2))
   return [[i, j, get_distance(sc[i,:], sc[j,:])] for (i, j) in from_to_list]


def get_orientation(bc_0, bc_1):
   return np.sign([b-a for (a, b) in zip(bc_0, bc_1)])


def get_correspondence_list(adj_lst_0, adj_lst_1):
   """
   Evaluates all possible correspondances between two items (i.e. scanners) of an adjacency list.
   This is done in two steps:
      1. Forming all possible combinations and keeping those where the distance values are (almost) identical (raw_list)
      2. Identifying correspondences between the points in raw_list, note that those can be switched, so I need to
         check against correspondences that are already known.
         Ex.:  (1 -> 2) corresponds to (11 -> 12)
               (2 -> 3) corresponds to (13 -> 12) <-- carefull start and end in the second vector are switched
               ... finally we get {1: 11, 2: 12, 3, 13, ...}
         Another trap could be correspondences by coincidence:
         Ex.:  (0, 0, 0) -> (1, 1, 1) of scenner 1 aligns with (11, 11, 11) -> (12, 12, 12)
               AND (51, 51, 51) -> (50, 52, 50) in scanner 2
         If I find a conflicting correspondence I skip this line.
   The result is a dict, where each item represents the correspondance between beacon incices of the two scanners.
   Ex.:  {..., 3: 13, ...} beacon 3 of scanner 1 corresponds to beacon 13 in scanner 2
   """
   raw_list = [(i, j) for (i, j) in product(adj_lst_0, adj_lst_1) if abs(i[2] - j[2]) < 0.001]
   for i in raw_list: print(i)
   cor = dict()
   for (a0, a1, _), (b0, b1, _) in raw_list:
      if a0 not in cor.keys():
         if b0 not in cor.values():
            cor[a0] = b0
         elif b1 not in cor.values():
            cor[a0] = b1
         else:
            pass
      if a1 not in cor.keys():
         if b1 not in cor.values():
            cor[a1] = b1
         elif b0 not in cor.values():
            cor[a1] = b0
         else:
            pass
   return cor


adjacency_lists = [get_scanner_adjacency_list(sc) for sc in scanners]

correspondence_list = get_correspondence_list(adjacency_lists[0], adjacency_lists[1])
print(correspondence_list)

B_inv = (np.invert(np.array([[404,-588,-901], [528,-643,409], [390,-675,-793]])))
C = (np.array([[-336,658,858], [-460,603,-452], [-322,571,750]]))

print(C * B_inv)

# 3. start with sensor 0:

# 3a. count the number of similar distances in the form [scanner 0, scanner 1, n], [scanner 0, scanner 2, m]

# 3b. find the sensor that has at least N similar distances. N=3 is required at least. And the 3 points must not lie
#     in one plain

# 3c. make a map of (possibly) corresponding connections between two points like so [from, to, from, to, dist], ...
#    for each scanner pair

# 3d. for each corresponding connection calculate the orientation in both systems as [from, to, ori, from, to, ori, dist], ...
#     ori is a vector of size 3 with either 1 or -1 indicating the orientation of the

# 3e. change the orientation of the second sensor and start over at step 3c again, if orientations of >=12 points match,
#     add a shift to the second sensor, so it aligns with the first one.

# 3f. add the new points to the first sensor and remove the second sensor from the search set.

# 3g. start over at 3a.

# 4. count the points in the first sensor