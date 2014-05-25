import math

class HammingMachine:
    
  def __init__(self):
      pass

  def issquare(self,toCheck):
      return toCheck != 0 and ((toCheck & (toCheck - 1)) == 0)

  def markArray(self, noOfRedBits,bitArray):
      toReturn = []
      placeIndex = 0
      for index in range(0,len(bitArray)+noOfRedBits):
          if self.issquare(index + 1):
              toReturn.append(2)
          else:
              toReturn.append(bitArray[placeIndex])
              placeIndex = placeIndex + 1
      print("To Return: " , toReturn)
      return toReturn

  def noOfRedBits(self,bitArray):
        initialLength = len(bitArray)
        numberOfBits = int(math.log(initialLength,2))
        
        while int(math.log(numberOfBits+initialLength,2)) > numberOfBits:
            numberOfBits=int(math.log(numberOfBits+initialLength,2))
        return numberOfBits+1

  def computeParityBits(self,array):
      square = 1
      while square <= len(array):
          bitSum = 0
          index = square
          while index <= len(array):
              bitIndex = index
              while bitIndex < (index+square) and bitIndex <= len(array):
                  if array[bitIndex-1] != 2:
                      bitSum = bitSum + array[bitIndex-1]
                  bitIndex = bitIndex + 1
              index = (bitIndex-1) + square + 1
          array[square - 1] = bitSum%2   
          square = 2*square
      print("Encoded Bit Array: " , array)
      return array
    
  def encode(self,bitArray):
      noOfRedBits = self.noOfRedBits(bitArray)
      array = self.markArray(noOfRedBits,bitArray)
      parityBits = self.computeParityBits(array)

  def decode(self,array):
      foundError = False
      bitDisfunctionality = 0
      square = 1
      while square <= len(array):
          bitSum = 0
          index = square
          while index <= len(array):
              bitIndex = index
              while bitIndex < (index+square) and bitIndex <= len(array):
                  if not( self.issquare(bitIndex )):
                      bitSum = bitSum + array[bitIndex-1]
                  bitIndex = bitIndex + 1
              index = (bitIndex-1) + square + 1
          if array[square - 1] != (bitSum%2):
              bitDisfunctionality = bitDisfunctionality + square - 1
              foundError = True
          square = 2*square
      if foundError == True:
          print("Error Bit: " , bitDisfunctionality)
          return bitDisfunctionality
      print("Ok")
      return -1
  def getInput(self):
      intBitArray = input("Enter bits: ")
      return [int(x) for x in str(intBitArray)]

if __name__ == "__main__":

    hm = HammingMachine()
    test = hm.getInput()
    hm.encode(test)
    hm.decode(test)
