#!/usr/bin/python3
"""
Module doc
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (list of list of integers): A 2D grid where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is land (1)
            if grid[i][j] == 1:
                # Check all four sides (up, down, left, right)
                if i == 0 or grid[i-1][j] == 0:  # top
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # left
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # right
                    perimeter += 1

    return perimeter
