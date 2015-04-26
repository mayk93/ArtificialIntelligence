from math import sqrt

def function(x):
    return ( ((x**7)*(sqrt( abs(1-(x**2)) )))/( (2-x)**(13/2) ) )

def computeSumTrapeeze(k,function,a,h):
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
        sigma = h/2 * computeSumTrapeeze(k,f,a,h)
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

def computeSumSimpson(k,function,a,h):
    result = 0
    for i in range(0,k):
        result += ( function(a+(i-1)*h) + 4*function(a+(((2*i-1)*h)/2)) + function(a+i*h) )
    return result

def Simpson(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/6 * computeSumSimpson(k,f,a,h)
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

def computeSumNewton(k,function,a,h):
    result = 0
    for i in range(0,k):
        result += ( function(a+(i-1)*h) + 3*function(a+( ((3*i-2)*h)/3 )) + 3*function(a+( ((3*i-1)*h)/3 )) + function(a+i*h) )
    return result

def Newton(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/8 * computeSumNewton(k,f,a,h)
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

def computeSumBool(k,function,a,h):
    result = 0
    for i in range(0,k):
        result += 7*function(a+(i-1)*h) + 32*function(a+((4*i-3)*h)/4) + 12*function(a+(((2*i-1)*h)/2)) + 32*function(a+(((4*i-1)*h)/4)) + 7*function(a+i*h)
    return result

def Bool(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/90 * computeSumBool(k,f,a,h)
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

trapeezeMethod(-1,1,function,(10**(-5)))
Simpson(-1,1,function,(10**(-5)))
Newton(-1,1,function,(10**(-5)))
Bool(-1,1,function,(10**(-5)))
