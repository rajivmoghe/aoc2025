import os
import sys


def get_ranges(aline: str):
    return [list(apiece.split('-')) for apiece in aline.split(',')]


def part_1(inlist):
    """Slower, brute force algorithm"""
    total = 0

    for i in range(100000):
        x = int(str(i) * 2)
        for l, h in inlist:
            if int(l) <= x <= int(h):
                total += x

    return total


def part_2(inlist):
    count = 0
    found = set()

    def is_mult(num_str, block_len):
        if block_len >= len(num_str) or len(num_str) % block_len != 0:
            return False
        num_blocks = len(num_str) // block_len
        block = num_str[:block_len]
        for i in range(1, num_blocks):
            if num_str[i*block_len:(i+1)*block_len] != block:
                return False
        return True

    for st, en in inlist:
        for numstr in range(int(st), int(en)+1):
            for blksize in [1, 2, 3, 4, 5]:
                if is_mult(str(numstr), blksize):
                    if numstr not in found:
                        # print(numstr, blksize)
                        count += 1
                    found.add(int(numstr))
                    pass

    # print("counted", count, "numbers.")
    return sum(found)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        rangelist = get_ranges(f.readline().strip())
        pass

    print('small  part 1: 1227775554')
    print("Answer part 1:", part_1(rangelist))
    print('small  part 2: 4174379265')
    print("Answer part 2:", part_2(rangelist))
