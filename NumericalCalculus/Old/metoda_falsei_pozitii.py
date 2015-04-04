import numpy as np
import matplotlib.pyplot as plt
import math

solutii = []

def f (x):
    return 1.0/2.0 + 1.0/4.0 * x**2 - x * math.sin(x) + 1.0/2.0 * math.cos(2 * x)
    #return 1.0 / 5.0 * x**2 - 4

t = np.arange(-10, 10, 0.1)
t1 = [f(x) for x in t]
    

def metoda_falsei_pozitii (a, b, err, n):
    fa = f(a)
    fb = f(b)
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)
    
    #plt.axis([-10, 10, -10, 10])
    #plt.plot([-10, 10], [0, 0], '-k')
    #plt.plot([0, 0], [-10, 10], '-k')
    #plt.plot([a, b], [fa, fb], '-g')
    #plt.plot([a, a], [0, fa], ':c')
    #plt.plot([b, b], [0, fb], ':c')
    #plt.plot([c, c], [0, fc], ':c')
    #plt.plot(t, t1, '-b')
    #plt.plot([a, b, c], [fa, fb, fc], 'oy')
    #plt.plot([a, b, c], [0, 0, 0], '*b')
    #plt.title('Metoda falsei pozitii')
    #plt.show()
    
    if a <= c and c <= b:
        if (fc == 0 or math.fabs(fc) < err) :
            solutii.append(c)
            print ("c: " + str(c))
            print ("n:" + str(n))
        elif fa * fc < 0:
            metoda_falsei_pozitii (a, c, err, n + 1)
        elif fc * fb < 0:
            metoda_falsei_pozitii (c, b, err, n + 1)



if __name__ == '__main__':

    for i in np.arange(-10, 10, 0.1):
        metoda_falsei_pozitii (i, i + 0.1, 10**-10, 0)
    
    t = np.arange(-10, 10, 0.1)
    t1 = [f(x) for x in t]
    
    plt.axis([-10, 10, -10, 10])
    plt.plot([-10, 10], [0, 0], '-k')
    plt.plot([0, 0], [-10, 10], '-k')
    plt.plot(t, t1, '-b')
    plt.plot(solutii, [0 for x in range(len(solutii))], 'or')
    plt.title('Metoda falsei pozitii')
    plt.show()   
    
    