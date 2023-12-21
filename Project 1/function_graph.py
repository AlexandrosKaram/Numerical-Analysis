import matplotlib.pyplot as plt
import numpy as np

  
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
