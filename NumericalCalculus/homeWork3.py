import copy
import matrix
from matrix import Matrix

def fillMatrix(matrix):
    return None

def fillResultVector(vector):
    return None

def Jacobi(m,A,a,epsilon,p):
    pass

def main():
    m = 10
    A = Matrix(m,m)
    A = copy.deepcopy(fillMatrix(A))
    a = Matrix(m,1)
    a = copy.deepcopy(fillResultVector(a))
    epsilon = 10*(-5)
    p = 10
    Jacobi(m,A,a,epsilon,p)

if __name__ == '__main__':
    main()
