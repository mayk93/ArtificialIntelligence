import math

class HammingMachine:
    
  def __init__(self):
      pass

  def isPowerOfTwo(self,toCheck):
      return toCheck != 0 and ((toCheck & (toCheck - 1)) == 0)

  def markArray(self, numberOfParityBits,bitArray):
      toReturn = []
      placeIndex = 0
      for index in range(0,len(bitArray)+numberOfParityBits):
          if self.isPowerOfTwo(index + 1):
              toReturn.append(2)
          else:
              toReturn.append(bitArray[placeIndex])
              placeIndex = placeIndex + 1
      print("To Return: " , toReturn)
      return toReturn

  def getNumberOfParityBits(self,bitArray):
        initialLength = len(bitArray)
        numberOfBits = int(math.log(initialLength,2))
        
        while int(math.log(numberOfBits+initialLength,2)) > numberOfBits:
            numberOfBits=int(math.log(numberOfBits+initialLength,2))
        return numberOfBits+1

  def computeParityBits(self,markedArray,numberOfParityBits):
      powerOfTwo = 1
      while powerOfTwo <= len(markedArray):
          bitSum = 0
          index = powerOfTwo
          while index <= len(markedArray):
              bitIndex = index
              while bitIndex < (index+powerOfTwo) and bitIndex <= len(markedArray):
                  if markedArray[bitIndex-1] != 2:
                      bitSum = bitSum + markedArray[bitIndex-1]
                  bitIndex = bitIndex + 1
              index = (bitIndex-1) + powerOfTwo + 1
          markedArray[powerOfTwo - 1] = bitSum%2   
          powerOfTwo = 2*powerOfTwo
      print("Encoded Bit Array: " , markedArray)
      return markedArray
    
  def encode(self,bitArray):
      numberOfParityBits = self.getNumberOfParityBits(bitArray)
      markedArray = self.markArray(numberOfParityBits,bitArray)
      parityBits = self.computeParityBits(markedArray,numberOfParityBits)

  def decode(self,bit):
      pass

  def getInput(self):
      intBitArray = input("Enter bits: ")
      return [int(x) for x in str(intBitArray)]

if __name__ == "__main__":

    hm = HammingMachine()
    test = hm.getInput()
    hm.encode(test)
