import function_graph as cf
import numpy as np
import iterative_methods as it


# Define function f
def f(x):
    return 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * x**3 + 20 * x**2 - 26 * x + 12


# Derivative of function f in respect of x
def df_dx(x):
    return -26 + 40 * x - 21 * x**2 + 2 * np.exp(x - 2) * (1 + 7 * x)


# Main
def main():
    # Print the graph of our function
    cf.display_graph(f, (0, 3), 1000)

    print("Check for quadratic convergence for both roots.")
    # Calculate roots of the function f using iterative methods
    bisection_results = (
        it.bisection(f, 0.5, 1), 
        it.bisection(f, 1.5, 2.1)
    )
    newton_raphson_results = (
        it.newton_raphson(f, df_dx, 0.5, print_convergence=True),
        it.newton_raphson(f, df_dx, 1.5, print_convergence=True),
    )
    secant_method_results = (
        it.secant(f, 0.5, 1), 
        it.secant(f, 1.5, 2.1)
    )
    
    print("We can clearly see that f converges quadratically only for the first root.\n")

    # Print the results
    print("Approximation of roots using:")
    print("1. Bisection method:")
    print(f"\ta. Root: {bisection_results[0][0]} Iterations needed: {bisection_results[0][1]}")
    print(f"\tb. Root: {bisection_results[1][0]} Iterations needed: {bisection_results[1][1]}")
    print("2. Newton-Raphson method:")
    print(f"\ta. Root: {newton_raphson_results[0][0]} Iterations needed: {newton_raphson_results[0][1]}")
    print(f"\tb. Root: {newton_raphson_results[1][0]} Iterations needed: {newton_raphson_results[1][1]}")
    print("3. Secant method:")
    print(f"\ta. Root: {secant_method_results[0][0]} Iterations needed: {secant_method_results[0][1]}")
    print(f"\tb. Root: {secant_method_results[1][0]} Iterations needed: {secant_method_results[1][1]}")


# Call main
if __name__ == "__main__":
    main()
