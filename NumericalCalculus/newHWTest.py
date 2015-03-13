import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc

PRECISION = 10**-14

def combinationMatrix(n,p):
    A = newMatrix(n)
    for i in range(0,n):
        for j in range(1,n):
            A[i][j] = combinations(p+j,i)
    return A

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

def printMatrix(matrix):
    print("---------------")
    for row in matrix:
        print(row)
    print("---------------")

def factorial(n):
    f = mpfr(1)
    i = mpfr(2)
    while i < n+1:
        f = f*mpfr(i)
        i = i+1
    return f

def combinations(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def transposeMatrix(A):
    AT = newMatrix(len(A[0]))
    for i in range(0,len(AT[0])):
        for j in range(0,len(AT[0])):
            AT[i][j] = A[j][i]
    return AT

def freeTerms(A):
    b = newVector(len(A[0]))
    for i in range(0,len(A[0])):
        b[i] = mpfr(0)
        for j in range(0,len(A[0])):
            b[i] = b[i] + A[i][j]
    return b

def multiplyMatrix(X, Y):
    result = newMatrix(len(X[0]))
    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    return result

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
                '''
                print("LIP = ",L[i][p])
                print("UPK = ",U[p][k])
                '''
                LIKsum = LIKsum + mpfr(L[i][p]*U[p][k])
            '''
            print("##########")
            print("A[i][k] =",A[i][k])
            print("LIKsum =",LIKsum)
            print("L[i][k] =",A[i][k]+LIKsum)
            print("##########")
            '''
            L[i][k] = A[i][k] - LIKsum
        U[k][k] = mpfr(1)
        for j in range(k+1,n):
            UKJsum = mpfr(0)
            for p in range(0,k):
                '''
                print("LKP = ",L[k][p])
                print("UPJ = ",U[p][j])
                '''
                UKJsum = UKJsum + L[k][p]*U[p][j]
            '''
            print("##########")
            print("A[k][j] =",A[k][j])
            print("UKJsum =",UKJsum)
            print("L[k][k] =",L[k][k])
            print("U[k][j] =",(A[k][j]-UKJsum)/L[k][k])
            print("##########")
            '''
            if L[k][k] == 0:
                L[k][k] = mpfr(PRECISION)
            U[k][j] = (A[k][j] - UKJsum)/L[k][k]
    return(L,U)

def calculateX(b,L,U,n):
    x = newVector(n)
    y = newVector(n)
    for i in range(0,n):
        LIKYKsum = mpfr(0)
        for k in range(0,i-1):
            LIKYKsum = LIKYKsum + L[i][k]*y[k]
        y[i] = (b[i] - LIKYKsum)/L[i][i]
    for i in range(n-1,-1,-1):
        UIKXKsum = mpfr(0)
        for k in range(i,n-1):
            UIKXKsum = UIKXKsum + U[i][k]*x[k]
        x[i] = y[i]-UIKXKsum
    return x

def matrixVectorMultiplication(X, V):
    result = []
    for row in X:
        localResult = mpfr(0)
        for matrixElement,vectorElement in zip(row,V):
            localResult = localResult + matrixElement*vectorElement
        result.append(localResult)
    return result

def main():
    n = 5
    p = 3
    A = combinationMatrix(n,p)
    b = freeTerms(A)
    (L,U) = LU(n,A,b)
    #printMatrix(A)
    #printMatrix(multiplyMatrix(L,U))
    print(b)
    x = calculateX(b,L,U,n)
    print(matrixVectorMultiplication(A,x))

if __name__ == "__main__":
    main()
