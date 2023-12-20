# bisection function to find an approach of the root of f in the interval [a, b]
def bisection(f, a, b):
    m = (a+b)/2   # mid-point

    # termination condition
    if f(m) == 0:
        return round(m, 5)   
    
    # recursive state
    if (f(m)*f(a)<0):
        # recur on the left half of the interval
        return bisection(f, a, m)
    else:
        # recur on the right half of the interval
        return bisection(f, m, b)