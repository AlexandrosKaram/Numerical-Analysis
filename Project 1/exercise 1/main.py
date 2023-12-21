import function_graph as cf
import numpy as np
import iterative_methods as it


# define our function
def f(x):
    return 14*x*np.exp(x-2) - 12*np.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12
    

# derivative of our f function in respect of x
def df_dx(x):
    return -26 + 40*x - 21*x**2 + 2*np.exp(x-2)*(1+7*x)


# main
def main():
    # print the graph of our function
    cf.print_graph(f, (0, 3), 1000)

    # calculate roots of the function f using iterative methods
    bisection_results = (it.bisection(f, 0.5, 1), it.bisection(f, 1.5, 2))
    newton_raphson_results = (it.newton_raphson(f, df_dx, 0.5), it.newton_raphson(f, df_dx, 1.5))
    
    # print the results
    print("Approximation of roots using:")
    print("1. Bisection method:")
    print(f"\ta. Root: {bisection_results[0][0]:.5f} Iterations needed: {bisection_results[0][1]}")
    print(f"\tb. Root: {bisection_results[1][0]:.5f} Iterations needed: {bisection_results[1][1]}")
    print("2. Newton-Raphson method:")
    print(f"\ta. Root: {newton_raphson_results[0][0]:.5f} Iterations needed: {newton_raphson_results[0][1]}")
    print(f"\tb. Root: {newton_raphson_results[1][0]:.5f} Iterations needed: {newton_raphson_results[1][1]}")
    

# call main
if __name__ == "__main__":
    main()
