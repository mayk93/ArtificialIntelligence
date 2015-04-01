import copy
import matrix
from matrix import Matrix
from math import sqrt

def fillMatrix(matrixToFill):
    toReturn = copy.deepcopy(matrixToFill)
    for i in range(0,matrixToFill.numberOfRows):
        for j in range(0,matrixToFill.numberOfColumns):
            if i == j:
                toReturn.insert(i,j,2)
            elif i == j+1:
                toReturn.insert(i,j,1)
            elif j == i+1:
                toReturn.insert(i,j,1)
    return toReturn

def fillResultVector(vector):
    VECTOR = 0 # A vector can be seen as a matrix with one column ( or one row )
    toReturn = copy.deepcopy(vector)
    for i in range(0,vector.numberOfRows):
        toReturn.insert(i,VECTOR,1) #Here, I am telling the matrix API to insert '1' at [i,0], that is, form a single column matrix that will server as our vector.
    return toReturn

def computeYiSum(Bsigma,bsig,x,i,mathM):
    toReturn = 0
    for j in range(1,mathM):
        toReturn = toReturn + (Bsigma.mathAt(i,j) * x.mathAt(j,1) + bsig.mathAt(i,1))
    return copy.deepcopy(toReturn)

def computeErrSum(A,y,x,i,mathM):
    toReturn = 0
    for j in range(1,mathM):
        toReturn = toReturn + (A.mathAt(i,j) * (y.mathAt(j,1)-x.mathAt(j,1)) * (y.mathAt(i,1)-x.mathAt(i,1)))
    return (copy.deepcopy(toReturn))

def Jacobi(m,A,a,epsilon,p):
    '''
    The following 5 lines are not part of the algorithm per se. They are helpers.
    '''
    VECTOR = 1 # See above. Here, it is 1 because we use math notation
    nOptim = 0
    xOptim = Matrix(m,m)
    mathP = p+1 #We use mathP (p+1) because the algorithm is written in mathematical notation (k = 1,p). By employing the matrix API, we can directly use the mathematical notation
    mathM = m+1 #We use mathM for the same reason we use mathP. It is used only for iterations, not defining sizes

    ni = copy.deepcopy(A.infiniteNorm())
    for k in range(1,mathP):
        sigma = ((2*k)/((mathP+1)*ni))
        Bsigma = Matrix(m,m)

        '''
        Compute Bsigma Matrix
        '''
        for i in range(1,mathM):
            for j in range(1,mathM):
                if i == j:
                    Bsigma.mathInsert(i,j,(1-sigma*A.mathAt(i,i)))
                else:
                    Bsigma.mathInsert(i,j,(-sigma*A.mathAt(i,j)))
        '''
        Compute bsig vector
        '''
        bsig = Matrix(m,1)
        for i in range(1,mathM):
            bsig.mathInsert(i,VECTOR,(sigma*A.mathAt(i,VECTOR)))
        '''
        Initialize
        '''
        n = 0
        x = Matrix(m,1)
        '''
        Do while loop
        '''
        condition = True
        while condition:
            n = n + 1
            y = Matrix(m,1)
            for i in range(1,mathM):
                yi = copy.deepcopy(computeYiSum(Bsigma,bsig,x,i,mathM))
                y.mathInsert(i,VECTOR,yi)
                err = copy.deepcopy(sqrt( abs(computeErrSum(A,y,x,i,mathM)) ))
            for i in range(1,mathM):
                x.mathInsert(i,VECTOR,copy.deepcopy(y.mathAt(i,VECTOR)))
            condition = err < epsilon
        if k == 1:
            nOptim = copy.deepcopy(n)
            xOptim = copy.deepcopy(x)
        elif k>1:
            if n < nOptim:
                nOptim = copy.deepcopy(n)
                xOptim = copy.deepcopy(x)
        else:
            print("This should never be seen. If you see this, something is very, very wrong ...")
    print("===== Jacobi =====")
    print("Optim n:",nOptim)
    print("Optim solution (x):")
    x.display()
    print("Test:")
    result = A.multiplyMatrix(x)
    result.display()
    print("====================")

def computeAijYjSum(A,y,i):
    toReturn = 0
    for j in range(1,i-1):
        toReturn = toReturn + A.mathAt(i,j)*y.mathAt(j,1)
    return copy.deepcopy(toReturn)

def computeAijXjSum(A,x,i,mathM):
    toReturn = 0
    for j in range(i+1,mathM):
        toReturn = toReturn + A.mathAt(i,j)*x.mathAt(j,1)
    return copy.deepcopy(toReturn)

def computeGaussSiedelErrSum(A,y,x,mathM):
    toReturn = 0
    for i in range(1,mathM):
        for j in range(1,mathM):
            toReturn = toReturn + A.mathAt(i,j) * (y.mathAt(j,1)-x.mathAt(j,1)) * y.mathAt(i,1)-x.mathAt(i,1)
    return copy.deepcopy(toReturn)

def GaussSiedel(m,A,a,epsilon,p):
    '''
    The following 5 lines are not part of the algorithm per se. They are helpers.
    '''
    VECTOR = 1 # See above. Here, it is 1 because we use math notation
    nOptim = 0
    xOptim = Matrix(m,m)
    mathP = p+1 #We use mathP (p+1) because the algorithm is written in mathematical notation (k = 1,p). By employing the matrix API, we can directly use the mathematical notation
    mathM = m+1 #We use mathM for the same reason we use mathP. It is used only for iterations, not defining sizes

    for k in range(1,mathP):
        sigma = ((2*k)/(p+1))
        n = 0
        x = Matrix(m,VECTOR)
        condition = True
        while condition:
            n = n+1
            y = Matrix(m,1)
            for i in range(1,mathM):
                yi = ((1-sigma) * x.mathAt(i,VECTOR)) + (sigma/A.mathAt(i,i)*(a.mathAt(i,VECTOR)-computeAijYjSum(A,y,i) - computeAijXjSum(A,x,i,mathM)))
                y.mathInsert(i,VECTOR,yi)
            err = copy.deepcopy(sqrt(abs(computeGaussSiedelErrSum(A,y,x,mathM))))
            for i in range(1,mathM):
                x.mathInsert(i,VECTOR,(copy.deepcopy(y.mathAt(i,VECTOR))))
            condition = err < epsilon
        if k == 1:
            nOptim = copy.deepcopy(n)
            xOptim = copy.deepcopy(x)
        elif k>1:
            if n < nOptim:
                nOptim = copy.deepcopy(n)
                xOptim = copy.deepcopy(x)
        else:
            print("This should never be seen. If you see this, something is very, very wrong ...")
    print("===== Gauss Siedel =====")
    print("Optim n:",nOptim)
    print("Optim solution (x):")
    x.display()
    print("Test:")
    result = A.multiplyMatrix(x)
    result.display()
    print("====================")

def main():
    m = 10
    A = Matrix(m,m)
    A = copy.deepcopy(fillMatrix(A))
    a = Matrix(m,1)
    a = copy.deepcopy(fillResultVector(a))
    epsilon = 10**(-5)
    p = 10

    print("The matrix A:")
    A.display()
    Jacobi(m,A,a,epsilon,p)
    GaussSiedel(m,A,a,epsilon,p)

if __name__ == '__main__':
    main()
