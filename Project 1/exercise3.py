import linear_equation_methods as le


# Main
def main():
    A = [
        [10, -7, 0],
        [-3, 2, 6],
        [5, -1, 5]
    ]

    b = [7, 4, 6]

    x = le.solve_linear_system(A, b)

    print("Solution of the linear system using PA = LU:")
    print(x)


# Call main
if __name__ == "__main__":
    main()