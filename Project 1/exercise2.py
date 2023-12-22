import function_graph as cf
import iterative_methods as it


# Define function f
def f(x):
    return 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4


# Derivative of f
def df_dx(x):
    return 324*x**5 + 225*x**4 - 408*x**3 - 207*x**2 + 70*x + 16


# Second derivative of f
def df2_dx2(x):
    return 1620*x**4 + 900*x**3 - 1224*x**2 - 414*x + 70


# This function can be ignored
def print_results(method_name, results):
    """ Helper void function that prints results of our calculations """
    max_root_length = max(len(str(result[0])) for result in results if result[0] is not None)
    max_iterations_length = max(len(str(result[1])) if result[1] is not None else 0 for result in results)

    print(f"{method_name}:")
    for i, result in enumerate(results, start=1):
        root, iterations = result
        if iterations is not None:
            print(f"\tRoot {i}:\t{root:>{max_root_length}} | Iterations executed: {iterations:>{max_iterations_length}}")
        else:
            print(f"\tRoot {i}:\t{root} | {iterations}")


# Main
def main():
    # Display the graph of the function
    # cf.display_graph(f, (-2, 2))

    # Calculate roots for our function
    bisection_2_results = (
        it.bisection_2(f, -1.5, -1.3),
        it.bisection_2(f, -0.7, -0.6),
        it.bisection_2(f, 0.1, 0.3),
        it.bisection_2(f, 0.4, 0.6),
        it.bisection_2(f, 1.1, 1.2)
    )

    newton_raphson_2_results = (
        it.newton_raphson_2(f, df_dx, df2_dx2, -1.4),
        it.newton_raphson_2(f, df_dx, df2_dx2, -0.65),
        it.newton_raphson_2(f, df_dx, df2_dx2, 0.15),
        it.newton_raphson_2(f, df_dx, df2_dx2, 0.4),
        it.newton_raphson_2(f, df_dx, df2_dx2, 1.15)
    )

    secant_2_results = (
        it.secant_2(f, -1.5, -1.4, -1.3),
        it.secant_2(f, -7, -0.65, -0.6),
        it.secant_2(f, 0.1, 0.2, 0.3),
        it.secant_2(f, 0.43, 0.48, 0.53),
        it.secant_2(f, 1.1, 1.15, 1.2)
    )

    # Print results
    print("Approximation of roots by:")
    print_results("1. Bisection variation", bisection_2_results)
    print_results("2. Newton-Raphson variation", newton_raphson_2_results)
    print_results("3. Secant variation", secant_2_results)


# Call main
if __name__ == "__main__":
    main()
