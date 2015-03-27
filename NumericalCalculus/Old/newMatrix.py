import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc
import math

PRECISION = 10**-13

def newMatrix(n):
    matrix = []
    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(mpfr(0))
        matrix.append(row)
    return matrix

def newVector(n):
    vector = []
    for i in range(0,n):
        vector.append(mpfr(0))
    return vector

def factorial(n):
    f = mpfr(1)
    i = mpfr(2)
    while i < n+1:
        f = f*mpfr(i)
        i = i+1
    return f

def combinations(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def printMatrix(matrix):
    print("---------------")
    for row in matrix:
        print(row)
    print("---------------")

def transposeMatrix(A):
    AT = newMatrix(len(A[0]))
    for i in range(0,len(AT[0])):
        for j in range(0,len(AT[0])):
            AT[i][j] = A[j][i]
    return AT

def combinationMatrix(n,p):
    A = newMatrix(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i-1][j-1] = combinations(p+j,i)
    return A

def multiplyMatrix(X, Y):
    result = newMatrix(len(X[0]))
    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    return result

def matrixVectorMultiplication(X, V):
    result = []
    for row in X:
        localResult = mpfr(0)
        for matrixElement,vectorElement in zip(row,V):
            localResult = localResult + matrixElement*vectorElement
        result.append(localResult)
    return result

def vectorSubstraction(x,y):
    return [mpfr(xi-yi) for xi,yi in zip(x,y)]

def freeTerms(A):
    b = newVector(len(A[0]))
    for i in range(0,len(A[0])):
        b[i] = mpfr(0)
        for j in range(0,len(A[0])):
            b[i] = b[i] + A[i][j]
    return b
'''
LU Method
'''
def LU(n,A,b):
    L = newMatrix(n)
    U = newMatrix(n)

    for i in range(0,n):
        L[i][0] = A[i][0]
    U[0][0] = mpfr(1)
    for j in range(1,n):
        U[0][j] = A[1][j]/L[1][1]

    for k in range(0,n):
        for i in range(k,n):
            LIKsum = mpfr(0)
            for p in range(0,k):
                LIKsum = LIKsum + mpfr(L[i][p]*U[p][k])
            L[i][k] = A[i][k] - LIKsum
        U[k][k] = mpfr(1)
        for j in range(k+1,n):
            UKJsum = mpfr(0)
            for p in range(0,k):
                UKJsum = UKJsum + L[k][p]*U[p][j]
            if L[k][k] == 0:
                L[k][k] = mpfr(PRECISION)
            U[k][j] = (A[k][j] - UKJsum)/L[k][k]
    return(L,U)

def calculateX_LU(n,b,L,U):
    y = newVector(n)
    for i in range(0,n):
        LIKYK = mpfr(0)
        for k in range(0,i):
            LIKYK = LIKYK + L[i][k]*y[k]
        y[i] = (b[i] - LIKYK)/L[i][i]
    x = newVector(n)
    for i in range(n-1,-1,-1):
        UIKXK = mpfr(0)
        for k in range(i,n):
            UIKXK = U[i][k]*x[k]
        x[i] = y[i]-UIKXK
    return x
'''
Cholesky Method
'''
def Cholesky(n,A,b):
    for j in rannge(0,n):
        for i in range(i+1,n):
            LJK = mpfr(0)
            LIK = mpfr(0)
            for k in range(0,j):
                LJK = LJK + L[j][k]**2
                LIK = LIK + L[i][k]*L[j][k]
            L[j][j] = sqrt(A[j][j]-LJK)/L[j][j]
    return L

def calculateX_CH(n,b,L):
    y = newVector(n)
    for i in range(0,n):
        LIKYK = mpfr(0)
        for k in range(0,i):
            LIKYK = LIKYK + L[i][k]*y[k]
        y[i] = (b[i] - LIKYK)/L[i][i]
    x = newVector(n)
    for i in range(n-1,-1,-1):
        LKI = mpfr(0)
        for k in range(i+1,n):
            LKI = LKI + L[k][i]*x[k]
        x[i] = (y[i]-LKI)/L[i][i]
    return x
'''
QR Method
'''
def QR(n,A,b):
    Q = newMatrix(n)
    R = newMatrix(n)
    aSum = mpfr(0)
    for i in range(0,n):
        aSum = aSum + A[i][1]**2
    R[1][1] = math.sqrt(aSum)
    for i in range(0,n):
        Q[i][1] = A[i][1]/R[1][1]
    for k in range(1,n):
        for j in range(0,k-1):
            AIKQIJ = mpfr(0)
            for i in range(0,n):
                AIKQIJ = AIKQIJ + A[i][k]*Q[i][j]
            R[j][k] = AIKQIJ
        A2IK = mpfr(0)
        R2IK = mpfr(0)
        for i in range(0,n):
            A2IK = A[i][k]**2
        for i in range(0,k-1):
            R2IK = R[i][k]**2
        R[k][k] = math.sqrt(abs(A2IK-R2IK))
        for i in range(0,n):
            RJKQIJ = mpfr(0)
            for j in range(0,k-1):
                RJKQIJ = RJKQIJ + R[j][k]*Q[i][j]
            Q[i][k] = mpfr(1/R[k][k])*(A[i][k]-RJKQIJ)
    return (Q,R)

def calculateX_QR(n,b,Q,R):
    y = newVector(n)
    for i in range(0,n):
        QJIBJ = mpfr(0)
        for j in range(0,n):
            QJIBJ = QJIBJ + Q[j][i]*b[j]
        y[i] = QJIBJ
    x = newVector(n)
    x[n-1] = y[n-1]/R[n-1][n-1]
    for i in range(n-2,-1,-1):
        RIJXJ = mpfr(0)
        for j in range(i+1,n):
            RIJXJ = RIJXJ + R[i][j]*x[j]
        x[i] = mpfr(1/R[i][i])*(y[i]-RIJXJ)
    return x

def main():
    n = 20
    p = 10
    A = combinationMatrix(n,p)
    b = freeTerms(A)
    (L,U) = LU(n,A,b)
    printMatrix(A)
    printMatrix(multiplyMatrix(L,U))

if __name__ == "__main__":
    main()
