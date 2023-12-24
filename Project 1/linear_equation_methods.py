import copy

"""
    Methods used in exercise 3.
"""


def initialize_matrix(n):
    """Initialize a matrix of size n with zeros"""
    return [[0] * n for _ in range(n)]


def print_matrix(A):
    """Prints a matrix"""
    for row in A:
        print(row)


def swap_rows(matrix, r1, r2):
    """Swaps two rows a matrix and returns the updated matrix"""
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
    U = copy.deepcopy(A)

    # Execute Gaussian elimination
    for j in range(n-1):
        for i in range(j+1, n):
            x = -U[i][j]/U[j][j]
            L[i][j] = -x
            for k in range(n):
                U[i][k] = U[i][k] + x*U[j][k]

    return P, L, U


def solve_linear_system(A, b):
    """Solve a linear system Ax = b and calculate the solution vector x.

        Parameters:
            A (list[list]): Coefficient matrix.
            b (list): Right-hand side vector.

        Returns:
            list: Solution vector x.
    """
    P, L, U = lu_decomposition(A)
    
    b_prime = []   # b'

    # Solve Pb = b'
    for row in P:
        b_prime.append(sum(row[j] * b[j] for j in range(len(row))))

    # Solve Ly = b' by subtitute values
    y = [0] * len(L)
    for i in range(len(L)):
        y[i] = b_prime[i]
        for j in range(i):
            # Forward subtitution step
            y[i] -= L[i][j] * y[j]

    # Solve Ux = y by subtitute values
    x = [0] * len(U[0])
    for i in range(len(U[0]) - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, len(U[0])):
            # Back subtitution step
            x[i] -= U[i][j] * x[j]
        # Divide by diagonal element 
        x[i] /= U[i][i]

    for i in range(len(x)):
        x[i] = round(x[i], 2)

    return x


def cholesky(A):
    """Function that receives a matrix A and returns its decomposed L version/
    
        Parameters:
            A (list[list]): The matrix.

        Returns:
            (list[list]): The decomposed lower triangular matrix.
    """
