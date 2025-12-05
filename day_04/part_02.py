#! /usr/bin/env python3

def find_accessible_rolls(grid):
    """Find all paper rolls that can be accessed by forklifts (< 4 adjacent rolls)."""
    rows = len(grid)
    cols = len(grid[0])
    accessible_positions = []

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
                    accessible_positions.append((row, col))

    return accessible_positions

def remove_rolls(grid, positions):
    """Remove rolls at specified positions from the grid."""
    # Convert grid to list of lists for mutability
    mutable_grid = [list(row) for row in grid]

    # Remove rolls at specified positions
    for row, col in positions:
        mutable_grid[row][col] = '.'

    # Convert back to list of strings
    return [''.join(row) for row in mutable_grid]

def count_total_removable_rolls(grid):
    """Count total rolls that can be removed through iterative process."""
    current_grid = grid[:]  # Make a copy
    total_removed = 0

    while True:
        # Find all accessible rolls
        accessible_positions = find_accessible_rolls(current_grid)

        # If no more rolls can be accessed, stop
        if not accessible_positions:
            break

        # Remove the accessible rolls
        current_grid = remove_rolls(current_grid, accessible_positions)
        total_removed += len(accessible_positions)

    return total_removed

if __name__ == "__main__":
    # Read the input file
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]

    # Count total removable rolls
    result = count_total_removable_rolls(grid)
    print(f"Total rolls of paper that can be removed: {result}")
