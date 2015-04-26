from math import sqrt

def function(x):
    return ( ((x**7)*(sqrt( abs(1-(x**2)) )))/( (2-x)**(13/2) ) )

def computeSum(k,function,a,h):
    result = 0
    for i in range(0,k):
        result += (function(a+((i-1)*h)) + function(a+i*h))
    return result

def trapeezeMethod(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/2 * computeSum(k,f,a,h)
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

trapeezeMethod(-1,1,function,(10**(-5)))
