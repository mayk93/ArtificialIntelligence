import copy

class System :
    def __init__(self):
        pass
    def firstEquation(self,x):
        #return 7*(x[0]**3)-10*x[0]+7*x[1]-1
        return x[0]**3+x[1]-1
    def secondEquation(self,x):
        #return 8*(x[1]**3)-11*x[1]+x[0]-1
        return x[1]**3-x[0]+1
    def systemValue(self,x):
        return list((self.firstEquation(x),self.secondEquation(x)))

class VectorOperations:
    def __init__(self):
        pass

class JacobiMatrix :
    def __init__(self):
        self.EPSILON = 10**(-5)
        self.system = System()
        self.matrix = []
        self.invertedMatrix = []
    def firstFunctionDerivativeRespX(self,x):
        return (self.system.firstEquation(list((x[0]+self.EPSILON,x[1])))-
                self.system.firstEquation(list((x[0],x[1]))))/self.EPSILON
    def firstFunctionDerivativeRespY(self,x):
        return (self.system.firstEquation(list((x[0],x[1]+self.EPSILON)))-
                self.system.firstEquation(list((x[0],x[1]))))/self.EPSILON
    def secondFunctionDerivativeRespX(self,x):
        return (self.system.secondEquation(list((x[0]+self.EPSILON,x[1])))-
                self.system.secondEquation(list((x[0],x[1]))))/self.EPSILON
    def secondFunctionDerivativeRespY(self,x):
        return (self.system.secondEquation(list((x[0],x[1]+self.EPSILON)))-
                self.system.secondEquation(list((x[0],x[1]))))/self.EPSILON
    def getInverseJacobiComponent(self,x,i,j):
        inverseDeterminant = self.firstFunctionDerivativeRespX(x) * self.secondFunctionDerivativeRespY(x) - self.firstFunctionDerivativeRespY(x) * self.secondFunctionDerivativeRespX(x)
        if i == 0 :
            if j == 0 :
                return self.secondFunctionDerivativeRespY(x)/inverseDeterminant
            elif j == 1 :
                return -self.firstFunctionDerivativeRespY(x)/inverseDeterminant
        elif i == 1 :
            if j == 0 :
                return -self.secondFunctionDerivativeRespX(x)/inverseDeterminant
            elif j == 1 :
                return self.firstFunctionDerivativeRespX(x)/inverseDeterminant
    def computeMatrix(self,x):
        self.matrix.append(self.firstFunctionDerivativeRespX(x))
        self.matrix.append(self.firstFunctionDerivativeRespY(x))
        self.matrix.append(self.secondFunctionDerivativeRespX(x))
        self.matrix.append(self.secondFunctionDerivativeRespY(x))
    def computeInvertedMatrix(self,x):
        for i in range(0,2):
            for j in range(0,2):
                self.invertedMatrix.append(self.getInverseJacobiComponent(x,i,j))
    def multiply(self,x):
        '''
        toReturn = []
        toReturn.append(x[0] * self.getInverseJacobiComponent(x,0,0) +
                        x[1] * self.getInverseJacobiComponent(x,0,1))
        toReturn.append(x[0] * self.getInverseJacobiComponent(x,1,0) +
                        x[1] * self.getInverseJacobiComponent(x,1,1))
        return copy.deepcopy(toReturn)
        '''
        toReturn = []
        toReturn.append(x[0] * self.invertedMatrix[0] + x[1] * self.invertedMatrix[1])
        toReturn.append(x[0] * self.invertedMatrix[2] + x[1] * self.invertedMatrix[3])
        return copy.deepcopy(toReturn)

def substract(vector0,vector1):
    toReturn = []
    toReturn.append(vector0[0] - vector1[0])
    toReturn.append(vector0[1] - vector1[1])
    return copy.deepcopy(toReturn)

class Methods :
    def __init__(self):
        pass
    def newthonMethod(self,EPSILON,x):
        system = System()
        jacobi = JacobiMatrix()
        jacobi.computeMatrix(x)
        jacobi.computeInvertedMatrix(x)
        xn = copy.deepcopy(x)
        iteration = 0
        '''
        while(abs(system.systemValue(x)[0])>EPSILON or
              abs(system.systemValue(x)[1])>EPSILON ):
              print("First Eq is ",abs(system.systemValue(x)[0]))
              print("Second Eq is ",abs(system.systemValue(x)[1]))
              print("Epsilon is",EPSILON)
        '''
              #print(iteration)
        for i in range(0,5):
              #print("System:",system.systemValue(x))
              print("Xn at iteration:",iteration,".\n",x)
              #print("Jacobi:",jacobi.matrix)
              #print("Jacobi Inverse:",jacobi.invertedMatrix)
              multiplication = copy.deepcopy(jacobi.multiply(system.systemValue(x)))
              print("Multiplication:",multiplication)
              copy.deepcopy( substract(x,multiplication) )
              xn.append(x)
              iteration += 1
        print(xn)

def main():
    system = System()
    jacobi = JacobiMatrix()

    methods = Methods()
    epsilon = 10**(-5)
    x = [0,0]
    methods.newthonMethod(epsilon,x)
    #print("With epsilon:",system.systemValue([x[0]+epsilon,x[1]]))
    #print("Without epsilon:",system.systemValue([x[0],x[1]]))
    #print("Derivative:",jacobi.firstFunctionDerivativeRespY(x))

if __name__ == '__main__':
    main()
