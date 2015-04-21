'''
Mandrescu Mihai Petru - 342
20.04.2015
'''
#Libraries
from gmpy2 import mpfr as largeNumber
from gmpy2 import sqrt as squareRoot
from time import time as currentTime
import gmpy2
gmpy2.get_context().precision=2500

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
        self.x = self.result[X]
        self.p = self.factors[P]
        self.q = self.factors[Q]
    def assign(self,p,q,A,x,startTime,endTime):
        return ((p,q),endTime-startTime,A,x)
    def factor(self,N):
        startTime = currentTime()
        possibleA = largeNumber(squareRoot(N))
        condition = True
        iteration = 0
        while condition:
            x = largeNumber(squareRoot(possibleA**2 - N))
            possibleP = possibleA - x
            possibleQ = possibleA + x

            #Debug
            '''
            print("---")
            print("Iteration:",iteration)
            print("possibleA:",str(possibleA))
            print("x:",x)
            print("possibleP:",str(possibleP))
            print("possibleQ:",str(possibleQ))
            print("Match:",str(largeNumber(possibleP*possibleQ)),"out of",N," --- Approximately",( largeNumber(largeNumber(possibleP*possibleQ)/N) )*100,"%")
            print("---")
            '''

            if possibleP*possibleQ == N:
                endTime = currentTime()
                condition = False
                return self.assign(possibleP,possibleQ,possibleA,x,startTime,endTime)
            else:
                possibleA += 1
                iteration += 1
    def display(self):
        print("=====")
        print("Factoring duration:",self.requiredTime)
        print("Large number to factor:",str(self.N))
        print("Factor p =",str(self.p))
        print("Factor q =",str(self.q))
        print("Found A =",str(self.A))
        print("Found x =",str(self.x))
        print("=====")

#Functions
def readLargePrime(path):
    largeNumberString = str((open(path,'rb').read()[:-2]).decode('utf-8'))
    return largeNumber(largeNumberString)
def main():
    factor = Factor(readLargePrime(LARGE_PRIME_FILE))
    #print(factor.p*factor.q)
    #print("----------")
    #print(largeNumber("327129389200956126794095202524923785038454884683880522683709156864173831685771907189723431987003055251536169657445398288389316631638599681249535441516671785722333533442730165267083018.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999385243800652649477309732749288685698384060403559849629018968111593048047925352128042324734689158076991973429018592886264922605359439222928240201201222876217200683662146436935573744285348762811802646552391922550105555035120219999746034681683195222930020296595949353561725779923431198642646317387954744171550035840427494675954033349576897679686868324404697631983591819719626179151305656574939074103")*largeNumber("327129389200956126794095202524923785038454884683880522683709156864173831685771907189723431987003055251536169657445398288389316631638599681249535441516671785722333533442730165267083018.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999385243800652649477309732749288685698384060403559849629018968111593048047925352128042324734689158076991973429018592886264922605359439222928240201201222876217200683662146436935573744285348762811802646552391922550105555035120219999746034681683195222930020296595949353561725779923431198642646317387954744171550035840427494675954033349576897679686868324404697631983591819719626179151305656574939074103"))
    factor.display()
    #print("----------")
    #print(readLargePrime(LARGE_PRIME_FILE))
if __name__ == "__main__":
    main()
