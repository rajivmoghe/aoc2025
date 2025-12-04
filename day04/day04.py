#!/usr/bin/env python3

import sys
import traceback


def check(grid, rows, cols, i, j) -> int:
    nbrcount = 0
    for rowidx in range(i-1, i+2):
        for colidx in range(j-1, j+2):
            if not (colidx < 0 or colidx >= rows or rowidx < 0 or rowidx >= cols or (rowidx == i and colidx == j)):
                if grid[rowidx][colidx] == '@':
                    nbrcount += 1
    return nbrcount


def part_1(lines: list[list[str]]) -> int:
    rows = len(lines)
    cols = len(lines[0])
    okays = 0

    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '@' and check(lines, rows, cols, i, j) < 4:
                okays += 1
    return okays


def part_2(lines: list[list[str]]) -> int:
    rows = len(lines)
    cols = len(lines[0])
    removed = 0

    while (True):
        okays = 0
        removelist = []
        for i in range(rows):
            for j in range(cols):
                if lines[i][j] == '@' and check(lines, rows, cols, i, j) < 4:
                    okays += 1
                    removelist.append([i,j])
        
        for apoint in removelist:
            lines[apoint[0]][apoint[1]] = '.'

        removed += okays

        if (okays == 0):
            break

    return removed


def process_lines(lines: list[str]) -> list[list[str]]:
    return [list(line) for line in lines]


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        print(f"Read {len(lines)} lines from {filename}")
        lines = process_lines(lines)
        print('small  part 1: 13')
        print("Answer part 1: should be", part_1(lines))
        print('small  part 2: 43')
        print("Answer part 2: should be", part_2(lines))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
