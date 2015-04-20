'''
Mandrescu Mihai Petru - 342
20.04.2015
'''
#Libraries
from gmpy2 import mpfr as largeNumber
from gmpy2 import sqrt as squareRoot
from time import time as currentTime

#Definitions
FACTORS = 0
TIME = 1
A = 2
X = 3
P = 0
Q = 1
LARGE_PRIME_FILE = "largePrime.txt"

#Class
class Factor:
    def __init__(self,N):
        self.N = N
        self.result = self.factor(N)
        self.factors = self.result[FACTORS]
        self.requiredTime = self.result[TIME]
        self.A = self.result[A]
        self.X = self.result[X]
        self.p = self.factors[P]
        self.q = self.factors[Q]
    def assign(self,p,q,A,x,startTime,endTime):
        return ((p,q),endTime-startTime,A,x)
    def factor(self,N):
        startTime = currentTime()
        A = largeNumber(0)
        possibleA = squareRoot(N)
        while A == largeNumber(0):
            x = squareRoot(possibleA**2 - N)
            possibleP = possibleA - x
            possibleQ = possibleA + x
            if possibleP*possibleQ == N:
                endTime = currentTime()
                return assign(possibleP,possibleQ,possibleA,x,startTime,endTime)
            else:
                possibleA += 1
    def display(self):
        print("=====")
        print("Factoring duration:",self.requiredTime)
        print("Large number to factor:",self.N)
        print("Factor p =",self.p)
        print("Factor q =",self.q)
        print("Found A =",self.A)
        print("Found x =",self.x)       
        print("=====")

#Functions
def readLargePrime(path):
    return largeNumber(open(path,'rb'))
def main():
    factor = Factor(readLargePrime(LARGE_PRIME_FILE))
    factor.display()
