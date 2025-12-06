#!/usr/bin/env python3

import sys
import traceback


def process_lines(lines: list[str]) -> list[str]:
    numcount = len(lines)
    rows = []
    for i in range(numcount):
        numrow = lines[i].split()
        rows.append(numrow)
    return rows


def part_1(lines: list[str]) -> int:
    total = 0

    for i in range(len(lines[0])):
        oper = lines[len(lines) - 1][i]
        val = 0 if oper == "+" else 1
        for j in range(len(lines) - 1):
            if oper == '+':
                val += int(lines[j][i])
            else:
                val *= int(lines[j][i])
        total += val
    return total


def process_lines2(lines: list[str]) -> list[list[str]]:
    numcount = len(lines)
    for i in range(numcount):
        lines[i] = lines[i].strip('\n')

    sumnums = []
    sums = []
    for j in range(len(lines[0])-1, -1, -1):
        strnum = ""
        for k in range(numcount - 1):
            strnum = strnum + lines[k][j]
        if not strnum.strip() or j == 0:
            if j == 0:
                sumnums.append(strnum)
                sumnums.append(lines[numcount - 1][j])
            sums.append(sumnums)
            sumnums = []
            continue
        elif lines[numcount-1][j] == " ":
            sumnums.append(strnum)
        else:
            sumnums.append(strnum)
            sumnums.append(lines[numcount - 1][j])

    return sums


def part_2(sums: list[list[str]]) -> int:
    total = 0
    for asum in sums:
        if asum[-1] == "+":
            sumt = 0
            for l in range(len(asum) - 1):
                sumt += int(asum[l])
            total += sumt
        elif asum[-1] == "*":
            prodt = 1
            for l in range(len(asum) - 1):
                prodt *= int(asum[l])
            total += prodt
    return total


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        fresh = process_lines(lines)
        print('small  part 1: 4277556')
        print("Answer part 1: should be 4693419406682", part_1(fresh))
        fresh = (process_lines2(lines))
        print('small  part 2: 3263827')
        print("Answer part 2: should be 9029931401920", part_2(fresh))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
