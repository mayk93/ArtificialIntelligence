import math
import numpy as np
import matplotlib.pyplot as plt

roots = []

e = math.e

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def f(x):
    return 3 - e**(sin(2*(x**2)) + cos(x**2))

def bisectionMethod (a, b, err, n):
    
    c = (a + b) / 2.0
    fa = f(a)
    fb = f(b)
    fc = f(c)
    if fc == 0 or math.fabs(fc) < err:
        print ("c = " + str(c))
        print ("n:" + str(n))
        roots.append(c)
        return
    elif (fa * fc < 0):
        bisectionMethod(a, c, err, n + 1)
    elif (fc * fb < 0):
        bisectionMethod(c, b, err, n + 1)


if __name__ == "__main__":
    
    for i in np.arange(-10, 10, 0.1):
        bisectionMethod(i, i + 0.1, 10.0**-13, 0)
        
    t = np.arange(-10, 10, 0.1)
    t1 = [ f(x) for x in t]
    
    plt.plot(t, t1, '-b')
    plt.plot([-10, 10], [0, 0], '-k')
    plt.plot([0, 0], [-10, 10], '-k')
    plt.plot(roots, [0 for x in range(len(roots))], 'or')
    plt.axis([-10, 10, -10, 10])
    plt.title('Bisection Method')
    plt.show()   
    