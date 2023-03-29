###############################################################
# Advent of Code 2021                                         #
# Day 22 https://adventofcode.com/2021/day/22                 #
# Puzzle input at https://adventofcode.com/2021/day/22/input  #
###############################################################
from typing import NamedTuple
import pytest

class body(NamedTuple):
    on: bool
    x: tuple[int, int]
    y: tuple[int, int]
    z: tuple[int, int]

    def score(self):
        if self.on:
            return (self.x[1]+1 - self.x[0]) * (self.y[1]+1 - self.y[0]) * (self.z[1]+1 - self.z[0])
        else:
            return -(self.x[1]+1 - self.x[0]) * (self.y[1]+1 - self.y[0]) * (self.z[1]+1 - self.z[0])

    @classmethod
    def parse_input_1(cls, s:str):
        com, range = s.split(' ')
        x, y, z = range.split(',')
        x, y, z = x[2:], y[2:], z[2:]
        x_0, x_1 = x.split('..')
        y_0, y_1 = y.split('..')
        z_0, z_1 = z.split('..')
        crop_input = lambda i: 50 if int(i) > 50 else -50 if int(i) < -50 else int(i)
        if (-50<=int(x_0)<=50 or -50<=int(x_0)<=50) and (-50<=int(y_0)<=50 or -50<=int(y_0)<=50) and (-50<=int(z_0)<=50 or -50<=int(z_0)<=50):
            return cls(com == 'on', list(map(crop_input, [x_0, x_1])), list(map(crop_input, [y_0, y_1])), list(map(crop_input, [z_0, z_1])))
        else:
            return None

    @classmethod
    def parse_input_2(cls, s:str):
        com, range = s.split(' ')
        x, y, z = range.split(',')
        x, y, z = x[2:], y[2:], z[2:]
        x_0, x_1 = x.split('..')
        y_0, y_1 = y.split('..')
        z_0, z_1 = z.split('..')

        return cls(
            com == 'on',
            (int(x_0), int(x_1)),
            (int(y_0), int(y_1)),
            (int(z_0), int(z_1))
        )

    def __eq__(self, other):
        return(self.on == other.on and self.x == other.x and self.y == other.y and self.z == other.z)


def test_score():
    test_body_1 = body(on=True, x=(9, 11), y=(9, 11), z=(9, 11))
    test_body_2 = body(on=False, x=(9, 11), y=(9, 11), z=(9, 11))
    test_body_3 = body(on=True, x=(-9, 9), y=(-9, 9), z=(-9, 9))
    assert test_body_1.score() == 3*3*3
    assert test_body_2.score() == -3*3*3
    assert test_body_3.score() == 19*19*19

def get_overlap(r, b):
    a  = not b.on
    x0, x1 = max(r.x[0], b.x[0]), min(r.x[1], b.x[1])
    y0, y1 = max(r.y[0], b.y[0]), min(r.y[1], b.y[1])
    z0, z1 = max(r.z[0], b.z[0]), min(r.z[1], b.z[1])
    return None if x0>x1 or y0>y1 or z0>z1 else body(a, x = (x0, x1), y = (y0,y1), z = (z0,z1))

def test_get_overlap():
    ref_body = body.parse_input_2("on x=-20..26,y=-36..17,z=-47..7")
    new_body = body.parse_input_2("on x=-20..33,y=-21..23,z=-26..28")
    res_body = body.parse_input_2("off x=-20..26,y=-21..17,z=-26..7")
    assert get_overlap(ref_body, new_body) == res_body

def solve(part_1 = False):
    list_of_bodies = []
    with open("./input_day22.txt", "r") as fs:
        for step in fs.read().splitlines():
            new_body = body.parse_input_2(step) if not part_1 else body.parse_input_1(step)
            if new_body:
                add_to_list = [new_body] if new_body.on else []
                for b in list_of_bodies:
                    overlap = get_overlap(new_body, b)
                    if overlap:
                        add_to_list += [overlap]
                list_of_bodies += add_to_list
    return sum(i.score() for i in list_of_bodies)

print("Part 1:", solve(part_1=True))
print("Part 2:", solve(part_1=False))
