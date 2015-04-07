import copy

def zeroMatrix(numberOfRows,numberOfColumns):
    zeroMatrix = []
    for row in range(0,numberOfRows):
        for column in range(0,numberOfColumns):
            zeroMatrix.append(Element(row,column,0))
    return zeroMatrix

def identityMatrix(numberOfRows,numberOfColumns):
    zeroMatrix = []
    for row in range(0,numberOfRows):
        for column in range(0,numberOfColumns):
            if row == column:
                zeroMatrix.append(Element(row,column,1))
            else:
                zeroMatrix.append(Element(row,column,0))
    return zeroMatrix

'''
The method 'multiplyAndAdd' takes two lists as arguments.
These lists are usually rows and columns of matrices
The method ensures they are of equal length and if they are,
it will sum the multiplication of each corresponding element.
This method is used to compute the multiplication of two matrices.
'''
def multiplyAndAdd(list0,list1):
    result = 0
    if len(list0) == len(list1):
        for element0, element1 in zip(list0,list1):
            result = result + element0*element1
        return result
    else:
        print("Bad lengths in 'multiplyAndAdd' method.")
        return None

def sameSize(matrix0,matrix1):
    if matrix0.numberOfRows != matrix1.numberOfRows:
        return False
    if matrix0.numberOfColumns != matrix1.numberOfColumns:
        return False
    return True

class Element():
    def __init__(self,rowNumber,columnNumber,value):
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.value = value

class Matrix:
    def __init__(self,numberOfRows,numberOfColumns):
        self.numberOfElements = numberOfRows * numberOfColumns
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.matrix = zeroMatrix(self.numberOfRows,self.numberOfColumns)
    def at(self,row,column):
        if row >= 0 and column >= 0 and row < self.numberOfRows and column < self.numberOfColumns:
            for element in self.matrix:
                if element.rowNumber == row and element.columnNumber == column:
                    return element.value
        else:
            print("Bad index in 'at' method.")
            return None
    def mathAt(self,row,column):
        if ((row > 0) and (column > 0)) and ((row <= self.numberOfRows) and (column <= self.numberOfColumns)):
            return self.at(row-1,column-1)
        else:
            print("Bad index in 'mathAt' method.")
            return None
    def insert(self,row,column,value):
        if row >= 0 and column >= 0 and row < self.numberOfRows and column < self.numberOfColumns:
            toRemoveIndex = 0
            for element in self.matrix:
                if element.rowNumber == row and element.columnNumber == column:
                    removed = self.matrix.pop(toRemoveIndex)
                    self.matrix.append(Element(row,column,value))
                toRemoveIndex += 1
        else:
            print("Bad index in 'insert' method.")
            return None
    def mathInsert(self,row,column,value):
        if ((row > 0) and (column > 0)) and ((row <= self.numberOfRows) and (column <= self.numberOfColumns)):
            self.insert(row-1,column-1,value)
        else:
            print("Bad index in 'mathInsert' method.")
            return None

    def diagonalMatrix(self):
        diagonal = Matrix(self.numberOfRows,self.numberOfColumns)
        for element in self.matrix:
            if element.rowNumber == element.columnNumber:
                diagonal.insert(element.rowNumber,element.columnNumber,element.value)
        return copy.deepcopy(diagonal)

    def negativeElements(self):
        negativeElements = Matrix(self.numberOfRows,self.numberOfColumns)
        for element in self.matrix:
            negativeElements.insert(element.rowNumber,element.columnNumber,-element.value)
        return copy.deepcopy(negativeElements)

    def lowerTriangularMatrix(self):
        lowerTriangular = Matrix(self.numberOfRows,self.numberOfColumns)
        for element in self.matrix:
            if element.rowNumber < element.columnNumber:
                lowerTriangular.insert(element.rowNumber,element.columnNumber,element.value)
        return copy.deepcopy(lowerTriangular)

    def upperTriangularMatrix(self):
        upperTriangular = Matrix(self.numberOfRows,self.numberOfColumns)
        for element in self.matrix:
            if element.rowNumber > element.columnNumber:
                upperTriangular.insert(element.rowNumber,element.columnNumber,element.value)
        return copy.deepcopy(upperTriangular)

    def lipUPKsum(L,U,k,i,m):
        toReturn = 0
        for p in rannge(1,k-1):
            toReturn = toReturn + L.mathAt(i,p)*U.mathAt(u,k)
        return toReturn

    def lkpUPJsum(L,U,k,j,m):
        toReturn = 0
        for p in rannge(1,k-1):
            toReturn = toReturn + L.mathAt(k,p)*U.mathAt(p,j)
        return toReturn

    def LUdecomposition():
        m = self.numberOfRows+1
        L = Matrix(self.numberOfRows,self.numberOfColumns)
        U = Matrix(self.numberOfRows,self.numberOfColumns)
        for i in range(1,m):
            L.mathInsert(i,1,A.mathAt(i,1))
        U.mathInsert(1,1,1)
        for j in range(2,m):
            U.mathInsert(1,j,A.mathAt(1,j)/L.mathAt(1,1))
        for k in range(2,m):
            for i in range(k,m):
                L.insert(i,k, ( A.mathAt(i,k) - lipUPKsum(L,U,k,i,m) ) )
            U.mathInsert(k,k,1)
            for j in range(k+1,m):
                U.insert(k,j, ( (A.mathAt(k,j) - lkpUPJsum(L,U,k,j,m)) / L.mathAt(k,k) ) )
        return copy.deepcopy( (copy.deepcopy(L),copy.deepcopy(U)) )

    def inverse(self):
        inverse = Matrix(self.numberOfRows,self.numberOfColumns)
        L,U = self.LUdecomposition()
        inverseColumns = []
        for indexOfInverseColumn in range(0,self.numberOfColumns):
            inverseColumn = solveLinearEquationSystem(A,canonicalBaseVector(indexOfInverseColumn))
            inverseColumns.append(inverseColumn)
        return copy.deepcopy(buildInverse(inverseColumns))

    def getRow(self,rowIndex):
        toReturnRow = []
        auxiliary = []
        for element in self.matrix:
            if element.rowNumber == rowIndex:
                auxiliary.append(copy.deepcopy(element))
        auxiliary.sort(key=lambda x: x.columnNumber)
        toReturnRow = [copy.deepcopy(element.value) for element in auxiliary]
        return copy.deepcopy((toReturnRow))

    def getColumn(self,columnIndex):
        toReturnColumn = []
        auxiliary = []
        for element in self.matrix:
            if element.columnNumber == columnIndex:
                auxiliary.append(copy.deepcopy(element))
        auxiliary.sort(key=lambda x: x.rowNumber)
        toReturnColumn = [copy.deepcopy(element.value) for element in auxiliary]
        return copy.deepcopy(toReturnColumn)

    def multiplyMatrix(self,otherMatrix):
        if self.numberOfColumns == otherMatrix.numberOfRows:
            toReturn = Matrix(self.numberOfRows,otherMatrix.numberOfColumns)
            for selfRowIndex in range(0,self.numberOfRows):
                selfCurrentRow = self.getRow(selfRowIndex)
                for otherColumnIndex in range(0,otherMatrix.numberOfColumns):
                    otherCurrentColumn = otherMatrix.getColumn(otherColumnIndex)
                    currentResult = multiplyAndAdd(selfCurrentRow,otherCurrentColumn)
                    toReturn.insert(selfRowIndex,otherColumnIndex,currentResult)
            return copy.deepcopy(toReturn)
        else:
            print("Bad number of rows or columns, in method 'multiplyMatrix'.")
            return None

    def scalarMultiplication(self,scalar):
        toReturn = Matrix(self.numberOfRows,self.numberOfColumns)
        for i in range(0,self.numberOfRows):
            for j in range(0,self.numberOfColumns):
                toReturn.insert(i,j,copy.deepcopy(scalar*self.at(i,j)))
        return copy.deepcopy(toReturn)

    def addMatrix(self,otherMatrix):
        if sameSize(self,otherMatrix):
            toReturn = Matrix(self.numberOfRows,otherMatrix.numberOfColumns)
            for rowIndex in range(0,self.numberOfRows):
                for columnIndex in range(0,otherMatrix.numberOfColumns):
                    toReturn.insert(rowIndex,columnIndex,(self.at(rowIndex,columnIndex)+otherMatrix.at(rowIndex,columnIndex)))
            return copy.deepcopy(toReturn)
        else:
            print("Bad number of rows or columns, in method 'addMatrix'.")
            return None

    def substractMatrix(self,otherMatrix):
        if sameSize(self,otherMatrix):
            toReturn = Matrix(self.numberOfRows,otherMatrix.numberOfColumns)
            for rowIndex in range(0,self.numberOfRows):
                for columnIndex in range(0,otherMatrix.numberOfColumns):
                    toReturn.insert(rowIndex,columnIndex,(self.at(rowIndex,columnIndex)-otherMatrix.at(rowIndex,columnIndex)))
            return copy.deepcopy(toReturn)
        else:
            print("Bad number of rows or columns, in method 'substractMatrix'.")
            return None

    def infiniteNorm(self):
        sums = []
        for rowIndex in range(0,self.numberOfRows):
            currentRow = self.getRow(rowIndex)
            sums.append(sum(currentRow))
        return max(sums)

    def normOne(self):
        sums = []
        for columnIndex in range(0,self.numberOfColumns):
            currentColumn = self.getColumn(columnIndex)
            sums.append(sum(currentColumn))
        return max(sums)

    def display(self):
        print("===============")
        for row in range(0,self.numberOfRows):
            for column in range(0,self.numberOfColumns):
                print(self.at(row,column)," ",end='')
            print('')
        print("===============")
