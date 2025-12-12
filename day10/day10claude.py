from functools import lru_cache
from itertools import combinations

def parse_machine(line):
    """Parse a machine line into buttons and targets"""
    # Extract buttons (in parentheses) and targets (in curly braces)
    parts = line.strip().split()
    
    buttons = []
    targets = None
    
    for part in parts:
        if part.startswith('(') and part.endswith(')'):
            # Parse button: (1,3) -> [1, 3]
            button_str = part[1:-1]
            if button_str:
                buttons.append([int(x) for x in button_str.split(',')])
        elif part.startswith('{') and part.endswith('}'):
            # Parse targets: {3,5,4,7} -> [3, 5, 4, 7]
            target_str = part[1:-1]
            targets = [int(x) for x in target_str.split(',')]
    
    return buttons, targets


def get_xor_patterns(buttons, num_counters):
    """
    Generate all possible XOR patterns by selecting subsets of buttons.
    Returns list of (button_indices, resulting_xor_pattern)
    """
    patterns = []
    num_buttons = len(buttons)
    
    # Try all possible subsets of buttons (2^n possibilities)
    for r in range(num_buttons + 1):
        for combo in combinations(range(num_buttons), r):
            # Calculate XOR pattern for this button combination
            xor_state = [0] * num_counters
            for button_idx in combo:
                for counter_idx in buttons[button_idx]:
                    xor_state[counter_idx] ^= 1
            
            patterns.append((combo, tuple(xor_state)))
    
    return patterns


def solve_machine(buttons, targets):
    """
    Solve for minimum button presses to reach target joltages.
    Uses recursive approach with memoization.
    """
    num_counters = len(targets)
    
    # Pre-compute all XOR patterns
    xor_patterns = get_xor_patterns(buttons, num_counters)
    
    # Create lookup: target_parity -> list of button combinations
    parity_to_patterns = {}
    for button_combo, xor_pattern in xor_patterns:
        if xor_pattern not in parity_to_patterns:
            parity_to_patterns[xor_pattern] = []
        parity_to_patterns[xor_pattern].append(button_combo)
    
    @lru_cache(maxsize=None)
    def min_presses(target_tuple):
        """Recursively find minimum presses to reach targets"""
        targets_list = list(target_tuple)
        
        # Base case: all zeros
        if all(t == 0 for t in targets_list):
            return 0
        
        # Invalid case: negative values
        if any(t < 0 for t in targets_list):
            return float('inf')
        
        # Calculate required parity for these targets
        required_parity = tuple(t % 2 for t in targets_list)
        
        # Get all button patterns that produce this parity
        if required_parity not in parity_to_patterns:
            return float('inf')  # Impossible to reach this parity
        
        min_cost = float('inf')
        
        # Try each valid XOR pattern
        for button_combo in parity_to_patterns[required_parity]:
            # Calculate contribution from pressing these buttons once
            contribution = [0] * num_counters
            for button_idx in button_combo:
                for counter_idx in buttons[button_idx]:
                    contribution[counter_idx] += 1
            
            # Subtract contribution from targets
            remaining = [targets_list[i] - contribution[i] for i in range(num_counters)]
            
            # Check if all remaining values are even
            if not all(r % 2 == 0 for r in remaining):
                continue  # This pattern doesn't work
            
            # Check for negative values
            if any(r < 0 for r in remaining):
                continue  # Overshot
            
            # Divide by 2 and recurse
            halved = tuple(r // 2 for r in remaining)
            recursive_cost = min_presses(halved)
            
            if recursive_cost != float('inf'):
                total_cost = len(button_combo) + 2 * recursive_cost
                min_cost = min(min_cost, total_cost)
        
        return min_cost
    
    result = min_presses(tuple(targets))
    return result if result != float('inf') else None


def main():
    # Test with the three examples from the problem
    test_cases = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    ]

    with open("input", 'r') as f:
        test_cases = [line.strip() for line in f.readlines()]
    
    # expected = [10, 12, 11]
    total = 0
    
    for i, line in enumerate(test_cases):
        buttons, targets = parse_machine(line)
        result = solve_machine(buttons, targets)
        
        print(f"Machine {i+1}: {targets}", sep=",")
        print(f"  Buttons: {buttons}")
        print(f"  Minimum presses: {result}")
        # print(f"  Expected: {expected[i]}")
        # print(f"  {'✓ CORRECT' if result == expected[i] else '✗ WRONG'}")
        print()
        
        if result is not None:
            total += result
    
    print(f"Total presses: {total}")
    # print(f"Expected total: {sum(expected)}")


if __name__ == "__main__":
    main()