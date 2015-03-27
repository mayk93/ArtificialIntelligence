'''
Numerical Calculus
Homework 3
'''
#Libraries
import gmpy2

#Variables
b = []

#Functions
"""
The function newEmptyMatrix(size)
will return a size x size 0 filled matrix.
"""
def newEmptyMatrix(size):
    newMatrix = []
    for i in range(0,size):
        newRow = []
        for j in range(0,size):
            newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix
def freeTerms(size):
    newB = []
    for i in range(0,size):
        newB.append(1)
    return newB]
'''
This method should be refactored to cgeck for negatives
'''
def isZero(listToCheck):
    index = 0
    for item in listToCheck:
        if item == 0:
            return (True,index)
        else:
            index += index
    return (False,index)
#Classes
"""
This class with implement square matrices
"""
def Matrix:
    def __init__(self,size):
        self.size = size
        self.matrix = newEmptyMatrix(size)
    '''
    The fillMatrix method will set the elements
    of the matrix to their appropriate values
    '''
    def fillMatrix(self):
        for i in range(0,self.size):
            self.matrix[i][i]   = 2
            self.matrix[i][i+1] = 1
            self.matrix[i+1][i] = 1
    '''
    The iterate will iterate over the matrix
    but with mathematical notation:
    1 through n would translate to 0 to n-1 ( both ends included )
    '''
    def iterate(rowStart,rowStop,columnStart,columnStop):
        isZero,badIndex = isZero([rowStart,rowStop,columnStart,columnStop])
        if not isZero:
            pass
        else
            print("Bad index:",badIndex)
            return -1
