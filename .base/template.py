#!/usr/bin/env python3

import sys
import traceback


def part_1(lines: list[str]) -> None:
    # Placeholder for part 1 solution; currently just parses lines
    parsed = [line.strip() for line in lines if line.strip()]
    print(f"Part 1 received {len(parsed)} non-empty lines")


def part_2(lines: list[str]) -> None:
    # Placeholder for part 2 solution; currently just parses lines
    parsed = [line.strip() for line in lines if line.strip()]
    print(f"Part 2 received {len(parsed)} non-empty lines")


def process_lines(lines: list[str]) -> list[str]:
    # Placeholder for parsing lines; based on input format
    # Return type changes based on input and requirements
    return lines


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        print(f"Read {len(lines)} lines from {filename}")
        lines = process_lines(lines)
        print('small  part 1: ANSWER 1')
        print("Answer part 1: should be", part_1(lines))
        print('small  part 2: ANSWER 2')
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
