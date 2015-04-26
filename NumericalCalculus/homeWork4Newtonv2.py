from matplotlib import pyplot as plotter
from gmpy2 import mpfr as real
from math import factorial

divisionPoints = [ real(-1/3) , real(-1/5) , real(-1/10) , real(0) , real(1/10) , real(1/5) , real(1/3) ]

def domain(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def f(x):
    return real( 1 / (1 + 100*(x**2)) )
def division(x,n,h):
    result = real(0)
    for k in range(0,n):
        result += ((-1)**k) * (factorial(n)/(factorial(k)*factorial(n-k))) * f(x + (n-k) * h)
    return result
def dividedF(x,points,h):
    n = len(points)
    return real(division(x,n,h)/(factorial(n)*(h**n)))

a = -2
b = 2
start = -0.5
stop = 3.5
h = 0.5
step = 10**(-1)

plotter.axis([a,b,a,b])
plotter.plot([x for x in domain(a,b,step)],[0 for x in domain(a,b,step)],'b')
plotter.plot([0 for x in domain(a,b,step)],[x for x in domain(a,b,step)],'b')
plotter.plot([x for x in domain(a,b,step)],[f(x) for x in domain(a,b,step)],'g')

plotter.plot([x for x in domain(start,stop,step)],[dividedF(x,divisionPoints,h) for x in domain(a,b,step)],'r')
plotter.show()
