import function_graph as cf


# Define function f
def f(x):
    return 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4


# Derivative of f
def df_dx(x):
    return 324*x**5 + 225*x**4 - 408*x**3 - 207*x**2 + 70*x + 16


# Second derivative of f
def df2_dx2(x):
    return 1620*x**4 + 900*x**3 - 1224*x**2 - 414*x + 70