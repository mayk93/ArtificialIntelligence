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
        return 0
    if n >= k:
        return factorial(n)/(factorial(n-k)*factorial(k))

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
    matrixT = newMatrix(len(matrix[0]))
    for i in range(1,len(matrixT[0])):
        for j in range(1,len(matrixT[0])):
            matrixT[i][j] = matrix[j][i]
    return AT

def combinationMatrix(n,p):
    A = newMatrix(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i][j] = combinations(p+j,i)
    return A

def multiplyMatrix(X, Y):
    n = len(X[0])
    result = newMatrix(n-1)
    for i in range(1,n):
       for j in range(1,n):
           for k in range(1,n):
               result[i][j] += X[i][k] * Y[k][j]
    return result

def matrixVectorMultiplication(X, V):
    result = []
    for rowIndex in range(0,len(X)+1):
        if rowIndex != 0:
            row = X[rowIndex]
            localResult = mpfr(0)
            for matrixElement,vectorElement in zip(row[1:],V[1:]):
                localResult = localResult + matrixElement*vectorElement
            result.append(localResult)
    return result

def vectorSubstraction(x,y):
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
    U[1][1] = 1
    for j in range(2,m):
        U[1][j] = A[1][j]/L[1][1]
    for k in range(2,m):
        for i in range(k,m):
            L[i][k] = A[i][k] - LIPUPKsum(L,U,i,k)
    U[k][k] = 1
    for j in range(k+1,m):
        U[k][j] = (A[k][j] - LKPUPJsum(L,U,j,k))/L[k][k]
    return (L,U)

def main():
    n = 3
    p = 2
    b = []
    A = combinationMatrix(n,p)
    (L,U) = LU(n,A,b)
    printMatrix(A)
    printMatrix(multiplyMatrix(L,U))

if __name__ == "__main__":
    main()
