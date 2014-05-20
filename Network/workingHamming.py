import math
class HammingMachine:
  def __init__(self):
    pass
  def computeParityBit(self,step,bitArray):
      currentPowerOfTwo = 2**step
      take = currentPowerOfTwo
      skip = currentPowerOfTwo
      startFrom = currentPowerOfTwo - 1
      bitSum = 0
      if startFrom < len(bitArray):
          for index in range(startFrom,len(bitArray),take+skip):
              for bitIndex in range(index,index+take):
                  if bitIndex < len(bitArray):
                      bitSum = bitSum + bitArray[bitIndex]
                  else:
                      return bitSum%2
      return bitSum%2
  def isPowerOfTwo(self,toCheck):
      return toCheck != 0 and ((toCheck & (toCheck - 1)) == 0)
  def addPlaceholders(self,encodedLength):
      toReturn = []
      for index in range(0,encodedLength):
          toReturn.append(2)
      return toReturn
  def addParityBits(self,encodedBitArray , parityBitsArray):
      reversedParityBitsArray = list(reversed(parityBitsArray))
      parityIndex = 0
      for index in range (0,len(encodedBitArray)):
          if self.isPowerOfTwo(index):
              encodedBitArray[index-1] = reversedParityBitsArray[parityIndex]
              parityIndex = parityIndex+1
      return encodedBitArray
  def addDataBits(self,encodedBitArray,bitArray):
        bitIndex = 0
        for index in range (0,len(encodedBitArray)):
            if encodedBitArray[index] == 2:
                encodedBitArray[index] = bitArray[bitIndex]
                bitIndex = bitIndex+1
        return encodedBitArray
  def merge(self,bitArray,parityBitsArray):
      encodedLength = len(bitArray) + len(parityBitsArray)
      encodedBitArray = self.addPlaceholders(encodedLength)
      encodedBitArray = self.addParityBits(encodedBitArray , parityBitsArray)
      encodedBitArray = self.addDataBits(encodedBitArray , bitArray)
      return encodedBitArray
  def getNumberOfParityBits(self, bitArray):
      return int(math.log(len(bitArray),2)) + 1
  def getParityBits(self,bitArray):
      toReturn = []
      for index in range (0,len(bitArray)):
          if self.isPowerOfTwo(index+1):
              toReturn.append(bitArray[index])
      return toReturn     
  def encode(self,bitArray):
      numberOfParityBits = self.getNumberOfParityBits(bitArray)
      parityBitsArray = []
      for index in range(0, numberOfParityBits):
          parityBitsArray.append(self.computeParityBit(index,bitArray))
      print(self.merge(bitArray,parityBitsArray))
  def getSum(self,step,bitArray):
      currentPowerOfTwo = 2**step
      take = currentPowerOfTwo
      skip = currentPowerOfTwo
      startFrom = currentPowerOfTwo - 1
      bitSum = 0
      if startFrom < len(bitArray):
          for index in range(startFrom,len(bitArray),take+skip):
              for bitIndex in range(index,index+take):
                  if bitIndex < len(bitArray) and not(self.isPowerOfTwo(bitIndex+1)):
                      bitSum = bitSum + bitArray[bitIndex]
                  else:
                      pass
      return bitSum%2
  def reCheckSums(self,parityBits,sumsArray):
      somethingWrong = []
      for index in range (0,len(parityBits)):
          if parityBits[index] != sumsArray[index]:
              somethingWrong.append(index)
      if somethingWrong != []:
          return False
      else:
          return True
  def checkSums(self,parityBits,sumsArray,bitArray):
      somethingWrong = []
      for index in range (0,len(parityBits)):
          if parityBits[index] != sumsArray[index]:
              somethingWrong.append(index)
      if somethingWrong != []:
          for attempt in range(0 , len(somethingWrong) ):
            print("Problem at: ")
            print(somethingWrong[attempt])
            print("Changing bitArray[",somethingWrong[attempt],"] to: ",bitArray[sumsArray[somethingWrong[attempt]]]^ 1)
            bitArray[somethingWrong[attempt]] =  bitArray[sumsArray[somethingWrong[attempt]]] ^ 1
            sumsArray[somethingWrong[attempt]] = sumsArray[somethingWrong[attempt]] ^ 1
            if self.reCheckSums(parityBits,sumsArray) == True:
                print("Ok")
                return
      else:
          print("Ok")
  def check(self,bitArray):
      parityBits = self.getParityBits(bitArray)
      sumsArray = []
      for index in range (0,len(parityBits)):
          sumsArray.append(self.getSum(index,bitArray))
      sumsArray = list(reversed(sumsArray))
      self.checkSums(parityBits,sumsArray,bitArray)
      print(bitArray)
if __name__ == "__main__":
    hm = HammingMachine()
    test = [0,0,1,0]
    newTest = [1,1,1,0]
    hm.encode(newTest)
    hm.check([0, 0, 1, 0, 1, 1, 0])