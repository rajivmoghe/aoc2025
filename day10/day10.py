#!/usr/bin/env python3

from collections import deque
import itertools
import sys
import traceback


def min_press_toggles(target: int, masks: list[int]) -> tuple[int, list[int]]:

    # Try smallest subsets first (greedy by size)
    for k in range(1, len(masks) + 1):
        # If k gets too big, we might want to stop
        if k > len(masks):  # Or some reasonable limit
            print("Something's very wrong. Shouldn't  have reached here.")
            break

        for combo in itertools.combinations(masks, k):
            # Compute XOR of all masks in combo
            xor_val = 0
            for mask in combo:
                xor_val ^= mask
            if xor_val == target:
                return k, list(combo)

    return -1, []


def part_1(machines: list[int | list[int]]) -> int:
    press_counts = 0

    for amachine in machines:
        min_pushes, path = min_press_toggles(amachine[0], amachine[1])
        print(
            f"MinPushes for machine {amachine}, bitwidth {amachine[2]} found in {min_pushes} button presses via path {path}.")
        press_counts += min_pushes
        pass

    return press_counts


def part_2(lines: list[str]) -> None:
    # Placeholder for part 2 solution; currently just parses lines
    parsed = [line.strip() for line in lines if line.strip()]
    print(f"Part 2 received {len(parsed)} non-empty lines")


def process_lines(lines: list[str]) -> list[int | list[int]]:
    machines = []
    for aline in lines:
        # print(f"ALINE = {aline}")
        target_str = aline[aline.find('[')+1:aline.find(']')]
        n = len(target_str)
        target = int(target_str.replace('.', '0').replace('#', '1'), 2)

        toggle_masks_str = aline[aline.find(
            ' ') + 1:  aline.find('{') - 1].split(' ')
        toggle_masks = [sum(1 << (n - 1 - int(p))
                            for p in s.strip("()").split(",")) for s in toggle_masks_str]

        # adder_masks_str = map (int, (aline[aline.find('{') + 1:  aline.find('}')].split(',')))
        # print(f"Adder Mask str: {adder_masks_str}")
        # adder_masks = [sum(1 << (n - 1 - int(p))
        #                     for p in s.split(",")) for s in adder_masks_str]
        

        machines.append([target, toggle_masks, n])
        # print(f"Process line: {aline} \t Values are target: {target}, T-masks: {toggle_masks}, A-masks: {adder_masks} .")

    return machines


def main():
    if len(sys.argv) != 2:
        print("Usage: python day02.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        lines = process_lines(lines)

        print('small  part 1: 7')
        print("Answer part 1: should be", part_1(lines))
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
