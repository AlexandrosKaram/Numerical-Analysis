import matplotlib.pyplot as plt
import numpy as np


def display_graph(function, x_range, num=1000):
    """Displays the graph of a function.

    Parameters:
        function (function): Function to be displayed.
        x_range (tuple): Range of the x values.
        num (int): Number of samples to generate in plotting.
    """
    # Generate x and y values
    x_values = np.linspace(x_range[0], x_range[1], num)
    y_values = function(x_values)

    # Plot the function
    plt.figure()
    plt.plot(x_values, y_values)
    plt.grid()
    plt.title("f Graph")
    plt.xlabel("x-ayis")
    plt.ylabel("y-axis")

    plt.show()
