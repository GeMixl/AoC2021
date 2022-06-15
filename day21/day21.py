###############################################################
# Advent of Code 2021                                         #
# Day 21 https://adventofcode.com/2021/day/21                 #
# Puzzle input at https://adventofcode.com/2021/day/21/input  #
###############################################################

with open("./input_day21.txt", "r") as fs:
    player1, player2 = [int(line.strip('\n').split(': ')[1]) for line in fs]


def deterministic_dice(win1, win2, score1=0, score2=0, rolling=0):
    if score2 >= 1000:
        return score1 * rolling
    win1 = (win1 + 3*rolling+6) % 10 or 10
    return deterministic_dice(win2, win1, score2, score1+win1, rolling+3)

print(f"Puzzle 1: {deterministic_dice(player1, player2)}")

'''
round rolling score1 score2 win1 win2 
0     0       4      8      0    0    
1     1,2,3   10     0      10   0
2     4,5,6   0      3      10   3
3     7,8,9   4      0      14   3
...
'''

from functools import cache

@cache
def dirac_dice(pos1, pos2, score1=0, score2=0):
    if score2 >= 21: return 0, 1

    wins1, wins2 = 0, 0
    for move, n in (3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1):
        pos1_ = (pos1 + move) % 10 or 10
        w2, w1 = dirac_dice(pos2, pos1_, score2, score1 + pos1_)
        wins1, wins2 = wins1 + n*w1, wins2 + n*w2
    return wins1, wins2

print(f"Puzzle 2: {max(dirac_dice(player1, player2))}")