import sympy as sp

# approach of the root of function f in the interval (a,b) using the Bisection method
def bisection(f, a, b):
    m = (a+b)/2   # mid-point

    # termination condition
    if abs(f(m)) < 10**(-5):   # 5 decimal digit precision
        return round(m, 5)   
    
    # recursive step
    if (f(m)*f(a)<0):
        # recur on the left half of the interval
        return bisection(f, a, m)
    else:
        # recur on the right half of the interval
        return bisection(f, m, b)


# approach of the root of function f using the Newton-Raphson method with initial guess - x
def newton_raphson(f, df_dx, x):
    # termination condition
    if abs(f(x)) < 10**(-5):  
        return round(x, 5)
    
    x_next = x - f(x)/df_dx(x)
    # recursive step
    return newton_raphson(f, df_dx, x_next)
