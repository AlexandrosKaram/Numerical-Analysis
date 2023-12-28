import random


TOLERANCE = 10 ** (-5)  # 5 decimal digit error tolerance
MAX_ITERATIONS = 100  # Maximum iterations to decide if method converges


"""
    Functions used in exercise 1
"""


def bisection(f, a, b, it=MAX_ITERATIONS):
    """Approximation of the root of function f in the interval [a,b] using the Bisection method.

    Parameters:
        f (function): The f function.
        a (float): Lower boundary of range.
        b (float): Upper boundary of range.
        it (int): Maximum number of iterations till convergence.
    Returns:
        tuple: Tuple containing the root approximation and the number of iterations executed.
    """
    m = (a + b) / 2  # Midpoint of the interval

    # Termination condition: Check if the root is at m
    if abs(f(m)) < TOLERANCE:
        return round(m, 5), MAX_ITERATIONS - it + 1
    elif it <= 0:  # Fail condition: Check if maximum number of iterations are reached
        return "Fail", None

    # Recursive step
    if f(m) * f(a) < 0:
        # Recur on the left half of the interval, decrease iterations
        return bisection(f, a, m, it - 1)
    else:
        # Recur on the right half of the interval, decrease iterations
        return bisection(f, m, b, it - 1)


def newton_raphson(f, df_dx, x, it=MAX_ITERATIONS, print_convergence=False):
    """Aproximation of the root of function f using the Newton-Raphson method.

    Parameters:
        f (function): The function f.
        df_dx (function): The derivative of the function f.
        x (float): Initial guess.
        it (int): Maximum number of iterations till convergence.
        print_steps (bool): Print steps to study convergence.
    Returns:
        tuple: Tuple containing the root approximation and the number of iterations executed
    """
    # Termination condition: Check if the root is at x
    if abs(f(x)) < TOLERANCE:
        if print_convergence: print()
        return round(x, 5), MAX_ITERATIONS - it + 1
    elif it <= 0:  # Fail condition: Check if maximum number of iterations are reached
        return "Fail", None

    x_next = x - f(x) / df_dx(x)  # Calculate next x by the Newton-Raphson formula
    # Recursive step: call Newton Raphson with next guess, decrease iterations
    if print_convergence:
        c = abs(abs(f(x)) - abs(f(x_next)))
        print(f"{MAX_ITERATIONS - it + 1}. {c:.6f} Square: {(c**2):.6f}")
    return newton_raphson(f, df_dx, x_next, it - 1, print_convergence = print_convergence)


def secant(f, a, b, it=MAX_ITERATIONS):
    """Approximation of the root of function f in the interval [a,b] using the Secant method.

    Parameters:
        f (function): The function f.
        a (float): Lower boundary of range.
        b (float): Upper boundary of range.
        it (int): Maximum number of iterations till convergence.
    Returns:
        tuple: Tuple containing the root approximation or error message and the number of iterations executed.
    """
    # Execute Secant method
    xn = b
    xn_1 = a
    while it >= 0:
        x_next = xn - f(xn) * (xn - xn_1) / (f(xn) - f(xn_1))

        # Check if root is at x
        if abs(f(x_next)) <= TOLERANCE:
            return round(x_next, 5), MAX_ITERATIONS - it + 1

        xn_1 = xn
        xn = x_next
        it -= 1

    return "Fail", None


"""
    Functions used in exercise 2
"""


def newton_raphson_2(f, df_dx, df2_dx2, x, it=MAX_ITERATIONS):
    """Approximation of the root of function f using a Newton-Raphson method variation

    Parameters:
        f (function): The function f.
        df_dx (function): Derivative of f.
        df2_dx2 (function): Second derivative of f.
        x (float): Initial guess.
        it (int): Maximum number of iterations till convergence

    Returns:
        tuple: Tuple containing the root approximation or error message and the number of iterations executed.
    """
    # Termination condition: Check if the root is at x
    if abs(f(x)) < TOLERANCE:
        return round(x, 5), MAX_ITERATIONS - it + 1
    elif it <= 0:  # Fail condition: Check if maximum number of iterations are reached
        return "Fail", None

    x_next = x - 1 / (df_dx(x) / f(x) - 0.5 * df2_dx2(x) / df_dx(x))  # Calculate next x by new formula

    # Recursive step: call Newton Raphson with next guess, decrease iterations
    return newton_raphson_2(f, df_dx, df2_dx2, x_next, it - 1)


def bisection_2(f, a, b, it=MAX_ITERATIONS):
    """Approximation of the root of function f in the interval [a,b] using a Bisection method variation.

    Parameters:
        f (function): The f function.
        a (float): Lower boundary of range.
        b (float): Upper boundary of range.
        it (int): Maximum number of iterations till convergence.
    Returns:
        tuple: Tuple containing the root approximation or error message and the number of iterations executed.
    """
    r = random.uniform(a, b)  # Calculate r as random float within the limits

    # Termination condition: Check if the root is at m
    if abs(f(r)) < TOLERANCE:
        return round(r, 5), MAX_ITERATIONS - it + 1
    elif it <= 0:  # Fail condition: Check if maximum number of iterations are reached
        return "Fail", None

    # Recursive step
    if f(a) * f(r) < 0:
        # Recur on the left half of the interval, decrease iterations
        return bisection_2(f, a, r, it - 1)
    elif f(b) * f(r) < 0:
        # Recur on the right half of the interval, decrease iterations
        return bisection_2(f, r, b, it - 1)
    else:
        return "Fail", None


def secant_2(f, a, b, c, it=MAX_ITERATIONS):
    """Approximation of the root of function f using a variation of the Secant method.

    Parameters:
        f (function): The function f.
        a (float): Will be used as x1.
        b (float): Will be used as x2.
        c (float): Will be used as x3.
        it (int): Maximum number of iterations till convergence.
    Returns:
        tuple: Tuple containing the root approximation or error message and the number of iterations executed.
    """
    x = [a, b, c]

    while it > 0:
        q = f(x[0]) / f(x[1])
        r = f(x[2]) / f(x[1])
        s = f(x[2]) / f(x[0])

        x.append(x[2] - (r * (r - q) * (x[2] - x[1]) + (1 - r) * s * (x[2] - x[0])) / ((q - 1) * (r - 1) * (s - 1)))

        # Check if root is at x
        if abs(f(x[3])) <= TOLERANCE:
            return round(x[3], 5), MAX_ITERATIONS - it + 1

        x = x[1:]  # Pop oldest element
        it -= 1

    return "Fail", None
