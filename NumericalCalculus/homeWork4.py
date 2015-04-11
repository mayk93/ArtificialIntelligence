class System :
    def __init__(self):
        pass
    def systemValue(x):
        return list((firstEquation(x),secondEquation(x)))
    def firstEquation(x):
        return 7*(x[0]**3)-10*x[0]+7*x[1]-1
    def secondEquation(x):
        return 8*(x[1]**3)-11*x[1]+x[0]-1

class VectorOperations:
    def __init__(self):
        pass

class JacobiMatrix :
    def __init__(self):
        self.EPSILON = 10**(-5)
        this.system = System()
    def firstFunctionDerivativeRespX(x):
        return (system.firstEquation(List((x[0]+self.EPSILON,x[1])))-
                system.firstEquation(List((x[0],x[1]))))/self.EPSILON
    def firstFunctionDerivativeRespY(x):
        return (system.firstEquation(List((x[0],x[1]+self.EPSILON)))-
                system.firstEquation(List((x[0],x[1]))))/self.EPSILON
    def secondFunctionDerivativeRespX(x):
        return (system.secondEquation(List((x[0]+self.EPSILON,x[1])))-
                system.secondEquation(List((x[0],x[1]))))/self.EPSILON
    def secondFunctionDerivativeRespY(x):
        return (system.secondEquation(List((x[0],x[1]+self.EPSILON)))-
                system.secondEquation(List((x[0],x[1]))))/self.EPSILON
    def getJacobi(x,i,j):
        inverseDeterminant = firstFunctionDerivativeRespX(x) * secondFunctionDerivativeRespY(x) - firstFunctionDerivativeRespY(x) * secondFunctionDerivativeRespX(x)

        if i == 0 :
            if j == 0 :
                return secondFunctionDerivativeRespY(x)/inverseDetrminant
            elif j == 1 :
                return -firstFunctionDerivativeRespY(x)/inverseDeterminant
        elif i == 1 :
            if j == 0 :
                return -secondFunctionDerivativeRespX(x)/inverseDeterminant
            elif j == 1 :
                return firstFunctionDerivativeRespX(x)/inverseDeterminant

class Methods :
    def __init__(self):
        pass
    def newthonMethod(EPSILON,x):
        system = System()
        jacobi = Jacobi()
        while(abs(system.systemValue(x)[0])>EPSILON and
              abs(system.systemValue(x)[1])>EPSILON ):
              pass
