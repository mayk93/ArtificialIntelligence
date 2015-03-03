import math
import numpy as np
import matplotlib.pyplot as plt

solutii = []

def f (x):
    return 1.0/2.0 + 1.0/4.0 * x**2 - x * math.sin(x) + 1.0/2.0 * math.cos(2 * x)
    #return x**3 +  4.0 * x**2 - 10.0
    #return math.sqrt(x**2 - 1)



def metoda_bisectiei (a, b, err, n):
    
    c = (a + b) / 2.0
    fa = f(a)
    fb = f(b)
    fc = f(c)
    if (fc == 0 or math.fabs(fc) < err):
        print ("c = " + str(c))
        print ("n:" + str(n))
        solutii.append(c)
        return
    elif (fa * fc < 0):
        metoda_bisectiei(a, c, err, n + 1)
    elif (fc * fb < 0):
        metoda_bisectiei(c, b, err, n + 1)


if __name__ == "__main__":
    
    for i in np.arange(-10, 10, 0.1):
        metoda_bisectiei(i, i + 0.1, 10.0**-10, 0)
        
    t = np.arange(-10, 10, 0.1)
    t1 = [ f(x) for x in t]
    plt.plot(t, t1, '-b')
    plt.plot([-10, 10], [0, 0], '-k')
    plt.plot([0, 0], [-10, 10], '-k')
    plt.plot(solutii, [0 for x in range(len(solutii))], 'or')
    plt.axis([-10, 10, -10, 10])
    plt.title('Metoda bisectiei')
    plt.show()   
    