# recursive bisection function
def bisection(f, a, b):
    m = (a+b)/2

    # final state
    if f(m) == 0:
        return round(m, 5)
    
    # recursive state
    if (f(m)*f(a)<0):
        return bisection(f, a, m)
    else:
        return bisection(f, m, b)