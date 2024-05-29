def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in the Pascal's Triangle.

    Returns:
        list of lists of ints: A list of lists representing Pascal's Triangle.
            Each inner list represents a row in the triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    triangle = []

    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    return triangle
