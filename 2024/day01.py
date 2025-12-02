#!/usr/bin/env python3

import sys

def part_1(lines: list[str]) -> None:
    lft, rgt = [], []
    for aline in lines:
        l, r = aline.strip().split(None)
        lft.append(l)
        rgt.append(r)

        lft.sort()
        rgt.sort()
        dist = 0

        for i in range(min(len(lft), len(rgt))):
            dist += abs(int(lft[i]) - int(rgt[i]))           

    print("Processing complete.")
    print(f"Final distance: {dist}")
    pass

def part_2(lines: list[str]) -> None:
    lft, rgt = [], []
    for aline in lines:
        l, r = aline.strip().split(None)
        lft.append(int(l))
        rgt.append(int(r))

    similarity_score = 0
    for num in lft:
        count = rgt.count(num)
        similarity_score += num * count

    print("Processing complete.")
    print(f"Similarity score: {similarity_score}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python day01.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        print(f"Read {len(lines)} lines from {filename}")
        part_1(lines)
        part_2(lines)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
