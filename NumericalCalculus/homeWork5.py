from math import sqrt
from math import e

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
    '''
    If bool shows nothing, decomment this
    '''
    #print("S:",s)
    #print("K:",k)
    return s

trapeezeMethod(-1,1,function,(10**(-5)))
Simpson(-1,1,function,(10**(-5)))
Newton(-1,1,function,(10**(-5)))
Bool(-1,1,function,(10**(-5)))

print('--- >>> <<< ---')

def integralFunction(x):
    return (x**3)/(e**3 - 1)

def otherFunction(x):
    return 3*(x**(-3))*Bool(0,x,integralFunction,(10**(-3)))

def otherFunction2(x):
    y = x**(-3) if x != 0 else 0
    return 3*(y)*Bool(0,x,integralFunction,(10**(-3)))

def computeSumNewtonCotes2(k,function,a,h):
    result = 0
    for i in range(0,k):
        result += ( function(a+(((3*i-2)*h)/3)) + function(a+(((3*i-1)*h)/3)) )
    return result

def NewtonCotes2(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/2 * abs(computeSumNewtonCotes2(k,f,a,h))
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

def computeSumNewtonCotes4(k,function,a,h):
    result = 0
    for i in range(0,k):
        result += ( 11*function(a+(((5*i-4)*h)/5)) + function(a+(((5*i-3)*h)/5)) + function(a+(((5*i-2)*h)/5)) + 11*function(a+(((5*i-1)*h)/5)) )
    return result

def NewtonCotes4(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/24 * abs(computeSumNewtonCotes4(k,f,a,h))
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

def computeSumGauss3(k,function,a,b,h):
    result = 0
    for i in range(0,k):
        result += ( 5*function(a + ( ((2*i-1)*h)/2 ) - ( ((b-a)*sqrt(15))/(10*k+(0.0001)) ) ) + 8*function(a+(((2*i-1)*h)/2)) + 5*function(a + ( ((2*i-1)*h)/2 ) - ( ((b-a)*sqrt(15))/(10*k+(0.0001)) ) ) )
    return result

def Gauss3(a,b,f,epsilon):
    k = 1
    s = 0
    condition = True
    while condition:
        h = ((b-a)/k)
        sigma = h/18 * abs(computeSumGauss3(k,f,a,b,h))
        error = abs(sigma-s)
        s = sigma
        k += 1
        condition = error > epsilon
    print("S:",s)
    print("K:",k)

NewtonCotes2(-1,1,otherFunction,(10**(-5)))
NewtonCotes4(-1,1,otherFunction,(10**(-5)))
Gauss3(-1,1,otherFunction2,(10**(-5)))
