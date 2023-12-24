import copy

"""
    Methods used in exercise 3.
"""

TOLERANCE = 10 ** (-4)


def initialize_matrix(n):
    """Initialize a matrix of size nxn with zeros."""
    return [[0] * n for _ in range(n)]


def round_matrix(A):
    """Round a matrix's values to the 2nd decimal digit."""
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = round(A[i][j], 2)


def print_matrix(A):
    """Prints a matrix."""
    for row in A:
        print("[", end="")
        for i, element in enumerate(row):
            if i < len(row) - 1:
                print(f"{element}\t", end="")
            else:
                print(element, end="")
        print("]")


def swap_rows(matrix, r1, r2):
    """Swaps two rows a matrix and returns the updated matrix."""
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
    for j in range(n - 1):
        max_value = abs(A[j][j])
        pivot_row = j
        for i in range(j + 1, n):
            if abs(A[i][j]) > max_value:
                max_value = abs(A[i][j])
                A = swap_rows(A, pivot_row, i)
                P = swap_rows(P, pivot_row, i)

    # Copy edited A to U
    U = copy.deepcopy(A)

    # Execute Gaussian elimination
    for j in range(n - 1):
        for i in range(j + 1, n):
            x = -U[i][j] / U[j][j]
            L[i][j] = -x
            for k in range(n):
                U[i][k] = U[i][k] + x * U[j][k]

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

    b_prime = []  # b'

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
    n = len(A)
    # Lower triangular matrix
    L = initialize_matrix(n)

    # Execute Cholesky
    for i in range(n):
        for j in range(i + 1):
            if i == j:  # Main diagonal
                s = sum(pow(L[j][k], 2) for k in range(j))
                L[j][j] = pow((A[j][j] - s), 1 / 2)
            else:  # Elements below main diagonal
                s = sum(L[i][k] * L[j][k] for k in range(j))
                if L[j][j] > 0:
                    L[i][j] = (A[i][j] - s) / L[j][j]

    round_matrix(L)
    return L


def infinity_norm(A):
    """Function to receive a matrix and calculate its infinite norm."""
    return max(sum(abs(A[i][j]) for j in range(len(A[0]))) for i in range(len(A)))


def gauss_seidel(A, b, max_iterations=1000):
    """Function that executes the Gauss-Seidel method.

    Parameters:
        A (list[list]): The matrix.
        b (list): The vector matrix.
        max_iterations (int): Maximum iterations till method fails.
    Returns:
        list: The solution x.
    """
    n = len(A)
    x = [0] * n  # Initial guess of x (0)
    old_norm = 0
    iterations = 0  # Count iterations to prevent infinite loop

    # Execute Gauss-Seidel
    while iterations < max_iterations:
        # Calculate new x vector
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
        new_norm = max(
            abs(x[i]) for i in range(len(x))
        )  # Calculate infinity norm as maximum absolute value of x
        # Check if converged
        if abs(new_norm - old_norm) < TOLERANCE:
            return [round(x[i], 4) for i in range(len(x))]
        old_norm = new_norm  # Replace old norm with new norm
        iterations += 1

    # Iterations have surpassed maximum limit
    return "Gauss-Seidel method fails."
