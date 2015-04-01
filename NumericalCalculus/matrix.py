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
    def transpose(self):
        oldNumberOfRows = self.numberOfRows
        self.numberOfRows = self.numberOfColumns
        self.numberOfColumns = oldNumberOfRows
        for element in self.matrix:
            oldRowNumber = element.rowNumber
            element.rowNumber = element.columnNumber
            element.columnNumber = oldRowNumber

    '''
    ===========================================================================
    The following section contains auxiliary methods used in the implementation
    of the matrix multiplication algorithm.
    ===========================================================================
    '''
    '''
    Order by column for getRow
    '''
    def getRow(self,rowIndex):
        toReturnRow = []
        auxiliary = []
        for element in self.matrix:
            if element.rowNumber == rowIndex:
                auxiliary.append(copy.deepcopy(element))
        auxiliary.sort(key=lambda x: x.columnNumber)
        toReturnRow = [copy.deepcopy(element.value) for element in auxiliary]
        return toReturnRow
    '''
    Order by row for getColumn
    '''
    def getColumn(self,columnIndex):
        toReturnColumn = []
        auxiliary = []
        for element in self.matrix:
            if element.columnNumber == columnIndex:
                auxiliary.append(copy.deepcopy(element))
        auxiliary.sort(key=lambda x: x.rowNumber)
        toReturnColumn = [copy.deepcopy(element.value) for element in auxiliary]
        return toReturnColumn
    '''
    ===========================================================================
    '''
    # This multiplication algorithm assumes your matrix (self) is on the "left"
    # while the other matrix is on the "right".
    def multiplyMatrix(self,otherMatrix):
        toReturn = Matrix(self.numberOfRows,otherMatrix.numberOfColumns)
        if self.numberOfColumns == otherMatrix.numberOfRows:
            for selfRowIndex in range(0,self.numberOfRows):
                selfCurrentRow = self.getRow(selfRowIndex)
                for otherColumnIndex in range(0,otherMatrix.numberOfColumns):
                    otherCurrentColumn = otherMatrix.getColumn(otherColumnIndex)
                    currentResult = multiplyAndAdd(selfCurrentRow,otherCurrentColumn)

                    print("Row",selfRowIndex,"from matrix A with column",otherColumnIndex,"from matrix B")
                    print("Row [A]:",selfCurrentRow)
                    print("Column [B]:",otherCurrentColumn)
                    print("Result:",currentResult)

                    toReturn.insert(selfRowIndex,otherColumnIndex,currentResult)

                    print("The resulting matrix, so far:")
                    toReturn.display()
            return toReturn
        else:
            print("Bad number of rows or columns, in method 'multiplyMatrix'.")
            return None
    def display(self):
        print("===============")
        for row in range(0,self.numberOfRows):
            for column in range(0,self.numberOfColumns):
                print(self.at(row,column)," ",end='')
            print('')
        print("===============")
