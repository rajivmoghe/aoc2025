import os
import time
import sys


class Dial:
    def __init__(self, size: int = 100, start: int = 50):
        self.size = size
        self.pointer = start
        # counts all touches of 0 (passes + landings)
        self.crossed_counter = 0
        self.landed_counter = 0    # counts only landings at 0

    def traverse(self, direction: str, steps: int) -> tuple[int, int, int]:
        """
        Move the dial pointer by 'steps' in the given direction ('R'/'L' or 'right'/'left').
        Returns (new_position, crossed_hits, landed_hits) for this move.
        """
        d = direction.strip().lower()
        delta = steps if d in ("r", "right") else -steps
        abs_steps = abs(delta)

        wraps = abs_steps // self.size
        remainder = abs_steps % self.size

        new_index = (self.pointer + delta) % self.size

        crossed_hits = wraps
        landed_hits = 0

        if new_index == 0:
            self.landed_counter += 1
        else:
            if delta > 0:  # moving right
                if self.pointer + remainder >= self.size:
                    crossed_hits += 1
            else:  # moving left
                if self.pointer - remainder < 0 and self.pointer != 0:
                    crossed_hits += 1

        self.crossed_counter += crossed_hits
        self.pointer = new_index

        return self.pointer, crossed_hits, landed_hits

    def traverse_slow_clear(self, direction: str, steps: int) -> tuple[int, int, int]:
        """
        Clear slow method: simulates each step to verify logic.
        Counts:
        - crossed_hits: times we pass through 0 (boundary crossing)
        - landed_hits: times we end a step exactly on 0
        """
        d = direction.strip().lower()
        delta = 1 if d in ("r", "right") else -1

        crossed_hits = 0
        landed_hits = 0
        current = self.pointer

        for i in range(steps):
            next_pos = (current + delta)
            if next_pos < 0:
                next_pos = self.size - 1
            elif next_pos > self.size - 1:
                next_pos = 0
            else:
                pass

            if next_pos == 0 and steps - i == 1:
                landed_hits += 1

            if current == 0 and next_pos == 1 and i != 0:
                crossed_hits += 1
            if current == 0 and next_pos == self.size - 1 and i != 0:
                crossed_hits += 1

            current = next_pos

        # Update the actual pointer and counters
        self.pointer = current
        self.crossed_counter += crossed_hits
        self.landed_counter += landed_hits

        return self.pointer, crossed_hits, landed_hits


dial = Dial()


def stream_file(filename: str, idle_timeout: float = 1.0):
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        last_activity = time.time()

        while True:
            line = f.readline()
            if line:
                dial.traverse(line.strip()[0], int(line.strip()[1:]))
                last_activity = time.time()  # reset timer whenever we get data
            else:
                # No new data yet
                if time.time() - last_activity > idle_timeout:
                    print(f"No new input for {idle_timeout} seconds. Exiting.")
                    break
                time.sleep(0.5)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    stream_file(filename)
    print("Final position:", dial.pointer )
    print("Total crossed:", dial.crossed_counter)
    print("Total landed:", dial.landed_counter)
    print("Final Count:", dial.crossed_counter + dial.landed_counter)
