from linear_equation_methods import print_matrix, round_matrix, initialize_matrix
from random import randrange

q = 0.15   # Probability of moving to a page
n = 15   # Total pages


def create_google_matrix(A):
    """Function that receives Adjacency matrix and creates Google matrix."""
    G = initialize_matrix(15)   # Initialize 15x15 Google matrix with zeros

    for j in range(n):
        nj = sum(A[j][i] for i in range(n))
        for i in range(n):
            G[i][j] = q/n + A[j][i]*(1-q)/nj
    
    return G


def multiply_matrix_with_vector(A, b):
    """Function that multiplies a Matrix with a Vector.
    
    Parameters:
        A (list[list]): The matrix
        b (list): The vector
    
    Returns:
        (list): The new vector
    """
    return [sum(A[i][j] * b[j] for j in range(len(b))) for i in range(len(A))]


def normalize_vector(b):
    """Function divide each element with the first non-zero element of the vector."""
    for i in range(len(b)):
        if b[i] != 0:
            return [b[j]/b[i] for j in range(len(b))]

    print("Error")
    return b


def power_method(A):
    """Function that executes the power method.
    
    Parameters:
        A (list[list]): The matrix we want to execute the power method with.
    
    Returns:
        (list): The eigenvector of the maximum eigenvalue
    """
    b = [1]*len(A[0])  # Base vector of 1's

    for i in range(len(A[0])):
        b = multiply_matrix_with_vector(A, b)
        b = normalize_vector(b)

    return b


# Main
def main():
    # Αdjacency matrix
    A = [
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    ]

    # Exercise 4a
    for j in range(n):
        nj = sum(A[j][i] for i in range(n))   # Sum of connections to j
        s = 0
        for i in range(n):
            s += q/n + A[j][i]*(1-q)/nj
        if s != 1:   # Sum of j-column not equal to 1
            print("Google matrix is not stochastic.")
            break
    else:   # Loop ended 
        print("Google matrix indeed is stochastic.")

    # Exercise 4b
    G = create_google_matrix(A)
    eigenvector = power_method(G)


# Call main
if __name__ == "__main__":
    main()
