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
    def __init__(self, p=None):
        self.left_node = None
        self.right_node = None
        self.parent_node = p


class Leaf(Node):
    def __init__(self, p, v):
        Node.__init__(self, p)
        self.val = v
        self.right_leaf = None
        self.left_leaf = None


def print_nodes(dat):
    res = []
    if type(dat.left_node) == Node:
        res += ["[",  print_nodes(dat.left_node)]
    else:
        res += ["[",  str(dat.left_node.val)]
    if type(dat.right_node) == Node:
        res += [print_nodes(dat.right_node), "]"]
    else:
        res = res + [",", str(dat.right_node.val), "]"]
    return "".join(res)


def read_binTree(dat, p=None):
    d = dat.popleft()
    if d == "[":
        n = Node(p)
        n.left_node = read_binTree(dat, n)
        d = dat.popleft()
    if d in "0123456789":
        return Leaf(p, int(d))
    if d == ",":
        n.right_node = read_binTree(dat, n)
        d = dat.popleft()
    if d == "]":
        return n


def neighborize_binTree(n: Node, payload: Leaf = None):
    if type(n) is Leaf:
        n.left_leaf = payload
        if payload is not None:
            payload.right_leaf = n
        return n
    payload = neighborize_binTree(n.left_node, payload)
    payload = neighborize_binTree(n.right_node, payload)
    return payload


def add_node(n1: Node, n2: Node) -> Node:
    n = Node(None)
    n.left_node, n.right_node = n1, n2
    n.left_node.parent_node = n
    n.right_node.parent_node = n
    return n


def explode_node(n: Node, level: int = 0) -> int:
    level += 1
    if type(n.left_node) is Leaf and type(n.right_node) is Leaf and level > 4:
        print(f"found number pair {n.left_node.val}, {n.right_node.val} at level = {level+1}")
        return True
    if explode_node(n.left_node, level):
        pass
        #print(f"redistribute {n.left_node.val} to {n.left_node.left_leaf}")
    if explode_node(n.right_node, level):
        pass
        #print(f"redistribute {n.right_node.val} to {n.right_node.right_leaf}")


myNode1 = read_binTree(data)
myNode2 = read_binTree(deque("[1,2]"))
myNode3 = add_node(myNode1, myNode2)
print(print_nodes(myNode3))
neighborize_binTree(myNode3)
explode_node(myNode1)
print(print_nodes(myNode3))
