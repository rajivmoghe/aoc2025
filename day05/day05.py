#!/usr/bin/env python3

import sys
import traceback


def part_1(freshset: list[tuple[int, int]], things: list[int]) -> int:
    freshcount = 0
    for athing in things:
        if any(start <= athing <= end for start, end in freshset):
            freshcount += 1

    return freshcount


def part_2(freshset: list[tuple[int, int]]) -> int:
    freshcount = 0

    def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if not ranges:
            return []

        # Sort by start
        ranges.sort(key=lambda x: x[0])
        merged = [ranges[0]]

        for current in ranges[1:]:
            last_start, last_end = merged[-1]
            curr_start, curr_end = current

            if curr_start <= last_end:  # overlap
                merged[-1] = (last_start, max(last_end, curr_end))
            else:
                merged.append(current)

        return merged

    merged_ranges = merge_ranges(freshset)
    for arange in merged_ranges:
        freshcount += (arange[1] - arange[0]) + 1

    return freshcount


def process_lines(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ingreds = []
    readrange = True
    for aline in lines:
        if not aline:
            readrange = False
            continue

        if readrange:
            start, end = map(int, aline.split('-'))
            ranges.append((start, end))
        else:
            ingreds.append(int(aline))

    return ranges, ingreds


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        fresh, stuff = process_lines(lines)
        print('small  part 1: 3')
        print("Answer part 1: should be 885", part_1(fresh, stuff))
        print('small  part 2: 14')
        print("Answer part 2: should be 348115621205535", part_2(fresh))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
