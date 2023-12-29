def f(x):
    return 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * x**3 + 20 * x**2 - 26 * x + 12


# Derivative of function f in respect of x
def df_dx(x):
    return -26 + 40 * x - 21 * x**2 + 2 * np.exp(x - 2) * (1 + 7 * x)