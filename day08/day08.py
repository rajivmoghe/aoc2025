#!/usr/bin/env python3

import math
import sys
import traceback


def part_1(points, dists, conns) -> int:

    parent = list(range(len(points)))
    size = [1] * len(points)

    def find(x):
        current = x
        while parent[current] != current:
            current = parent[current]
        return current

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

    def k_largest(k):
        rootsizes = [size[i] for i in range(len(parent)) if parent[i] == i]
        return sorted(rootsizes, reverse=True)[:k]

    for _, p1, p2 in dists[:conns]:
        union(p1, p2)

    consizes = k_largest(3)
    return math.prod(consizes)


def part_2(points, dists, conns) -> int:

    parent = list(range(len(points)))
    size = [1] * len(points)
    component_count = len(points)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        nonlocal component_count
        rootX, rootY = find(x), find(y)
        if rootX == rootY:
            return
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        parent[rootY] = rootX
        size[rootX] += size[rootY]
        component_count -= 1

    def component_size(x):
        return size[find(x)]

    for dist, p1, p2 in dists:
        union(p1, p2)
        if component_count == 1:
            critical_vals = (points[p1][0], points[p2][0])
            break

    myresult = critical_vals[0] * critical_vals[1]
    return myresult


def process_lines(lines: list[str]):
    points = []
    numboxes = len(lines)
    dists = []

    def distf(i, j):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

    for aline in lines:
        x, y, z = map(int, aline.split(','))
        points.append((x, y, z))

    for i in range(numboxes):
        for j in range(i + 1, numboxes):
            if i != j:
                dists.append((distf(i, j), i, j))

    dists.sort()
    return points, dists


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        points, dists = process_lines(lines)
        connections = 10 if "small" in filename else 1000
        print('small  part 1: 40')
        print("Answer part 1: should be 90036",
              part_1(points, dists, connections))
        print('small  part 2: 25272')
        print("Answer part 2: should be", part_2(points, dists, connections))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
