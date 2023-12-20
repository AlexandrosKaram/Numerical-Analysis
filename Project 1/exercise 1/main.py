import function_graph as cf
import numpy as np


# define our function
def f(x):
    return 14*x*np.exp(x-2) - 12*np.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12
    
  

# main
def main():
    cf.print_graph(f, (0, 3), 1000)


# call main
if __name__ == "__main__":
    main()