###############################################################
# Advent of Code 2021                                         #
# Day 18 https://adventofcode.com/2021/day/18                 #
# Puzzle input at https://adventofcode.com/2021/day/18/input  #
###############################################################

# with a lot of help from bwerner!!!
# https://github.com/benediktwerner


from math import ceil
from functools import reduce
from itertools import permutations


def read_binTree(it, n=0):
    d = next(it)
    if d == "[":
        n += 1
        left_node = read_binTree(it, n)
        d = next(it)
    if d in "0123456789":
        return int(d)
    if d == ",":
        right_node = read_binTree(it, n)
        d = next(it)
    if d == "]":
        n -= 1
    return [left_node, right_node]


def add_to_left(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_to_left(x[0], n), x[1]]


def add_to_right(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_to_right(x[1], n)]


def explode_snailfish_number(x, n=0) -> (bool, int, [], int):
    if isinstance(x, int):
        return False, None, x, None
    l, r = x
    if n >= 4:
        return True, l, 0, r
    exp, a, l, b = explode_snailfish_number(l, n+1)
    if exp:
        return True, a, [l, add_to_left(r, b)], None
    exp, a, r, b = explode_snailfish_number(r, n+1)
    if exp:
        return True, None, [add_to_right(l, a), r], b
    return False, None, x, None


def split_snailfish_number(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, ceil(x / 2)]
        return False, x
    a, b = x
    change, a = split_snailfish_number(a)
    if change:
        return True, [a, b]
    change, b = split_snailfish_number(b)
    return change, [a, b]

def add_snailfish_number(a, b):
    res =  [a, b]
    while True:
        change, _, res, _ = explode_snailfish_number(res)
        if change:
            continue
        change, res = split_snailfish_number(res)
        if not change:
            break
    return res


def magnitude(x):
    if isinstance(x, int):
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


with open("input_day18.txt", "r") as fs:
    data = map(str.strip, fs)
    result = [read_binTree(iter(line)) for line in data]
    print(result[0])
    print("Puzzle 1: {}".format(magnitude(reduce(add_snailfish_number, result))))
    print("Puzzle 2: {}".format(max(magnitude(add_snailfish_number(a, b)) for a, b in permutations(result, 2))))
