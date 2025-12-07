#! /usr/bin/env python3

def solve():
    # Read the input file
    with open('input.txt', 'r') as f:
        grid = [line.rstrip('\n') for line in f]

    # Find the starting position (S)
    start_row = 0
    start_col = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                start_row = row
                start_col = col
                break

    # Count unique timelines using memoization
    # Each timeline is defined by the sequence of choices made at splitters
    memo = {}

    def count_paths(row, col):
        """Count the number of distinct paths from (row, col) to the bottom."""

        # Check if we've already computed this
        if (row, col) in memo:
            return memo[(row, col)]

        # Base case: exited the bottom of the grid
        if row >= len(grid):
            return 1

        # Check bounds
        if col < 0 or col >= len(grid[0]):
            return 0

        # Check what's at the current position
        cell = grid[row][col]

        if cell == '^':
            # Hit a splitter - particle goes both left and right
            # Each creates its own set of timelines
            left_paths = count_paths(row + 1, col - 1)
            right_paths = count_paths(row + 1, col + 1)
            result = left_paths + right_paths
        else:
            # Empty space or S - continue downward
            result = count_paths(row + 1, col)

        memo[(row, col)] = result
        return result

    return count_paths(start_row, start_col)

if __name__ == '__main__':
    result = solve()
    print(f"Total number of timelines: {result}")
