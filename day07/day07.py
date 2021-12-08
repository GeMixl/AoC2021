###############################################################
# Advent of Code 2021                                         #
# Day 6 https://adventofcode.com/2021/day/6                   #
# Puzzle input at https://adventofcode.com/2021/day/6/input   #
###############################################################
global lookup


def dist0(c, m):
    return sum([m - i if m > i else i - m for i in c])


def dist1(c, m):
    return sum([lookup[m-i] if m > i else lookup[i-m] for i in c])


def median(c):
    return c[len(c)//2]


with open("input_day07.txt", "r") as fs:
    crabs = [int(i) for i in fs.readline().split(",")]
crabs.sort()

lookup = [n//2 * (n+1) if n % 2 == 0 else n//2 * (n+1) + n//2 + 1 for n in range(2000)]

med = median(crabs)
guess = dist1(crabs, med)
guess_hi = dist1(crabs, med+1)
guess_lo = dist1(crabs, med-1)

if guess > guess_lo:
    med -=1
    while guess > guess_lo:
        med -= 1
        guess = guess_lo
        guess_lo = dist1(crabs, med)
if guess > guess_hi:
    med += 1
    while guess > guess_hi:
        med += 1
        guess = guess_hi
        guess_hi = dist1(crabs, med)
result = guess

print(result)
