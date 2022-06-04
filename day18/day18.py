###############################################################
# Advent of Code 2021                                         #
# Day 18 https://adventofcode.com/2021/day/18                 #
# Puzzle input at https://adventofcode.com/2021/day/18/input  #
###############################################################

from collections import deque

with open("test_day18.txt", "r") as fs:
    data = [i for i in fs.readline()]

data = deque(data)


class Node:
    def __init__(self, m=None):
        self.isVal = False
        self.left_node = None
        self.right_node = None
        self.parent = m

    def __str__(self):
        return str(self.value)


def print_nodes(dat):
    res = []
    if type(dat.left_node) == Node:
        res += ["[",  print_nodes(dat.left_node)]
    else:
        res += ["[",  str(dat.left_node)]
    if type(dat.right_node) == Node:
        res += [print_nodes(dat.right_node), "]"]
    else:
        res = res + [",", str(dat.right_node), "]"]
    return "".join(res)


def read_binTree(dat, m=None):
    d = dat.popleft()
    if d == "[":
        n = Node(m)
        n.left_node = read_binTree(dat, n)
        d = dat.popleft()
    if d in "0123456789":
        return int(d)
    if d == ",":
        n.right_node = read_binTree(dat, n)
        d = dat.popleft()
    if d == "]":
        return n


def add_node(n1: Node, n2: Node) -> Node:
    n = Node(None)
    n.left_node, n.right_node = n1, n2
    n.left_node.parent_node = n
    n.right_node.parent_node = n
    return n


def explode_node(n: Node, level: int = 0, payload: int = None) -> int:
    level += 1
    if type(n) is not Node:
        return False
    if type(n.left_node) is not Node and type(n.right_node) is not Node and level > 4:
        print(f"found number pair {n.left_node}, {n.right_node} at level = {level+1}")
        return True
    if explode_node(n.left_node, level, payload):
        print(f"redistribute {n.left_node.left_node}, {n.left_node.right_node}")
        payload = n.left_node.right_node
        n.left_node = 0
    if explode_node(n.right_node, level, payload):
        pass


myNode1 = read_binTree(data)
myNode2 = read_binTree(deque("[1,2]"))
myNode3 = add_node(myNode1, myNode2)
print(print_nodes(myNode3))
explode_node(myNode1)
print(print_nodes(myNode3))
