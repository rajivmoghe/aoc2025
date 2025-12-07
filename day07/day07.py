#!/usr/bin/env python3

import sys
import traceback


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def part_1(lines: list[str]) -> int:
    # Placeholder for part 1 solution; currently just parses lines
    parsed = [line.strip() for line in lines if line.strip()]
    splitcount = 0
    lanes = len(parsed[0])
    beams = [' '] * lanes
    beams[parsed[0].find('S')] = "|"
    for i in range(2, len(parsed) - 1, 2):
        layer = parsed[i]
        splitters = find(layer, "^")
        for asplitter in splitters:
            if beams[asplitter] == "|":
                beams[asplitter] = ' '
                beams[asplitter - 1] = '|'
                beams[asplitter + 1] = '|'
                splitcount += 1

    return splitcount


def part_2(lines: list[str]) -> int:
    parsed = [line.strip() for line in lines if line.strip()]
    lanes = len(parsed[0])
    beams = [0] * lanes
    beams[parsed[0].find('S')] = 1
    for i in range(2, len(parsed) - 1, 2):
        layer = parsed[i]
        splitters = find(layer, "^")
        for asplitter in splitters:
            if beams[asplitter] > 0:
                beams[asplitter-1] += beams[asplitter]
                beams[asplitter+1] += beams[asplitter]
                beams[asplitter] = 0
    return sum(beams)


# Unused for this problem
# def process_lines(lines: list[str]) -> list[str]:
#     # Placeholder for parsing lines; based on input format
#     # Return type changes based on input and requirements
#     return lines


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        # lines = process_lines(lines)
        print('small  part 1: ANSWER 21')
        print("Answer part 1: should be 1640. Is", part_1(lines))
        print('small  part 2: ANSWER 2')
        print("Answer part 2: should be 40999072541589. Is ", part_2(lines))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
