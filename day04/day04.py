#!/usr/bin/env python3

import sys
import traceback


def check(grid, rows, cols, i, j) -> int:
    nbrcount = 0
    for rowidx in range(i-1, i+2):
        for colidx in range(j-1, j+2):
            if colidx < 0 or colidx >= rows or rowidx < 0 or rowidx >= cols or (rowidx == i and colidx == j):
                print(f"{rowidx} {colidx} outside the grid - do not use same cell-{(rowidx == i and colidx == j)}")
            else:
                print(
                    f"{rowidx} {colidx} inside the grid - ok to use. Value is {grid[rowidx][colidx]}")
                if grid[rowidx][colidx] == '@':
                    nbrcount += 1

    print(f"nbrcount for {i}, {j} is {nbrcount}")
    return nbrcount


def part_1(lines: list[list[str]]) -> int:
    rows = len(lines)
    cols = len(lines[0])
    okays = 0

    outter = []
    for i in range(rows):
        for j in range(cols):
            outter.append(lines[i][j])
            if lines[i][j] == '@':
                print(f"{i} {j}  Neighbor check required")
                if check(lines, rows, cols, i, j) < 4:
                    print("sparse neighbour")
                    okays += 1
                else:
                    print("crowded neighbour")
            else:
                print(f"{i} {j}  Neighbor check NOT required")

        outter.append('\n')

    return okays


def part_2(lines: list[str]) -> None:
    # Placeholder for part 2 solution; currently just parses lines
    parsed = [line.strip() for line in lines if line.strip()]
    print(f"Part 2 received {len(parsed)} non-empty lines")


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
        print('small  part 1: 13\n')
        print("Answer part 1: should be\n", part_1(lines))
        # print('small  part 2: ANSWER 2')
        # print("Answer part 2: should be", part_2(lines))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
