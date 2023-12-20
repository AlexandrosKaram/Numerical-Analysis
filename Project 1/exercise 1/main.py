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

    # calculate function root using iterative methods
    print("Root of f using:")
    print("a. Bisection method:", it.bisection(f, 0, 3))
    print("b. Newton-Raphson method:", it.newton_raphson(f, df_dx, 0))

# call main
if __name__ == "__main__":
    main()
    