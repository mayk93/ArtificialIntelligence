from gmpy2 import mpfr
from math import sqrt
from math import pi

def newEmptyMatrix(rows,columns):
    newMatrix = []
    for i in range(0,rows):
        newRow = []
        for j in range(0,columns):
            newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix

class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.matrix = newEmptyMatrix(rows,columns)

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
    def Add(self,x):
        b = Matrix(self.rows,self.columns)
        if self.rows == x.rows and self.rows == x.columns:
            for i in range(1,self.rows):
                for j in range(1,self.columns):
                    b.matrix[i][j] = self.matrix[i][j] + x.matrix[i][j]
        return b
    def multiplyMatrix(self,x):
    	b = Matrix(self.rows,self.columns)
    	if self.columns == x.rows:
    		for i in range(1,self.rows):
        		for j in range(1,x.columns):
        			b.matrix[i][j] = 0;
        			for k in range(1,self.columns):
        				b.matrix[i][j] += self.matrix[i][k] * x.matrix[k][j]

    	return b
    def multiplyScalar(self,x):
        b = Matrix(self.rows,self.columns)
        for i in range(1,self.rows):
            for j in range(1,self.columns):
                b.matrix[i][j] = self.matrix[i][j] * x
        return b
    def Substract(self,x):
    	b = Matrix(self.rows,self.columns)
    	if self.rows == x.rows and self.columns == x.columns:
    		for i in range(1,self.rows):
        		for j in range(1,self.columns):
        			b.matrix[i][j] = self.matrix[i][j] - x.matrix[i][j]
    	return b
    def Transpose(self):
        b = Matrix(self.rows,self.columns)
        for i in range(1,self.columns):
            for j in range(1,self.rows):
                b.matrix[i][j] = self.matrix[j][i];
        return b;
    def norma(self):
    	m = 0
    	for i in range(0,self.rows):
            mi = 0
            for j in range(1,self.columns):
                mi += abs(self.matrix[j][i]);
            if mi > m:
                m = mi
    	return m
    def getLength(self):
        maxNumerOfDigits = 0
        for row in self.matrix:
            currentNumberOfDigits = 0
            for number in row:
                currentNumberOfDigits = currentNumberOfDigits + len(str(number))
            if currentNumberOfDigits > maxNumerOfDigits:
                maxNumerOfDigits = currentNumberOfDigits
        return maxNumerOfDigits

'''
Variables
'''
m = 10
p = 10
eps = 10**(-10)
A = Matrix(m,m)
b = Matrix(m,1)
I = Matrix(m,m)

'''
Methods
'''
def JacobiMethod(p):
    i = 0
    j = 0
    t = mpfr(0)
    mi = mpfr(0)
    er = mpfr(0)
    sigma0 = mpfr(0)
    u0 = 0
    mi = A.norma()
    t = mpfr(2 / mi)

    B = Matrix(m,m)
    bs = Matrix(m,1)
    X = Matrix(m, 1)
    Y = Matrix(m, 1)
    X0 = Matrix(m, 1)

    for k in range(0,p): #Might be p
        sigma = t / (p + 1) * mpfr(k)
        As = Matrix(m,m)
        As = A.multiplyScalar(sigma);
        B = I.Substract(As);
        bs = b.multiplyScalar(sigma);
        u = 0;
        for i in range(0,m): #Might be m
            X.matrix[i][0] = 0;
        condition = True
        while condition:
            u += 1
            Y = X.multiplyMatrix(B)
            Y = Y.Add(bs)
            sum = mpfr(0)
            for i in range(0,m): #Might be m
                for j in range(0,m): #Might be m
                    sum += A.matrix[i][j] * (Y.matrix[j][0] - X.matrix[j][0])*(Y.matrix[i][0] - X.matrix[i][0])
            er = sqrt(sum)
            X = Y

            condition = (er > eps)

        if k == 1:
            u0 = u
            #X0 = X
            #print([element + 1 for element in row for row in X.matrix])
            X0.matrix = [[element + 1 for element in row] for row in X.matrix]
            sigma0 = sigma
        elif u < u0:
            u0 = u
            #X0 = X
            X0.matrix = [[element + 1 for element in row] for row in X.matrix]
            sigma0 = sigma
    print("\n ====================> Relaxed Jacobi Method <==================== \n")
    print("\n ===> Parametrul optim de relaxare:", sigma0)
    print("Solution:")
    X0.displayMatrix();
    print("\n ===> A * X0 - Test:")
    (X0.multiplyMatrix(A)).displayMatrix()

def main():
    i = 0
    j = 0
    for i in range(0,m): #Might be m
    	for j in range(0,m): #Might be m
            if i == j:
                A.matrix[i][j] = 2
            elif j == i + 1 or i == j + 1:
                A.matrix[i][j] = 1
            else:
                A.matrix[i][j] = 0
    for i in range(0,m): #Might be m
        b.matrix[i][0] = 1
    for i in range(0,m): #Might be m
    	for j in range(0,m): #Might be m
            if (i == j):
                I.matrix[i][j] = 1
            else:
                I.matrix[i][j] = 0
    print(b.matrix)
    JacobiMethod(p)
	#//metodaGaussSeidel(p);
	#//metodaGradientConjugat();

main()
