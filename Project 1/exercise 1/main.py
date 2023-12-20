import matplotlib.pyplot as plt
import numpy as np


# define function
def f(x):
    return 14*x*np.exp(x-2) - 12*np.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12
    
    
# function to print graph
def print_graph(function, x_range, num=1000):
    # generate x and y values
    x_values = np.linspace(x_range[0], x_range[1], num)
    y_values = function(x_values)

    # plot the function
    plt.figure()
    plt.plot(x_values, y_values)
    plt.title("f Graph")
    plt.xlabel('x-ayis')
    plt.ylabel('y-axis')

    plt.show()


# main
def main():
    print_graph(f, (0, 3), 1000)


# call main
if __name__ == "__main__":
    main()