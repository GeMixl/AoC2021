###############################################################
# Advent of Code 2021                                         #
# Day 8 https://adventofcode.com/2021/day/8                   #
# Puzzle input at https://adventofcode.com/2021/day/8/input   #
###############################################################


def find_n_set(in_set: [], n:int) -> []:
    return [i for idx, i in enumerate(in_set) if len(i) == n]


def number_of_matching_letters(tst: str, ref: str) -> int:
    return sum([1 if i in tst else 0 for i in ref])


def find_zero(l):
    list_of_candidates = find_n_set(l, 6)
    seven = find_seven(l)
    four = find_four(l)
    for candidate in list_of_candidates:
        if number_of_matching_letters(candidate, four) == 3 and number_of_matching_letters(candidate, seven) == 3:
            return candidate


def find_one(l):
    result = find_n_set(l, 2)
    return result[0]


def find_two(l):
    list_of_candidates = find_n_set(l, 5)
    four = find_four(l)
    for candidate in list_of_candidates:
        if number_of_matching_letters(candidate, four) == 2:
            return candidate


def find_three(l):
    list_of_candidates = find_n_set(l, 5)
    seven = find_seven(l)
    for candidate in list_of_candidates:
        if number_of_matching_letters(candidate, seven) == 3:
            return candidate


def find_four(l):
    result = find_n_set(l, 4)
    return result[0]


def find_five(l):
    list_of_candidates = find_n_set(l, 5)
    seven = find_seven(l)
    four = find_four(l)
    for candidate in list_of_candidates:
        if number_of_matching_letters(candidate, four) == 3 and number_of_matching_letters(candidate, seven) == 2:
            return candidate


def find_six(l):
    list_of_candidates = find_n_set(l, 6)
    seven = find_seven(l)
    four = find_four(l)
    for candidate in list_of_candidates:
        if number_of_matching_letters(candidate, four) == 3 and number_of_matching_letters(candidate, seven) == 2:
            return candidate


def find_seven(l):
    result = find_n_set(l, 3)
    return result[0]


def find_eight(l):
    result = find_n_set(l, 7)
    return result[0]


def find_nine(l):
    list_of_candidates = find_n_set(l, 6)
    seven = find_seven(l)
    four = find_four(l)
    for candidate in list_of_candidates:
        if number_of_matching_letters(candidate, four) == 4:
            return candidate


def get_number_from_letters(l, mapping):
    for idx, i in enumerate(mapping):
        if len(l) == len(i) and 0 not in [k in l for k in i]:
            return str(idx)


with open("input_day08.txt", "r") as fs:
    data = [i.strip('\n').split('|')[0].strip(' ').split(' ') +
            i.strip('\n').split('|')[1].strip(' ').split(' ') for i in fs]

count = 0
for i in data:
    for j in i[10:]:
        if (len(j) == 2) | (len(j) == 3) | (len(j) == 4) | (len(j) == 7):
            count += 1
print("Puzzle 1:")
print(count)

result = 0
for i in data:
    mapping = [find_zero(i[:10]),
               find_one(i[:10]),
               find_two(i[:10]),
               find_three(i[:10]),
               find_four(i[:10]),
               find_five(i[:10]),
               find_six(i[:10]),
               find_seven(i[:10]),
               find_eight(i[:10]),
               find_nine(i[:10])]

    num = ''.join([get_number_from_letters(j, mapping) for j in i[10:]])
    result += int(num)
print("Puzzle 2:")
print(result)



