#!/usr/bin/python3
"""
Module Docs
"""


def canUnlockAll(boxes):
    """
    Function Docs
    """
    # Number of boxes
    n = len(boxes)

    # Set to keep track of unlocked boxes
    unlocked = set()
    unlocked.add(0)  # First box is unlocked

    # Stack to keep track of boxes to check
    stack = [0]  # Start with the first box

    # Traverse boxes
    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == n

