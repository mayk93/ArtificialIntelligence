import copy
import matplotlib.pyplot as plt

def firstEquation(x,y):
    return 7*(x**3) - 10*x - 7*y + 1
def firstEquationFunction(x):
    return x**3 - (10/7)*x + (1/7)
def secondEquation(x,y):
    return 8*(y**3) - 11*y + x - 1
def secondEquationFunction(x):
    return -8*(x**3) + 11*x + 1
def firstEquationDerivativeX(x,y):
    return 21*(x**2) - 10
def firstEquationDerivativeY(x,y):
    return -7
def secondEquationDerivativeX(x,y):
    return 1
def secondEquationDerivativeY(x,y):
    return 24*(y**2) - 11
def jacobi(x,y):
    matrix = [ firstEquationDerivativeX(x,y) , firstEquationDerivativeY(x,y) , secondEquationDerivativeX(x,y) , secondEquationDerivativeY(x,y) ]
    return copy.deepcopy(matrix)
def computeDeterminant(matrix):
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]
def invert(matrix):
    determinant = computeDeterminant(matrix)
    inverted = [ (matrix[3]/determinant) , -(matrix[1]/determinant) , -(matrix[2]/determinant) , (matrix[0]/determinant) ]
    return copy.deepcopy( inverted )
def systemValue(x,y):
    systemValue = [ firstEquation(x,y) , secondEquation(x,y) ]
    return copy.deepcopy(systemValue)
def matrixVectorMultiplication(matrix,vector):
    newVector = [ matrix[0] * vector[0] + matrix[1] * vector[1] , matrix[2] * vector[0] + matrix[3] * vector[1] ]
    return copy.deepcopy(newVector)
def vectorSubtraction(leftVector,rightVector):
    newVector = [ leftVector[0] - rightVector[0] , leftVector[1] - rightVector[1] ]
    return copy.deepcopy(newVector)
def condition(x,y,epsilon):
    return abs(systemValue(x,y)[0]) < epsilon and abs(systemValue(x,y)[1]) < epsilon
def newtonMethod(values,epsilon):
    while not condition(values[0],values[1],epsilon):
        newValues = copy.deepcopy( vectorSubtraction( values , matrixVectorMultiplication(invert(jacobi(values[0],values[1])),systemValue(values[0],values[1])) ) )
        values = copy.deepcopy(newValues)
    return copy.deepcopy(values)
def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
def almostIn(currentRoot,roots,epsilon):
    for root in roots:
        if abs(currentRoot[0] - root[0]) <= epsilon:
            return True
        if abs(currentRoot[1] - root[1]) <= epsilon:
            return True
    return False
def plot(roots):
    plt.plot([x for x in drange(-2,2,0.1)], [firstEquationFunction(x) for x in drange(-2,2,0.1)])
    plt.plot([x for x in drange(-2,2,0.1)], [secondEquationFunction(x) for x in drange(-2,2,0.1)],'r')
    plt.plot(roots,'g^')

    plt.axis([-3, 3, -3, 3])
    plt.xlabel('Function')
    plt.ylabel('Value')
    plt.show()
def problem1():
    step = 10**(-1)
    values = [0,0]
    epsilon = 10**(-5)
    roots = []
    for x in drange(-2,2,step):
        for y in drange(-2,2,step):
            currentRoot = newtonMethod([x,y],epsilon)
            if not almostIn(currentRoot,roots,10**(-1)):
                roots.append(currentRoot)
    plot(roots)
    print("Roots:",roots)
def f(x):
    return 1/(1+100*(x**2))
def problem2a(m,roots,a,b): # Lagrange
    n = len(roots)
    for k in range(0,m):
        z = a + ((b-a)/(m-1))*k
        polynomValue = 0
        for i in range(0,n):
            product = f(roots[i])
            denominator = 1 # Up
            nominator = 1   # Down
            for j in range(0,n):
                if i != j:
                    denominator *= (z - roots[j])
                    nominator *= (roots[i]-roots[j])
            product *= denominator/nominator
            polynomValue += product
        print("Polynom in ",z,":",polynomValue)
def problem2b(m,roots,a,b):
    n = len(roots)
    matrix = [[0 for x in range(n)] for x in range(n)]
    c = [0 for i in range(0,n)]
    for k in range(0,m):
        z = a + ((b-a)/(m-1))*k
        for i in range(0,n):
            matrix[i][0] = f(roots[i])
        c[0] = matrix[0][0]
        for i in range(1,n):
            for j in range(i,n):
                matrix[i][j] = (matrix[i-1][j] - matrix[i-1][j-1])/(roots[j]-roots[j-i])
            c[i] = matrix[i][i]
        #print("Matrix:",matrix)
        polynomValue = c[0]
        for i in range(1,n):
            product = c[i]
            for j in range(0,i):
                product *= (z - roots[j])
            polynomValue += product
        print("Polynom in",z,":",polynomValue)
def main():
    #pass
    problem1()
    #print(systemValue(-1.3054662227021259, -0.2170215531444045))
    #problem2a(20,[-1/3,-1/5,-1/10,0,1/10,1/5,1/3],-1.5,1.5)
    #problem2b(20,[-1/3,-1/5,-1/10,0,1/10,1/5,1/3],-1.5,1.5)

if __name__ == '__main__':
    main()
