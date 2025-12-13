from functools import lru_cache
from multiprocessing import Pool
import sys
import time
import traceback


def find_all_paths(graph, start, end, path: list | None = None, visited: set | None = None):
    if path is None:
        path = []

    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == end:
        yield path.copy()
    else:
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                yield from find_all_paths(graph, neighbor, end, path, visited)

    path.pop()
    visited.remove(start)


def part_1(graph):

    paths = list(find_all_paths(graph, 'svr', 'out'))

    print(f"Found {len(paths)} paths:")
    for i, path in enumerate(paths, 1):
        print(f"{i}. {' → '.join(path)}")

    return len(paths)


def find_paths_with_nodes(graph, start, end, required_nodes):
    required = set(required_nodes)

    def dfs(current, path, visited):
        path.append(current)
        visited.add(current)

        if current == end:
            if required.issubset(set(path)):
                yield path.copy()
        else:
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    yield from dfs(neighbor, path, visited)

        path.pop()
        visited.remove(current)

    return sum(1 for _ in dfs(start, [], set()))


def find_paths_worker(args):
    graph, first_step, end, required, max_depth = args
    required_set = set(required)
    count = 0

    def dfs(current, visited, found_required, depth):
        nonlocal count
        if depth > max_depth:
            return
        if current == end:
            if found_required == required_set:
                count += 1
            return

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_found = found_required | (
                    {neighbor} if neighbor in required_set else set())
                dfs(neighbor, visited, new_found, depth + 1)
                visited.remove(neighbor)

    # Start from first_step
    visited = {'svr', first_step}
    found = ({first_step} if first_step in required_set else set()) | (
        {'svr'} if 'svr' in required_set else set())
    dfs(first_step, visited, found, 1)
    return count


def parallel_count(graph, start, end, required, max_depth=50):
    first_neighbors = graph.get(start, [])

    if not first_neighbors:
        return 0

    # Create work for each initial branch
    tasks = [(graph, neighbor, end, required, max_depth)
             for neighbor in first_neighbors]

    with Pool() as pool:
        results = pool.map(find_paths_worker, tasks)

    return sum(results)


def count_paths_memo(graph, start, end):
    @lru_cache(maxsize=None)
    def dfs(current):
        if current == end:
            return 1

        total = 0
        for neighbor in graph.get(current, []):
            total += dfs(neighbor)

        return total

    return dfs(start)


def part_2(graph):

    paths_svr_to_fft = count_paths_memo(graph, 'svr', 'fft')
    print(paths_svr_to_fft)
    paths_fft_to_dac = count_paths_memo(graph, 'fft', 'dac')
    print(paths_fft_to_dac)
    paths_dac_to_out = count_paths_memo(graph, 'dac', 'out')
    print(paths_dac_to_out)

    answer = paths_svr_to_fft * paths_fft_to_dac * paths_dac_to_out
    
    return answer


def process_lines(lines):
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        node, neighbors = line.split(':')
        graph[node.strip()] = neighbors.strip().split()
    return graph


def main():
    if len(sys.argv) != 2:
        print("Usage: python day11.py <filename>. Using default small")
        # sys.exit(1)
        filename = "day11/small"
    else:
        filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        graph = process_lines(lines)
        # print('small  part 1: ANSWER 1')
        # print("Answer part 1: should be", part_1(graph))
        print(f"Total nodes: {len(graph)}")
        print(f"Total edges: {sum(len(v) for v in graph.values())}")
        print('small  part 2: ANSWER 2')
        start = time.time()
        print("Answer part 2: should be", part_2(graph))
        end = time.time()
        print(f"Time: {end - start:.3f} seconds")


    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
