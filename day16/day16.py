###############################################################
# Advent of Code 2021                                         #
# Day 16 https://adventofcode.com/2021/day/16                 #
# Puzzle input at https://adventofcode.com/2021/day/16/input  #
###############################################################

from operator import add, mul, gt, lt, eq

# Code adapted from viliampucik!
# https://github.com/viliampucik/adventofcode/blob/master/2021/16.py
def parse_bitstream(fs):
    data = ((int(b, base=16) >> i) & 1 for b in fs.read().strip() for i in range(3, -1, -1))
    operation = add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq
    pos = 0
    ver = 0

    def read_bits(n):
        nonlocal pos
        pos += n
        return sum(next(data) << i for i in range(n-1, -1, -1))

    def read_packet():
        nonlocal ver
        ver += read_bits(3)
        print("VERSION: {}".format(ver))
        packet_id = read_bits(3)
        if packet_id == 4:
            print("LITERAL PACKET")
            c = read_bits(1)
            message = read_bits(4)
            while c == 1:
                c = read_bits(1)
                message = message << 4 | read_bits(4)
            print("\t{}".format(message))
        else:
            print("OP PACKET {}".format(packet_id))
            c = read_bits(1)
            print("\tFLAG {}".format(c))
            if c == 0:
                sub_pac_len = read_bits(15)
                print("\tsub packet length {}".format(sub_pac_len))
                length = pos + sub_pac_len
                message = read_packet()
                while pos < length:
                    message = operation[packet_id](message, read_packet())
            else:
                sub_pac_count = read_bits(11)
                print("\tsub packet count {}".format(sub_pac_count))
                message = read_packet()
                for _ in range(sub_pac_count-1):
                    message = operation[packet_id](message, read_packet())
        return message

    message = read_packet()
    return ver, message

with open("input_day16.txt", "r") as fs:
    result = parse_bitstream(fs)

print("Puzzle 1:")
print(result[0])
print("Puzzle 2:")
print(result[1])

