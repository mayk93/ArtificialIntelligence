from matplotlib import pyplot as plotter
from functools import reduce
from gmpy2 import mpfr as real

def domain(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

division = [real(-1/3),real(-1/5),real(-1/10),real(0),real(1/10),real(1/5),real(1/3)]

def f (x):
    return 1/(1+100*(x**2))
def deltaF (x,h):
    return f(x+h) - f(x)
def deltaFn (x,h,n):
    result = x
    for iteration in range(0,n):
        result += deltaF(result,h)
    return result
def leftDeltaF (x,h):
    return f(x) - f(x+h)
def leftDeltaFn (x,h,n):
    result = x
    for iteration in range(0,n):
        result += leftDeltaF(result,h)
    return result

def computeCurrentResult(currentPoint,currentPointIndex,points):
    return (f(currentPoint)/(reduce(lambda x, y: x*y, [(currentPoint-xi) for xi,xiindex in enumerate(points) if currentPointIndex != xiindex])))
def nthOrderDivision(points):
    return sum( [ computeCurrentResult(currentPoint,currentPointIndex,points) for currentPoint,currentPointIndex in enumerate(points) ] )
def newtonInterpolationPolynom(x,points):
    result = f(x) + nthOrderDivision(points[:1])*(x-division[0]) + nthOrderDivision(points[:2])*(x-division[0])*(x-division[1]) + nthOrderDivision(points[:3])*(x-division[0])*(x-division[1])*(x-division[2]) + nthOrderDivision(points[:4])*(x-division[0])*(x-division[1])*(x-division[2])*(x-division[3]) + nthOrderDivision(points[:5])*(x-division[0])*(x-division[1])*(x-division[2])*(x-division[3])*(x-division[4]) + nthOrderDivision(points[:6])*(x-division[0])*(x-division[1])*(x-division[2])*(x-division[3])*(x-division[4])*(x-division[5])

a = -2
b = 2
h = 1
step = 10**(-1)

zeroOrderDivision = [f(x) for x in division]

plotter.axis([a,b,a,b])
plotter.plot([x for x in domain(a,b,step)],[0 for x in domain(a,b,step)],'b')
plotter.plot([0 for x in domain(a,b,step)],[x for x in domain(a,b,step)],'b')
plotter.plot([x for x in domain(a,b,step)],[f(x) for x in domain(a,b,step)],'g')

plotter.plot([x for x in domain(a,b,step)],[newtonInterpolationPolynom(x,division) for x in domain(a,b,step)],'r')
plotter.show()
