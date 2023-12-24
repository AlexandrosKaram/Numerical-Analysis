import function_graph as cf
import iterative_methods as it


# Define function f
def f(x):
    return (
        54 * x**6
        + 45 * x**5
        - 102 * x**4
        - 69 * x**3
        + 35 * x**2
        + 16 * x
        - 4
    )


# Derivative of f
def df_dx(x):
    return 324 * x**5 + 225 * x**4 - 408 * x**3 - 207 * x**2 + 70 * x + 16


# Second derivative of f
def df2_dx2(x):
    return 1620 * x**4 + 900 * x**3 - 1224 * x**2 - 414 * x + 70


# This function can be ignored
def print_results(method_name, results):
    """Helper void function that prints results of our calculations."""
    max_root_length = max(len(str(result[0])) for result in results)
    max_iterations_length = max(len(str(result[1])) for result in results)

    print(f"{method_name}:")
    for i, result in enumerate(results, start=1):
        root, iterations = result
        if iterations is not None:
            print(
                f"\tRoot {i}:\t{root:>{max_root_length}} | Iterations executed: {iterations:>{max_iterations_length}}"
            )
        else:
            print(
                f"\tRoot {i}:\t{root:>{max_root_length}} | Iterations executed: Maximum"
            )


def calculate_results():
    """Helper function to calculate results of our methods.

    Returns:
        tuple: Tuple containing the results of each method.
    """
    bisection_2_results = (
        it.bisection_2(f, -1.5, -1.3),
        it.bisection_2(f, -0.7, -0.6),
        it.bisection_2(f, 0.1, 0.3),
        it.bisection_2(f, 0.4, 0.6),
        it.bisection_2(f, 1.1, 1.2),
    )

    newton_raphson_2_results = (
        it.newton_raphson_2(f, df_dx, df2_dx2, -1.4),
        it.newton_raphson_2(f, df_dx, df2_dx2, -0.65),
        it.newton_raphson_2(f, df_dx, df2_dx2, 0.15),
        it.newton_raphson_2(f, df_dx, df2_dx2, 0.4),
        it.newton_raphson_2(f, df_dx, df2_dx2, 1.15),
    )

    secant_2_results = (
        it.secant_2(f, -1.5, -1.4, -1.3),
        it.secant_2(f, -7, -0.65, -0.6),
        it.secant_2(f, 0.1, 0.2, 0.3),
        it.secant_2(f, 0.43, 0.48, 0.53),
        it.secant_2(f, 1.1, 1.15, 1.2),
    )

    return bisection_2_results, newton_raphson_2_results, secant_2_results


def print_results_diversity():
    """Helper void function that prints the amount of times the results differed for each method."""
    results_sets = [set(), set(), set()]
    for i in range(20):
        temp_results = calculate_results()
        results_sets[0].add(frozenset(temp_results[0]))
        results_sets[1].add(frozenset(temp_results[1]))
        results_sets[2].add(frozenset(temp_results[2]))

    print("\nOut of 20 times, results were different: ")
    print(f"For Bisection: {len(results_sets[0]) - 1} times.")
    print(f"For Newton-Raphson: {len(results_sets[1]) - 1} times.")
    print(f"For Secant: {len(results_sets[2]) - 1} times.")


def compare_variations_to_original(variation_results):
    original_results = (
        (
            it.bisection(f, -1.4, -1.3),
            it.bisection(f, -0.7, -0.6),
            it.bisection(f, 0.17, 0.22),
            it.bisection(f, 0, 46, 0.52),
            it.bisection(f, 1.1, 1.2),
        ),
        (
            it.newton_raphson(f, df_dx, -1.3),
            it.newton_raphson(f, df_dx, -1.6),
            it.newton_raphson(f, df_dx, 0.22),
            it.newton_raphson(f, df_dx, 0.43),
            it.newton_raphson(f, df_dx, 1.1),
        ),
        (
            it.secant(f, -1.4, -1.3),
            it.secant(f, -0.7, -0.6),
            it.secant(f, 0.17, 0.22),
            it.secant(f, 0.46, 0.52),
            it.secant(f, 1.1, 1.2),
        ),
    )

    variotion_times_better = 0
    original_times_better = 0
    equal = 0

    for i, method in enumerate(original_results):
        for j, result in enumerate(method):
            if result[1] != None and variation_results[i][j][1] != None:
                if result[1] < variation_results[i][j][1]:
                    original_times_better += 1
                elif result[1] == variation_results[i][j][1]:
                    equal += 1
                else:
                    variotion_times_better += 1

    print(
        f"\nOut of {variotion_times_better + original_times_better + equal} results tested:"
    )
    print(f"Variation methods appeared faster {variotion_times_better} times.")
    print(f"Original methods appeared faster {original_times_better} times.")
    print(f"Both methods were equally fast {equal} times.\n")


# Main
def main():
    # Display the graph of the function
    # cf.display_graph(f, (-2, 2))

    # Calculate roots for our function
    results = calculate_results()

    # Print results
    print("Approximation of roots by:")
    print_results("1. Bisection variation", results[0])
    print_results("2. Newton-Raphson variation", results[1])
    print_results("3. Secant variation", results[2])

    # Check if results are the same
    print_results_diversity()

    # Compare variations to original methods
    compare_variations_to_original(results)


# Call main
if __name__ == "__main__":
    main()
