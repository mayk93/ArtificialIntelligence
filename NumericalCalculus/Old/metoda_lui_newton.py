import numpy as np
import matplotlib.pyplot as plt
import math

solutii = []

def f (x):
    return 1.0/2.0 + 1.0/4.0 * x**2 - x * math.sin(x) + 1.0/2.0 * math.cos(2 * x)
    #return 1.0 / 5.0 * x**2 - 4
    #return x**3 +  4.0 * x**2 - 10.0

def f_derivat(x):
    return 0.5 * x - x * math.cos(x) - math.sin(2 * x) - math.sin(x)

def setupPlot():
    t = np.arange(-10, 10, 0.01)
    t1 = [f(x) for x in t]
        
    plt.axis([-10, 10, -10, 10])
    plt.plot([-10, 10], [0, 0], '-k')
    plt.plot([0,0], [-10, 10], '-k')
        
    plt.plot(solutii, [0 for x in range(len(solutii))], 'or')
        
    plt.plot(t, t1, '-b')    
    plt.title('Metoda lui Newton')

def metoda_lui_newton(x0, err):
    
    fx0 = f(x0)
    
    xn = x0 - f(x0) / f_derivat(x0)
    fxn = f(xn)
    
    
    #setupPlot()
    #plt.plot([x0, x0], [0, fx0], ':c')
    #plt.plot([x1, x1], [0, fx1], ':c')
    #plt.plot([xn, xn], [0, fxn], ':c')

    #plt.plot([x0, x0 + 0.5], [0, 0], 'ob')
    #plt.plot([x0, x0 + 0.5], [fx0, f(x0+ 0.5)], 'xb')
    
    #plt.plot([xn], [fxn], 'or', [xn], [fxn], 'xr')
    #plt.show()
    
    
    if (math.fabs(fxn) < err) and (math.fabs(xn - x0) < err):
        solutii.append(xn)
        print("x:" + str(xn))
    else:
        metoda_lui_newton(xn, err)
    
    


if __name__ == '__main__':
    
    #metoda_coardei (-10, 10, 10**-2, 0)
    for x in np.arange(-10.0, 10.0, 0.5):
        if f(x) * f(x + 0.5) < 0:
            metoda_lui_newton (x+0.1, 10.0**-10)
        
    setupPlot()
    plt.show()
    