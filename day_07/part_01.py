#! /usr/bin/env python3

from collections import deque

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

    # Track beams: (row, col, direction)
    # All beams move downward in this problem
    beams = deque()
    beams.append((start_row, start_col, 'down'))

    # Track visited beam states to avoid infinite loops
    visited = set()
    visited.add((start_row, start_col, 'down'))

    # Count the number of splits
    split_count = 0

    while beams:
        row, col, direction = beams.popleft()

        # Move the beam downward (all beams move down in this problem)
        next_row, next_col = row + 1, col

        # Check if the beam exits the manifold
        if next_row >= len(grid) or next_row < 0 or next_col >= len(grid[0]) or next_col < 0:
            continue

        # Check what's at the next position
        cell = grid[next_row][next_col]

        if cell == '^':
            # Beam hits a splitter - it splits!
            # The beam stops, and two new downward beams are created
            # from the immediate left and right of the splitter
            split_count += 1

            # Create two new downward beams from left and right positions
            left_pos_state = (next_row, next_col - 1, 'down')
            right_pos_state = (next_row, next_col + 1, 'down')

            if left_pos_state not in visited and next_col - 1 >= 0:
                visited.add(left_pos_state)
                beams.append(left_pos_state)

            if right_pos_state not in visited and next_col + 1 < len(grid[0]):
                visited.add(right_pos_state)
                beams.append(right_pos_state)

        elif cell == '.' or cell == 'S':
            # Beam continues downward
            next_state = (next_row, next_col, 'down')
            if next_state not in visited:
                visited.add(next_state)
                beams.append(next_state)

    return split_count

if __name__ == '__main__':
    result = solve()
    print(f"Total number of splits: {result}")
