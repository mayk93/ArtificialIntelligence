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
    def display(self):
        print("===============")
        for row in range(0,self.numberOfRows):
            for column in range(0,self.numberOfColumns):
                print(self.at(row,column)," ",end='')
            print('')
        print("===============")
