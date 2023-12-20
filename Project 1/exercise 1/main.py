import matplotlib.pyplot as plt
import numpy as np


# define function
def f(x):
    return 14*x*np.exp(x-2) - 12*np.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12
    
    
# generate x and y values
x_values = np.linspace(0, 3, num=1000)
y_values = f(x_values)

# plot the function
plt.figure()
plt.plot(x_values, y_values)
plt.show()