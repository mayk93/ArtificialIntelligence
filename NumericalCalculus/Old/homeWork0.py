import math
import statistics

e = math.e

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def f(x):
    return 3 - e**(sin(2*(x**2)) + cos(x**2))

def fPrime(x):
    return (- e**(sin(2*(x**2)) + cos(x**2)))*(4*x*cos(2*(x**2))-2*x*sin(x**2))

def stop(a,b,m,error):
    return True if ((b-a)/(2**m))<m else False

def bisection(a,b,error):
    an = []
    bn = []
    cn = []
    an.append(a)
    bn.append(b)
    cn.append( statistics.mean([a,b]) ) # This is c0

    m = 0
    n = 0
    while not stop(an[n],bn[n],m,error):
        if n > 0:
            if f(cn[n-1]) == 0:
                return c[n-1]
            if f(cn[n-1]) < 0:
                an.append(a[n-1])
                
    
def main():
    bisection()

if __name__ == "__main__":
    main()
