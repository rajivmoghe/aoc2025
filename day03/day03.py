#!/usr/bin/env python3

import sys
import traceback


def part_1(lines: list[list[int]]) -> int:
    joltage: int = 0
    for aline in lines:
        leftidx: int = 0
        leftval: int = 0
        rghtval: int = 0

        for i in range(len(aline) - 1):
            if aline[i] > leftval:
                leftval = aline[i]
                leftidx = i

        for j in range(leftidx+1, len(aline)):
            if aline[j] > rghtval:
                rghtval = aline[j]

        joltage += leftval*10 + rghtval

    return joltage


def get_max_at(line, _frm, pos):
    idx, val = _frm, 0
    for i in range(_frm, len(line) - pos +1):
        if line[i] > val:
            val = line[i]
            idx = i

    return idx, val


def part_2(lines: list[list[int]]) -> int:
    joltage: int = 0
    for aline in lines:
        outvals = []
        outidxs = []
        stridx = 0
        for j in range(12, 0, -1):
            idx, val = get_max_at(aline, stridx, j)
            stridx = idx + 1
            outvals.append(val)
            outidxs.append(idx)
        num = int("".join(str(d) for d in outvals))
        joltage += num

    return joltage


def process_lines(lines: list[str]) -> list[list[int]]:
    parsed: list[list[int]] = [
        [int(d) for d in aline.strip()] for aline in lines]
    return parsed


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        lines = process_lines(lines)
        print('small  part 1: 357')
        print("Answer part 1: (should be 17435)", part_1(lines))
        print('small  part 2: 3121910778619')
        print("Answer part 2: (should be 172886048065379)", part_2(lines))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
