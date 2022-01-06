###############################################################
# Advent of Code 2021                                         #
# Day 10 https://adventofcode.com/2021/day/10                 #
# Puzzle input at https://adventofcode.com/2021/day/10/input  #
###############################################################

from collections import deque

with open("input_day10.txt", "r") as fs:
    data = [in_str.strip('\n') for in_str in fs]

mapping = {'<': '>', '{': '}',  '[': ']', '(': ')'}
points1 = {'>': 25137, '}': 1197, ']': 57, ')': 3}
points2 = {'>': 4, '}': 3, ']': 2, ')': 1}
score1 = 0
score2 = []
for d in data:
    checker = deque()
    for i in d:
        if i in '<[{(':
            checker.append(i)
        if i in ')}]>':
            opening = checker.pop()
            closing = mapping[opening]
            if closing != i:
                score1 += points1[i]
                checker.clear()
                break
    tmp_score = 0
    while len(checker) > 0:
        bracket = mapping[checker.pop()]
        tmp_score *= 5
        tmp_score += points2[bracket]
    if tmp_score > 0:
        score2.append(tmp_score)

score2.sort()

print("Puzzle 1: ")
print(score1)
print("Puzzle 2:")
print(score2[len(score2)//2])

