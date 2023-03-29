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

'''
    def __str__(self):
        s = ''
        for i in range(self.x[0], self.x[1]+1):
            for j in range(self.y[0], self.y[1]+1):
                for k in range(self.z[0], self.z[1]+1):
                    s+= f'{i}, {j}, {k}\n'
        return s
'''

def test_score():
    test_body_1 = body(on=True, x=(9, 11), y=(9, 11), z=(9, 11))
    test_body_2 = body(on=False, x=(9, 11), y=(9, 11), z=(9, 11))
    test_body_3 = body(on=True, x=(-9, 9), y=(-9, 9), z=(-9, 9))
    assert test_body_1.score() == 3*3*3
    assert test_body_2.score() == -3*3*3
    assert test_body_3.score() == 19*19*19


def test_check_for_overlap():
    assert check_for_overlap(body.parse_input("on x=11..13,y=11..13,z=11..13"),
                             body.parse_input("on x=9..11,y=9..11,z=9..11")) is True
    assert check_for_overlap(body.parse_input("on x=11..13,y=11..13,z=11..13"),
                             body.parse_input("on x=9..10,y=10..11,z=9..10")) is False
    assert check_for_overlap(body.parse_input("on x=11..13,y=11..13,z=11..13"),
                             body.parse_input("on x=9..10,y=9..10,z=9..10")) is False
    assert check_for_overlap(body.parse_input("on x=11..13,y=11..13,z=11..13"),
                             body.parse_input("on x=9..20,y=11..13,z=11..12")) is True

def check_for_overlap(r, b):
    return ((r.x[0] <= b.x[0] <= r.x[1] or r.x[0] <= b.x[1] <= r.x[1] or b.x[0] <= r.x[0] <= b.x[1] or b.x[0] <= r.x[1] <= b.x[1] ) and
            (r.y[0] <= b.y[0] <= r.y[1] or r.y[0] <= b.y[1] <= r.y[1] or b.y[0] <= r.y[0] <= b.y[1] or b.y[0] <= r.y[1] <= b.y[1]) and
            (r.z[0] <= b.z[0] <= r.z[1] or r.z[0] <= b.z[1] <= r.z[1] or b.z[0] <= r.z[0] <= b.z[1] or b.z[0] <= r.z[1] <= b.z[1]))

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

def test_split_body():
    assert split_body(
        body(on=True, x=(11, 13), y=(11, 13), z=(11, 13)),
        body(on=True, x=( 9, 15), y=(11, 13), z=(11, 13))
    ) == [body(on=True, x=( 9, 10), y=(11, 13), z=(11, 13)),
          body(on=True, x=(14, 15), y=(11, 13), z=(11, 13))]
    assert split_body(
        body(on=True, x=(11, 13), y=(11, 13), z=(11, 13)),
        body(on=True, x=( 9, 12), y=(11, 13), z=(11, 13))
    ) == [body(on=True, x=( 9, 10), y=(11, 13), z=(11, 13))]
    assert split_body(
        body(on=True, x=(11, 13), y=(11, 13), z=(11, 13)),
        body(on=True, x=(12, 15), y=(11, 13), z=(11, 13))
    ) == [body(on=True, x=(14, 15), y=(11, 13), z=(11, 13))]
    assert split_body(
        body(on=True, x=(11, 13), y=(11, 13), z=(11, 13)),
        body(on=True, x=(12, 13), y=(11, 13), z=(11, 13))
    ) == []
    assert split_body(
        body(on=True, x=(11, 13), y=(11, 13), z=(11, 13)),
        body(on=True, x=(12, 15), y=(12, 15), z=(11, 13))
    ) == [body(on=True, x=(12, 13), y=(14, 15), z=(11, 13)),
          body(on=True, x=(14, 15), y=(12, 13), z=(11, 13)),
          body(on=True, x=(14, 15), y=(14, 15), z=(11, 13))]
    assert split_body(
        body(on=True, x=(11, 13), y=(11, 13), z=(11, 13)),
        body(on=True, x=(12, 15), y=(12, 15), z=(21, 23))
    ) == []
    assert split_body(
        body(on=True, x=(12, 14), y=(12, 14), z=(12, 14)),
        body(on=True, x=(14, 16), y=(10, 12), z=(14, 16))
    ) == [body(on=True, x=(14, 14), y=(10, 11), z=(14, 14)),
          body(on=True, x=(14, 14), y=(10, 11), z=(15, 16)),
          body(on=True, x=(14, 14), y=(12, 12), z=(15, 16)),
          body(on=True, x=(15, 16), y=(10, 11), z=(14, 14)),
          body(on=True, x=(15, 16), y=(10, 11), z=(15, 16)),
          body(on=True, x=(15, 16), y=(12, 12), z=(14, 14)),
          body(on=True, x=(15, 16), y=(12, 12), z=(15, 16))]

def test_subtract_body():
    assert split_body(
        body(on=False, x=( 9, 11), y=( 9, 11), z=( 9, 11)),
        body(on=True, x=(10, 12), y=(10, 12), z=(10, 12))
    ) == [body(on=True, x=(10, 11), y=(10, 11), z=(12, 12)),
          body(on=True, x=(10, 11), y=(12, 12), z=(10, 11)),
          body(on=True, x=(10, 11), y=(12, 12), z=(12, 12)),
          body(on=True, x=(12, 12), y=(10, 11), z=(10, 11)),
          body(on=True, x=(12, 12), y=(10, 11), z=(12, 12)),
          body(on=True, x=(12, 12), y=(12, 12), z=(10, 11)),
          body(on=True, x=(12, 12), y=(12, 12), z=(12, 12))]


def split_body(r, b):
    seg = [None, None, None]
    for i, (r_coo, b_coo) in enumerate(zip([r.x, r.y, r.z], [b.x, b.y, b.z])):
        xb0, xb1 = b_coo
        xr0, xr1 = r_coo

        xb0_lt_xref = xb0 < xr0
        xb1_gt_xref = xb1 > xr1
        xb0_eq_xref = xr0 == xb0
        xb1_eq_xref = xr1 == xb1
        xb0_in_xref = xr0 < xb0 <= xr1
        xb1_in_xref = xr0 <= xb1 < xr1

        if xb0_lt_xref and xb1_gt_xref:                         ##  --------B----------
            seg[i] = [(xb0, xr0-1), (xr0, xr1), (xr1+1, xb1)]   ##     -----R-----
        elif xb0_lt_xref and xb1_in_xref:                        # ---B---
            seg[i] = [(xb0, xr0-1), (xr0, xb1)]                  #       ---R---
        elif xb0_eq_xref and xb1_in_xref:                       ##  --B--
            seg[i] = [(xb0, xb1-1), (xb1, xr1)]                 ##  ---R---
        elif xb0_eq_xref and xb1_gt_xref:                        #  ---B---
            seg[i] = [(xb0, xr1), (xr1+1, xb1)]                  #  --R--
        elif xb0_in_xref and xb1_eq_xref:                       ##    --B--
            seg[i] = [(xb0, xb1)]                               ##  ---R---
        elif xb0_lt_xref and xb1_eq_xref:                       #   ---B---
            seg[i] = [(xr0, xb1)]                               #       -R-
        elif xb0_eq_xref and xb1_eq_xref:                        #   --B--
            seg[i] = [(xb0, xb1)]                                #   --R--
        elif xb0_in_xref and xb1_gt_xref:                       ##     ----B----
            seg[i] = [(xb0, xr1), (xr1+1, xb1)]                 ##   --R--
        elif xb0_in_xref and xb1_in_xref:                        #    --B--
            seg[i] = [(xr0, xb0-1), (xb0, xb1), (xb1+1, xr1)]    # ------R-----
        else:                                                   ##   ---B---
            seg[i] = []                                         ##           --R--

    res =  [body(on=True, x=s1, y=s2, z=s3) for s1 in seg[0] for s2 in seg[1] for s3 in seg[2]]
    return [b for b in res if not check_for_overlap(r, b)]


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
