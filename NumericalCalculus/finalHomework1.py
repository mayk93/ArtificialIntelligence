import math
from gmpy2 import mpfr

def newMatrix(n):
    matrix = []
    for i in range(0,n+1):
        row = []
        for j in range(0,n+1):
            if i == 0 or j == 0:
                row.append(-1)
            else:
                row.append(mpfr(0))
        matrix.append(row)
    return matrix

def newVector(n):
    vector = []
    for i in range(0,n+1):
        if i == 0:
            vector.append(-1)
        else:
            vector.append(mpfr(0))
    return vector

def factorial(n):
    if n == 0 or n == 1:
        return 1
    f = mpfr(1)
    i = mpfr(2)
    while i < n+1:
        f = f*mpfr(i)
        i = i+1
    return f

def combinations(n,k):
    if n == 0 and k == 0:
        return mpfr(0)
    if n >= k:
        return factorial(n)/(factorial(n-k)*factorial(k))
    else:
        return mpfr(0)

def printMatrix(matrix):
    print("---------------")
    for rowIndex in range(0,len(matrix[0])):
        if rowIndex != 0:
            row = []
            for columnIndex in range(0,len(matrix[0])):
                if columnIndex != 0:
                    row.append(matrix[rowIndex][columnIndex])
            print(row)
    print("---------------")

def transposeMatrix(matrix):
    n = len(matrix[0])-1
    matrixT = newMatrix(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrixT[i][j] = matrix[j][i]
    return matrixT

def combinationMatrix(n,p):
    A = newMatrix(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(combinations(p+j,i) == None):
                print("Returned None for ",i,p)
            A[i][j] = combinations(p+j,i)
    return A

def getColumn(A,columnIndex):
    column = []
    for rowIndex in range(1,len(A[0])):
        column.append(A[rowIndex][columnIndex])
    return column

def vectorMultiplication(x,y):
    return sum([mpfr(xi*yi) for xi,yi in zip(x,y)])

def multiplyMatrix(X, Y):
    result = newMatrix(len(X[0])-1)
    for xRowIndex in range(1,len(X[0])):
        xRow = X[xRowIndex][1:]
        for yColumnIndex in range(1,len(Y[0])):
            yColumn = getColumn(Y,yColumnIndex)
            result[xRowIndex][yColumnIndex] = vectorMultiplication(xRow,yColumn)
    return result

def matrixVectorMultiplication(X, V):
    '''
    print("Matrix Vect")
    print("Matrix")
    print("Normmal MAtrix")
    print(X)
    print("Print Matrix")
    printMatrix(X)
    print("Vector")
    print(V)
    V = V[1:len(V)-1]
    print("New V:")
    print(V)
    '''

    result = []
    for rowIndex in range(0,len(V)):
        if rowIndex != 0:
            row = X[rowIndex]
            localResult = mpfr(0)
            for matrixElement,vectorElement in zip(row[1:],V[1:]):
                localResult = localResult + matrixElement*vectorElement
            result.append(localResult)
    return result

def vectorSubstraction(x,y):
    x = x[1:len(x)-1]
    return [mpfr(xi-yi) for xi,yi in zip(x,y)]

def LIPUPKsum(L,U,i,k):
    toReturnSum = mpfr(0)
    for p in range(1,k):
        toReturnSum = toReturnSum + L[i][p]*U[p][k]
    return toReturnSum

def LKPUPJsum(L,U,j,k):
    toReturnSum = mpfr(0)
    for p in range(1,k):
        toReturnSum = toReturnSum + L[k][p]*U[p][j]
    return toReturnSum

def LU(n,A,b):
    L = newMatrix(n)
    U = newMatrix(n)
    m = n+1
    for i in range(1,m):
        L[i][1] = A[i][1]
    U[1][1] = mpfr(1)
    for j in range(2,m):
        U[1][j] = A[1][j]/L[1][1]
    for k in range(2,m):
        for i in range(k,m):
            L[i][k] = A[i][k] - LIPUPKsum(L,U,i,k)
        U[k][k] = mpfr(1)
        for j in range(k+1,m):
            U[k][j] = (A[k][j] - LKPUPJsum(L,U,j,k))/L[k][k]
    return (L,U)

def freeTerms(A):
    b = newVector(len(A[0]))
    for i in range(1,len(A[0])):
        b[i] = mpfr(0)
        for j in range(1,len(A[0])):
            if(b[i] == None or A[i][j] == None):
                print("b[",i,"]:",b[i])
                print("A[",i,"][",j,"]:",A[i][j])
                print(A)
                printMatrix(A)
            b[i] = b[i] + A[i][j]
    return b

def printVector(V):
    print('-----')
    toPrint = []
    for i in range(1,len(V)-1):
        toPrint.append(V[i])
        #print(V[i])
    print(toPrint)
    print('-----')
    #return toPrint

def LIKYKsum(i,L,y):
    toReturnSum = mpfr(0)
    for k in range(1,i):
        toReturnSum += L[i][k]*y[k]
    return toReturnSum

def solveY(b,L):
    n = len(L[0])
    y = newVector(n-1)
    for i in range(1,n):
        y[i] = (b[i] - LIKYKsum(i,L,y))/L[i][i]
    return y

def UIKXKsum(i,U,x):
    toReturnSum = mpfr(0)
    for k in range(i+1,len(x)):
        toReturnSum = toReturnSum + U[i][k]*x[k]
    return toReturnSum

def solveX(y,U):
    n = len(y)
    x = newVector(n-1)
    for i in range(n-1,0,-1):
        #print(x[i])
        x[i] = y[i] - UIKXKsum(i,U,x)
    return x

def LJKsum(L,j):
    toReturnSum = mpfr(0)
    for k in range(1,j-1):
        toReturnSum = toReturnSum + L[j][k]**2
    return toReturnSum

def LIKLJKsum(L,i,j):
    toReturnSum = mpfr(0)
    for k in range(1,j-1):
        toReturnSum = toReturnSum + L[i][k]*L[j][k]
    return toReturnSum

def Cholesky(n,A,b):
    L = newMatrix(n)
    for j in range(1,n):
        for i in range(j+1,n):
            L[j][j] = math.sqrt( A[j][j] - LJKsum(L,j) )
            L[i][j] = ((A[i][j])-LIKLJKsum(L,i,j))/L[j][j]
    return (L,transposeMatrix(L))

def solveCholeskyY(b,L):
    n = len(L[0])
    y = newVector(n-1)
    for i in range(1,n):
        y[i] = (b[i] - LIKYKsum(i,L,y))/L[i][i]
    return y

def LKIXKsum(i,L,x,m):
    toReturnSum = mpfr(0)
    for k in range(i+1,m):
        toReturnSum = toReturnSum + L[i][k]*x[k]
    return toReturnSum

def solveCholeskyX(y,L):
    n = len(y)
    x = newVector(n-1)
    for i in range(n-1,0,-1):
        x[i] = (y[i] - LKIXKsum(i,L,x,n))/L[i][i]
    return x

def main():
    n = 5
    p = 2
    A = combinationMatrix(n,p)
    b = freeTerms(A)
    '''
    LU Method
    '''
    '''
    (L,U) = LU(n,A,b)
    y = solveY(b,L)
    x = solveX(y,U)
    printVector(vectorSubstraction(b,matrixVectorMultiplication(A,x)))
    '''
    '''
    Cholesky
    '''
    '''
    (L,Lp) = Cholesky(n,A,b)
    y = solveCholeskyY(b,L)
    x = solveCholeskyX(y,L)
    printVector(vectorSubstraction(b,matrixVectorMultiplication(A,x)))
    '''

if __name__ == "__main__":
    main()
