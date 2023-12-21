TOLERANCE = 10**(-5)   # 5 decimal digit error tolerance 
MAX_ITERATIONS = 100   # Maximum iterations to decide if method converges


def bisection(f, a, b, it=MAX_ITERATIONS):
    """ Approximation of the root of function f in the interval (a,b) using the Bisection method

        Parameters:
            f (function): The f function.
            a (float): Lower boundary of range.
            b (float): Upper boundary of range.
            it (int): Maximum number of iterations till convergence.        
        Returns:
            tuple: Tuple containing the root approximation and the number of iterations executed.
    """
    m = (a+b)/2   # Midpoint of the interval

    # Termination condition: check if the root is at m or have reached the maximum number of iterations
    if abs(f(m)) < TOLERANCE:   
        return m, MAX_ITERATIONS-it+1
    elif it <= 0:
        return None, MAX_ITERATIONS-it
    
    # Recursive step
    if (f(m)*f(a)<0):
        # Recur on the left half of the interval, decrease iterations
        return bisection(f, a, m, it-1)
    else:
        # Recur on the right half of the interval, decrease iterations
        return bisection(f, m, b, it-1)


def newton_raphson(f, df_dx, x, it=MAX_ITERATIONS):
    """ Aproximation of the root of function f using the Newton-Raphson method

        Parameters:
            f (function): The function f.
            df_dx (function): The derivative of the function f.
            x (float): Initial guess.
            it (int): Maximum number of iterations till convergence.
        Returns:
            tuple: Tuple containing the root approximation and the number of iterations executed
    """
    # Termination condition: check if the root is at x or have reached the maximum number of iterations
    if abs(f(x)) < TOLERANCE:  
        return x, MAX_ITERATIONS-it+1
    elif it <= 0:
        return None, MAX_ITERATIONS-it

    x_next = x - f(x)/df_dx(x)
    # Recursive step: call Newton Raphson with next guess, decrease iterations
    return newton_raphson(f, df_dx, x_next, it-1)


# approach of the root of function f in the interval (a,b) using the Secant method
def secant(f, x0, x1):
    x_next = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
    # termination condition
    if (abs(f(x_next)) < TOLERANCE):
        return round(x_next, 5)
    
    # recursive step
    return secant(f, x1, x_next)