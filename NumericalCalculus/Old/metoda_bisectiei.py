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
step = 0.1
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
#Function to analyze and it's derivative
def f(x):
    return 3 - e**(sin(2*(x**2)) + cos(x**2))
def fPrime(x):
    return (- e**(sin(2*(x**2)) + cos(x**2)))*(4*x*cos(2*(x**2))-2*x*sin(x**2))
#Methods
BISECTION = 0
FALSE = 1
SECANT = 2
CORD = 3
NEWTON = 4
methods = {BISECTION:"Bisection Method",
           FALSE:"False Position Method",
           SECANT:"Secant Method",
           CORD:"Cord Method",
           NEWTON:"Newtons Method"}
#The Bisection Method
def bisectionMethod (a, b, err, n):
    if len(roots) < numberOfRoots:
        c = (a + b) / 2.0
        fa = f(a)
        fb = f(b)
        fc = f(c)
        if fc == 0 or math.fabs(fc) < err:
            print("Root",len(roots),":",c,"found at iteration",n)
            roots.append(c)
            return
        elif fa * fc < 0:
            bisectionMethod(a, c, err, n + 1)
        elif fc * fb < 0:
            bisectionMethod(c, b, err, n + 1)
    else:
        return
#False Position Method
def falsePositionMethod (a, b, err, n):
    if len(roots) < numberOfRoots:
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if a <= c and c <= b:
            if (fc == 0 or math.fabs(fc) < err) :
                roots.append(c)
                print("Root",len(roots),":",c,"found at iteration",n)
            elif fa * fc < 0:
                falsePositionMethod (a, c, err, n + 1)
            elif fc * fb < 0:
                falsePositionMethod (c, b, err, n + 1)
    else:
        return
#The Secant Method
def secantMethod(x0, x1, err, n):
    if len(roots) < numberOfRoots:
        fx0 = f(x0)
        fx1 = f(x1)
        xn = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        fxn = f(xn)
        if math.fabs(fxn) < err and math.fabs(xn - x1) < err:
            roots.append(xn)
            print("Root",len(roots),":",xn,"found at iteration",n)
        else:
            secantMethod(x1, xn, err, n + 1)
    else:
        return
#Cord Methd
def cordMethod(x0, x1, err, n):
    if len(roots) < numberOfRoots:
        fx0 = f(x0)
        fx1 = f(x1)
        xn = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        fxn = f(xn)
        if (math.fabs(fxn) < err) and (math.fabs(xn - x1) < err):
            roots.append(xn)
            print("Root",len(roots),":",xn,"found at iteration",n)
        else:
            cordMethod(x0, xn, err, n + 1)
    else:
        return
#Newtons Method
def newtonMethod(x0, err):
    if len(roots) < numberOfRoots:
        fx0 = f(x0)
        xn = x0 - f(x0) / fPrime(x0)
        fxn = f(xn)
        if (math.fabs(fxn) < err) and (math.fabs(xn - x0) < err):
            roots.append(xn)
            print("Root",len(roots),":",xn)
        else:
            newtonMethod(xn, err)
    else:
        return
#Main and Plot
def main(method):
    print("Method:",methods[method])
    for i in np.arange(start, end, step):
        if method == BISECTION:
            #Bisection Method
            if f(i) * f(i + step) < 0:
                bisectionMethod(i, i + step, 10.0**precision, 0)
        elif method == FALSE:
            #False Position Method
            if f(i) * f(i + step) < 0:
                falsePositionMethod(i, i + step, 10.0**precision, 0)
        elif method == SECANT:
            #Secant Method
            if f(i) * f(i + step) < 0:
                secantMethod(i, i + step, 10.0**precision, 0)
        elif method == CORD:
            #Cord Method
            if f(i) * f(i + step) < 0:
                cordMethod(i, i + step, 10.0**precision, 0)
        elif method == NEWTON:
            #Newtons Method
            if f(i) * f(i + step) < 0:
                newtonMethod (i+step, 10.0**precision)
        else:
            print("No such method")
    t = np.arange(start, end, 0.1)
    t1 = [ f(x) for x in t]
    
    plt.plot(t, t1, '-b')
    plt.plot([plotXStart, plotXEnd], [0, 0], '-k')
    plt.plot([0, 0], [plotYStart, plotYEnd], '-k')
    plt.plot(roots, [0 for x in range(len(roots))], 'or')
    plt.axis([plotXStart, plotXEnd, plotYStart, plotYEnd])
    plt.title(methods[method])
    plt.show() 
    
if __name__ == "__main__":
    main(NEWTON)  
