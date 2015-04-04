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
          #in loc de 0 de la len, era startFrom
          for index in range(0,len(bitArray),take+skip):
              for bitIndex in range(index,index+take):
                  if bitIndex < len(bitArray):
                      print("Parity bit ", step, " is made of: bitArray[", bitIndex, "] = ", bitArray[bitIndex])
                      bitSum = bitSum + bitArray[bitIndex]
                  else:
                      print("Parity bit ",step+1," = ", bitSum%2, " returned from else.")
                      return bitSum%2
      print("Parity bit ",step+1," = ", bitSum%2, " returned normaly.")              
      return bitSum%2
  def computeParityBit2(self,step,bitArray):
      print("\n\n\n")
      currentPowerOfTwo = 2**step
      take = currentPowerOfTwo
      skip = currentPowerOfTwo
      startFrom = currentPowerOfTwo - 1
      print("Bit Array is: " , bitArray)
      print("Current step is: ", step)
      print("Current power of 2: ", currentPowerOfTwo)
      print("Must take ", take, " and skip ", skip, " bits every time.")
      print("Start sum from: " , startFrom)
      takenBits = []
      for index in range(startFrom,len(bitArray),take+skip):
          for bitIndex in range(index,index+take):
              if self.isPowerOfTwo(bitIndex):
                  print("bitArray[",bitIndex,"] = " , bitArray[bitIndex] , " is at a power of two. We skip.")
              if bitIndex < len(bitArray):
                  print("Taking: bitArray[",bitIndex,"] = ",bitArray[bitIndex])
                  takenBits.append(bitArray[bitIndex])
      print("At this iteration, the following bits will be taken: " , takenBits)
      print("The sum of these bits is: " , sum(takenBits)%2)
      return sum(takenBits)%2
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
  def encode(self,bitArray):
      numberOfParityBits = self.getNumberOfParityBits(bitArray)
      markedArray = self.markArray(numberOfParityBits,bitArray)
      parityBitsArray = []
      for index in range(0, len(markedArray)):
          parityBitsArray.append(self.computeParityBit2(index,markedArray))
      #print(self.merge(bitArray,parityBitsArray))
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
  def getInput(self):
      intBitArray = input("Enter bits: ")
      return [int(x) for x in str(intBitArray)]
if __name__ == "__main__":
    hm = HammingMachine()
    #test = [0,0,1,0]
    #newTest = [1,1,1,1]
    bitInput = hm.getInput()
    hm.encode(bitInput)
    #hm.check([0, 0, 1, 0, 1, 1, 0])
