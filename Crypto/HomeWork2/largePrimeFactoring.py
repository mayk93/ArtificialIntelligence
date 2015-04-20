'''
Mandrescu Mihai Petru - 342
20.04.2015
'''
#Libraries
from gmpy2 import mpfr as largeNumber
from gmpy2 import sqrt as squareRoot
from copy import deepcopy as new
from time import time as currentTime

#Definitions
FACTORS = 0
TIME = 1
P = 0
Q = 1

class Factor:
    def __init__(self,N):
        self.N = N
        self.result = self.factor(N)
        self.factors = self.result[FACTORS]
        self.requiredTime = self.result[TIME]
        self.p = self.factors[P]
        self.q = self.factors[Q]
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
