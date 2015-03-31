'''
Numerical Calculus
Homework 3
'''
#Libraries
from gmpy2 import mpfr

#Variables
b = []

#Functions
"""
The function newEmptyMatrix(size)
will return a size x size 0 filled matrix.
"""
def newEmptyMatrix(rows,columns):
    newMatrix = []
    for i in range(0,rows):
        newRow = []
        for j in range(0,columns):
            newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix
def freeTerms(size):
    newB = []
    for i in range(0,size):
        newB.append(1)
    return newB
def check(listToCheck):
    index = 0
    for item in listToCheck:
        if item <= 0:
            return (True,index)
        else:
            index += index
    return (False,index)
#Classes
"""
This class with implement square matrices
"""
class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.matrix = newEmptyMatrix(rows,columns)
    '''
    The fillMatrix method will set the elements
    of the matrix to their appropriate values
    '''
    def fillMatrix(self):
        for i in range(0,self.rows):
            self.matrix[i][i]   = 2
            try:
                self.matrix[i][i+1] = 1
            except:
                pass
            try:
                self.matrix[i+1][i] = 1
            except:
                pass
    def testMatrix(self):
        for i in range(0,self.rows):
            for j in range(0,self.columns):
                self.matrix[i][j] = i*10+j
    '''
    The iterate will iterate over the matrix
    but with mathematical notation:
    1 through n would translate to 0 to n-1 ( both ends included )
    '''
    def iterate(self,rowStart,rowStop,columnStart,columnStop):
        checkTest,badIndex = check([rowStart,rowStop,columnStart,columnStop])
        if not checkTest:
            rowStart = rowStart-1
            rowStop  = rowStop
            columnStart = rowStart-1
            columnStop  = rowStop
            for i in range(rowStart,rowStop):
                for j in range(columnStart,columnStop):
                    print(str(self.matrix[i][j])+" ",end='')
                print("")
        else:
            print("Bad index:",badIndex)
            return -1
    def getLength(self):
        maxNumerOfDigits = 0
        for row in self.matrix:
            currentNumberOfDigits = 0
            for number in row:
                currentNumberOfDigits = currentNumberOfDigits + len(str(number))
            if currentNumberOfDigits > maxNumerOfDigits:
                maxNumerOfDigits = currentNumberOfDigits
        return maxNumerOfDigits
    def displayMatrix(self):
        LENGTH = self.getLength()
        for k in range(0,LENGTH+self.columns):
            print("=",end='')
        print("")
        for i in range(0,self.rows):
            for j in range(0,self.columns):
                print(str(self.matrix[i][j])+" ",end='')
            print("")
        for k in range(0,LENGTH+self.columns):
            print("=",end='')
        print("")
    def norma(self):
        m = mpfr(0)
        for i in range(1,self.rows):
            mi = mpfr(0)
            for j in range(1,self.columns):
                mi += abs(self.matrix[j][i]);
            if (mi > m):
                m = mi
        return m
    def multiply(self,x):
        b = Matrix(self.rows,self.columns)
        for i in range(1,self.rows):
            for j in range(1,self.columns):
                b.matrix[i][j] = self.matrix[i][j] * x
        return b
    def substract(self,x):
        b = Matrix(self.rows,self.columns)
        if self.rows == x.rows and self.columns == x.columns:
            for i in range(1,self.rows):
                for j in range(1,self.columns):
                    b.matrix[i][j] = self.matrix[i][j] - x.matrix[i][j];
            return b
    def add(self,x):
        b = Matrix(self.rows,self.columns)
        if self.rows == x.rows and self.columns == x.columns:
            for i in range(1,self.rows):
                for j in range(1,self.columns):
                    b.matrix[i][j] = self.matrix[i][j] + x.matrix[i][j];
            return b;
    def multiplyMatrix(self,x):
    	b = Matrix(self.rows,self.columns)
    	if self.columns == x.rows:
            for i in range(1,self.rows):
                for j in range(1,self.columns):
                    b.matrix[i][j] = 0
                    for k in range(1,self.columns):
                        try:
                            b.matrix[i][j] += self.matrix[i][k] * x.matrix[k][j];
                        except:
                            pass
            return b;

def metodaJacobi(A,m,p):
    i = 0
    j = 0
    u0 = 0
    t = mpfr(0)
    mi = mpfr(0)
    er = mpfr(0)
    sigma0 = mpfr(0)

    mi = A.norma()
    t = mpfr(2 / mi)

    B = Matrix(m,m)
    I = Matrix(m,m)
    b = Matrix(m,1)
    bs = Matrix(m,1)
    X = Matrix(m,1)
    Y = Matrix(m,1)
    Z0 = Matrix(m,1)

    for k in range(1,p): #Here might be p, not p+1
        sigma = mpfr(t / (p + 1) * mpfr(k))
        As = Matrix(m,m)
        As = A.multiply(sigma);
        B = I.substract(As);
        bs = b.multiply(sigma);
        u = 0;
        eps = mpfr(10**(-10))

        for i in range(i,m): #Here might be m, not pm+1
            X.matrix[i][0] = 0
        while er > eps:
            u += 1
            Y = B.multiply(X)
            Y = Y.add(bs)
            sum = mpfr(0)
            for i in range(i,m): #Here might be m, not pm+1
                for j in range(j,m): #Here might be m, not pm+1
                    sum += A.matrix[i][j] * (Y.matrix[j][1] - X.matrix[j][1])*(Y.matrix[i][1] - X.matrix[i][1])
            er = sqrt(sum);
            X = Y;
        if k == 1:
            u0 = u
            X0 = X
            sigma0 = sigma
        elif u < u0:
            u0 = u
            X0 = X
            sigma0 = sigma
    print("\n ====================> Relaxed Jacobi Method <==================== \n")
    print("\n ===> Parametrul optim de relaxare:", sigma0)
    print("\n ===> Iterations:",u0)
    print("Solution:")
    X0.displayMatrix();
    print("\n ===> A * X0 - Test:")
    (A.multiplyMatrix(X0)).displayMatrix()

#Main
def main():
    m = 10
    p = 10
    A = Matrix(m,m)
    A.fillMatrix()
    A.displayMatrix()
    metodaJacobi(A,m,p)

if __name__ == '__main__':
    main()
