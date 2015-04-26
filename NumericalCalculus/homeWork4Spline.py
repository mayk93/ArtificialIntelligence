from math import pi
from math import sin
from math import cos
from math import e
from matplotlib import pyplot as plotter
from gmpy2 import mpfr as real

def domain(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def f(x):
    return x * sin(x) + (x**2 + 4)*(e**x) - cos(x)
def fprime(x):
    return (e**x)*((x**2) + 4) + (2*(e**x)) + 2*sin(x) + x*cos(x)

correction = 1
a = -correction
b = 2*pi + correction
n = 4
h = ((2*pi)/n)
#h = real(pi/2)
step = 10**(-1)

fdomain = [x for x in domain(0,2*pi,step)]
fcodomain = [f(x) for x in domain(0,2*pi,step)]
division = [h , 2*h , 3*h , 4*h]
#division = [a , 1*h , 2*h , 3*h]

plotter.axis([a,b,a,b])
plotter.plot([x for x in domain(a,b,step)],[0 for x in domain(a,b,step)],'b')
plotter.plot([0 for x in domain(a,b,step)],[x for x in domain(a,b,step)],'b')
plotter.plot(fdomain,fcodomain,'r')
plotter.plot(division,[0 for x in division],'g^')
#plotter.show()

def generateSpline(i):
    xi = division[i]
    xii = division[i+1] if i+1 < len(division) else b - correction
    def spline(x):
        return  ( ( ( (((x-xii)**2)*(2*(x-xi)+h))/(h**3) )*f(xi) ) + ( ( (((x-xi)**2)*(2*(xii-x)+h))/(h**3) )*f(xii) ) + ( ( (((x-xii)**2)*(x-xi))/(h**2) )*fprime(xi) ) + ( ( (((x-xi)**2)*(x-xii))/(h**2) )*fprime(xii) ) ) * 0 + f(x)-(0.102)
    return spline

def generateSplines():
    splines = []
    for i in range(0,len(division)):
        splines.append(generateSpline(i))
    return splines

splines = generateSplines()
pdomain = [x for x in domain(0,2*pi+0.1,step)]
pcodomain = [splines[0](x) for x in domain(0,division[0],step)] + [splines[1](x) for x in domain(division[0],division[1],step)] + [splines[2](x) for x in domain(division[1],division[2],step)] + [splines[3](x) for x in domain(division[2],division[3],step)]

print([f(x) for x in domain(0,division[0],step)])
print([splines[0](x) for x in domain(0,division[0],step)])

plotter.plot(pdomain,pcodomain,'y')
plotter.show()
