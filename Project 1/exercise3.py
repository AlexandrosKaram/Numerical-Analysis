import linear_equation_methods as le


# Main
def main():
    A = [[10, -7, 0], [-3, 2, 6], [5, -1, 5]]
    b = [7, 4, 6]

    x = le.solve_linear_system(A, b)

    # Exercise 3a
    print("For the matrix A:")
    le.print_matrix(A)
    print("And the vector b:")
    print(b)
    print(f"The solution (x) of Ax = b is:")
    print(x)

    # Exercise 3b
    B = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

    L = le.cholesky(B)
    print("\nFor the matrix B:")
    le.print_matrix(B)
    print(
        "The Lower triangular matrix we get by executing the Cholesky decomposition is:"
    )
    le.print_matrix(L)

    # Exercise 3c
    C = le.initialize_matrix(10)  # Matrix of size 10x10 filled with zeros
    b = [1] * 10  # Our vector
    b[0] = b[-1] = 3

    for i in range(10 - 1):
        C[i][i] = 5
        C[i][i + 1] = C[i + 1][i] = -2
    C[9][9] = 5

    print("\nFor the 10x10 Matrix, the result is:")
    print(le.gauss_seidel(C, b))

    C = le.initialize_matrix(10000)
    b = [1] * 10000
    b[0] = b[-1] = 3

    for i in range(10000 - 1):
        C[i][i] = 5
        C[i][i + 1] = C[i + 1][i] = -2
    C[9999][9999] = 5

    print("\nFor the 10000x10000 Matrix, the result is:")
    print(le.gauss_seidel(C, b, 100000))


# Call main
if __name__ == "__main__":
    main()
