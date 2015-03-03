import numpy as np
import matplotlib.pyplot as plt
import math

solutii = []

def f (x):
    return 1.0/2.0 + 1.0/4.0 * x**2 - x * math.sin(x) + 1.0/2.0 * math.cos(2 * x)
    #return 1.0 / 5.0 * x**2 - 4
    #return x**3 +  4.0 * x**2 - 10.0

def setupPlot():
    t = np.arange(-10, 10, 0.01)
    t1 = [f(x) for x in t]
        
    plt.axis([-10, 10, -10, 10])
    plt.plot([-10, 10], [0, 0], '-k')
    plt.plot([0,0], [-10, 10], '-k')
        
    plt.plot(solutii, [0 for x in range(len(solutii))], 'or')
        
    plt.plot(t, t1, '-b')    
    plt.title('Metoda secantei')

def metoda_secantei(x0, x1, err, n):
    if n > 6:
        return
    
    
    fx0 = f(x0)
    fx1 = f(x1)
    
    xn = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
    fxn = f(xn)
    
    
    #setupPlot()
    #plt.plot([x0, x0], [0, fx0], ':c')
    #plt.plot([x1, x1], [0, fx1], ':c')
    #plt.plot([xn, xn], [0, fxn], ':c')
    #plt.plot([x0, x1], [fx0, fx1], '-y', [x0, x1], [0, 0], 'xb')
    #plt.plot([x0, x1], [fx0, fx1], 'ob', [xn], [fxn], 'or', [xn], [0], 'xr')
    #plt.show()
    
    
    if (math.fabs(fxn) < err) and (math.fabs(xn - x1) < err):
        solutii.append(xn)
        print("x:" + str(xn))
    else:
        metoda_secantei(x1, xn, err, n + 1)
    
    


if __name__ == '__main__':
    
    #metoda_coardei (-10, 10, 10**-2, 0)
    for x in np.arange(-10.0, 10.0, 0.5):
        if f(x) * f(x + 0.5) < 0:
            metoda_secantei (x, x + 0.5, 10.0**-10, 0)
        
    setupPlot()
    plt.show()
    