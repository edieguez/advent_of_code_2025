#! /usr/bin/env python3

def count_accessible_rolls(grid):
    """Count paper rolls that can be accessed by forklifts."""
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0

    # Define the 8 adjacent directions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Check each position in the grid
    for row in range(rows):
        for col in range(cols):
            # Only check positions that have paper rolls
            if grid[row][col] == '@':
                adjacent_rolls = 0

                # Count adjacent paper rolls
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # Check if the adjacent position is within bounds
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if grid[new_row][new_col] == '@':
                            adjacent_rolls += 1

                # A roll is accessible if it has fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1

    return accessible_count

if __name__ == "__main__":
    # Read the input file
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]

    # Count accessible rolls
    result = count_accessible_rolls(grid)
    print(f"Number of accessible paper rolls: {result}")

