from __future__ import annotations

from decimal import Decimal


def inverse_of_matrix(matrix: list[list[float]]) -> list[list[float]]:


    D = Decimal  # An abbreviation to be conciseness
    # Calculate the determinant of the matrix
    determinant = D(matrix[0][0]) * D(matrix[1][1]) - D(matrix[1][0]) * D(matrix[0][1])
    if determinant == 0:
        raise ValueError("This matrix has no inverse.")
    # Creates a copy of the matrix with swapped positions of the elements
    swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
    swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
    swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]
    # Calculate the inverse of the matrix
    return [[float(D(n) / determinant) or 0.0 for n in row] for row in swapped_matrix]
