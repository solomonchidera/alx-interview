#!/usr/bin/python3
"""
Module documentation
"""


def rotate_2d_matrix(matrix):
    """
    Function: rotate 2d matrix ie trying to escape the matrix 💀
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
