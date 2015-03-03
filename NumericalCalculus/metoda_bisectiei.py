#Libraries
import math
import numpy as np
import matplotlib.pyplot as plt
#Root parameters
roots = []
numberOfRoots = 5
precision = -13
#Function Plot
start = 0
end = 10
#Axis Plot
plotXStart = -10
plotXEnd = 10
plotYStart = -10
plotYEnd = 10
#Auxiliary mathematical functions
e = math.e
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
#Function to analyze
def f(x):
    return 3 - e**(sin(2*(x**2)) + cos(x**2))
#The Bisection Method
def bisectionMethod (a, b, err, n):
    if len(roots) < numberOfRoots:
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
    else:
        return
#Main and Plot
if __name__ == "__main__":
    
    for i in np.arange(start, end, 0.1):
        bisectionMethod(i, i + 0.1, 10.0**precision, 0)
        
    t = np.arange(start, end, 0.1)
    t1 = [ f(x) for x in t]
    
    plt.plot(t, t1, '-b')
    plt.plot([plotXStart, plotXEnd], [0, 0], '-k')
    plt.plot([0, 0], [plotYStart, plotYEnd], '-k')
    plt.plot(roots, [0 for x in range(len(roots))], 'or')
    plt.axis([plotXStart, plotXEnd, plotYStart, plotYEnd])
    plt.title('Bisection Method')
    plt.show()   
    
