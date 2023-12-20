import numpy as np
import matplotlib.pyplot as plt
import math

# define the function
def f(x):
    if 0<=x<=3:
        return 14*x*math.exp(x-2) - 12*math.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12
    else:
        return None
    
