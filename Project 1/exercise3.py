import linear_equation_methods as le


# Main
def main():
    A = [[10, -7, 0], [-3, 2, 6], [5, -1, 5]]

    B = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

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
    L = le.cholesky(B)
    print("\nFor the matrix B:")
    le.print_matrix(B)
    print(
        "The Lower triangular matrix we get by executing the Cholesky decomposition is:"
    )
    le.print_matrix(L)

    # Exercise 3c


# Call main
if __name__ == "__main__":
    main()
