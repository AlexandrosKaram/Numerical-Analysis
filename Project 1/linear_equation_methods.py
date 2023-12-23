"""
    Methods used in exercise 3.
"""


def initialize_matrix(n):
    return [[0] * n for _ in range(n)]


def swap_rows(matrix, r1, r2):
    temp_matrix = []
    for row in matrix:
        if row == matrix[r1]:
            temp_matrix.append(matrix[r2])
        elif row == matrix[r2]:
            temp_matrix.append(matrix[r1])
        else:
            temp_matrix.append(row)

    return temp_matrix


def lu_decomposition(A):
    """Function that receives a matrix and returns the respective P L and U matrices.

        Parameters:
            A (list): The array to be decomposed.

        Returns:
            P (list): The Permutation matrix.
            L (list): The Lower matrix.
            U (list): The upper matrix.
    """
    n = len(A)

    # Initialize P, L matrices
    P = initialize_matrix(n)
    L = initialize_matrix(n)
    
    # Put ones in main diagonal of P, L
    for i in range(n):
        P[i][i] = 1
        L[i][i] = 1

    # Execute pivoting
    for j in range(n-1):
        max_value = abs(A[j][j])
        pivot_row = j
        for i in range(j+1, n):
            if abs(A[i][j]) > max_value:
                max_value = abs(A[i][j])    
                A = swap_rows(A, pivot_row, i) 
                P = swap_rows(P, pivot_row, i)
    
    # Copy edited A to U
    U = A[:]
    print(U)


A = [
    [0, 3, -1],
    [2, 1, 4],
    [1, 4, -2]
]
lu_decomposition(A)
