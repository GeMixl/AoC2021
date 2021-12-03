###############################################################
# Advent of Code 2021                                         #
# Day 1 https://adventofcode.com/2021/day/3                   #
# Puzzle input at https://adventofcode.com/2021/day/3/input   #
###############################################################

def reduce_by_bit_crit1(d, k):
    res = 0
    if len(d) == 1:
        return (d)
    for i in d:
        res += 1 if i[k] == '1' else -1
    if res >= 0:
        return [i for i in d if i[k] =='1']
    else:
        return [i for i in d if i[k] =='0']


def reduce_by_bit_crit2(d, k):
    res = 0
    if len(d) == 1:
        return(d)
    for i in d:
        res += 1 if i[k] == '1' else -1
    if res < 0:
        return [i for i in d if i[k] =='1']
    else:
        return [i for i in d if i[k] =='0']


with open("input_day03.txt", "r") as fs:
    data = [i.strip("\n") for i in fs]
result = [0] * len(data[0])
for i in data:
    for (idx, j) in enumerate(i):
        result[idx] += 1 if j == '1' else -1
gamma = [1 if i>=0 else 0 for i in result]
epsilon = [0 if i>=0 else 1 for i in result]

gamma_int = int("".join(str(i) for i in gamma), 2)
epsilon_int = int("".join(str(i) for i in epsilon), 2)
print("First Puzzle:")
print(gamma_int * epsilon_int)
print("")

oxgenrating = data
for i in range(0, len(oxgenrating[0])):
    oxgenrating = reduce_by_bit_crit1(oxgenrating, i)

co2scrubb = data
for i in range(0, len(co2scrubb[0])):
    co2scrubb = reduce_by_bit_crit2(co2scrubb, i)

oxgenrating_int = int("".join(str(i) for i in oxgenrating), 2)
co2scrubb_int = int("".join(str(i) for i in co2scrubb), 2)
print("Second Puzzle:")
print(oxgenrating_int * co2scrubb_int)