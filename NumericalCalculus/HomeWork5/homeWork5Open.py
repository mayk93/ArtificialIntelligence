from math import sqrt
from math import e
from matplotlib import pyplot as plotter
from matplotlib import patches as plotName
from integralApproximation import *

PRECISION = 2
step = 10**(-1)

def domain(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def integralFunction(x):
    return (x**3)/((e**x - 1)+(10**(-5)))

def function(x,aproximationMethod):
    a = 0
    b = x
    f= integralFunction
    epsilon = (10**(-PRECISION))
    return 3*(x**(-3))*aproximationMethod(a,b,f,epsilon) if x != 0 else 3*aproximationMethod(a,b,f,epsilon)

def computeSumNewtonCotes2(k,function,a,h,aproximationMethod):
    result = 0
    for i in range(0,k):
        result += ( function(a+(((3*i-2)*h)/3),aproximationMethod) + function(a+(((3*i-1)*h)/3),aproximationMethod) )
    return result

def NewtonCotes2(a,b,f,epsilon,aproximationMethod):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/2 * abs(computeSumNewtonCotes2(k,f,a,h,aproximationMethod))
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S - Aria de sub grafic:",s)
    print("K - Numarul de iteratii necesare:",k)

def computeSumNewtonCotes4(k,function,a,h,aproximationMethod):
    result = 0
    for i in range(0,k):
        result += ( 11*function(a+(((5*i-4)*h)/5),aproximationMethod) + function(a+(((5*i-3)*h)/5),aproximationMethod) + function(a+(((5*i-2)*h)/5),aproximationMethod) + 11*function(a+(((5*i-1)*h)/5),aproximationMethod) )
    return result

def NewtonCotes4(a,b,f,epsilon,aproximationMethod):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/24 * abs(computeSumNewtonCotes4(k,f,a,h,aproximationMethod))
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S - Aria de sub grafic:",s)
    print("K - Numarul de iteratii necesare:",k)

def computeSumGauss3(k,function,a,b,h,aproximationMethod):
    result = 0
    for i in range(0,k):
        result += ( 5*function(a + ( ((2*i-1)*h)/2 ) - ( ((b-a)*sqrt(15))/(10*k+(0.0001)) ) , aproximationMethod) + 8*function(a+(((2*i-1)*h)/2),aproximationMethod) + 5*function(a + ( ((2*i-1)*h)/2 ) - ( ((b-a)*sqrt(15))/(10*k+(0.0001)) ) ,aproximationMethod) )
    return result

def Gauss3(a,b,f,epsilon,aproximationMethod):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/18 * abs(computeSumGauss3(k,f,a,b,h,aproximationMethod))
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S - Aria de sub grafic:",s)
    print("K - Numarul de iteratii necesare:",k)

a = -1
b = 1
f = function
epsilon = (10**(-PRECISION))

NewtonCotes2(a,b,f,epsilon,Bool)
NewtonCotes4(a,b,f,epsilon,trapeezeMethod)
Gauss3(a,b,f,epsilon,Newton)
