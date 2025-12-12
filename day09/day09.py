#!/usr/bin/env python3

import sys
import traceback
import matplotlib.pyplot as plt



def part_1(tiles: list[tuple[int, ...]]) -> int:
    maxarea = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            tilearea = (abs(tiles[j][0] - tiles[i][0]) + 1) * \
                (abs(tiles[j][1] - tiles[i][1]) + 1)
            maxarea = max(maxarea, tilearea)

    return maxarea


def plot_the_points(points):
    x_vals = [p[0] for p in points]  # First element of each tuple
    y_vals = [p[1] for p in points]  # Second element of each tuple
    plt.figure(figsize=(10, 10))
    plt.scatter(x_vals, y_vals, s=10, color='blue', alpha=0.6)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{len(points)} Points Plot')
    plt.grid(True, alpha=0.3)
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        if x1 == x2 or y1 == y2:
            plt.plot([x1, x2], [y1, y2], 'r-', linewidth=1)

    plt.xlim(0, 100000)
    plt.ylim(0, 100000)
    plt.show()
    pass

def part_2(tiles: list[tuple[int, ...]]) -> int:
    board = []
    x, y = 0, 0

    def setgreens(t1, t2):
        print(f"setting green between {t1} and {t2}")
        if t1[0] == t2[0]:
            print("horiontal")
        elif t1[1] == t2[1]:
            print("vertical")
        else:
            print("input has been read wrong")
        pass

    for i in range(len(tiles)):
        x = max(x, tiles[i][0])
        y = max(y, tiles[i][1])

    for j in range(len(tiles)):
        k = j+1 if i < len(tiles) - 1 else 0
        setgreens(tiles[j], tiles[k])
        pass
    
    print(f"Max of x and y are: {x} , {y}")
    pass
    return 0


def process_lines(lines: list[str]) -> list[tuple[int, ...]]:

    return [tuple(map(int, aline.split(','))) for aline in lines]


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        tiles = process_lines(lines)
        # print('small  part 1: 50')
        # print("Answer part 1: should be 4748826374", part_1(tiles))
        # print('small  part 2: ANSWER 2')
        plot_the_points(tiles)
        # print("Answer part 2: should be", part_2(tiles))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
