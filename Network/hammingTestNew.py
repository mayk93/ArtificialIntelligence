import math
class HammingMachine:
  def __init__(self):
    pass
  def computeParityBit(self,step,bitArray):
      bitParity = 0
      for index in range(0,len(bitArray),2**step):
          if index < len(bitArray):
              bitParity = bitParity + bitArray[index]
          else:
              return bitParity%2
      return bitParity%2
  def isPowerOfTwo(self,toCheck):
      return toCheck != 0 and ((toCheck & (toCheck - 1)) == 0)
  def merge(self,bitArray,parityBitsArray):
      encodedBitArray = []
      bitIndex = 0
      parityIndex = 0
      for index in range(0,len(bitArray)+len(parityBitsArray)):
          if self.isPowerOfTwo(index+1):
              encodedBitArray.append(parityBitsArray[parityIndex])
              parityIndex = parityIndex+1
          else:
              encodedBitArray.append(bitArray[bitIndex])
              bitIndex = bitIndex + 1
      return encodedBitArray        
  def encode(self,bitArray):
      numberOfParityBits = int(math.log(len(bitArray),2)) + 1
      parityBitsArray = []
      for index in range(0, numberOfParityBits):
          parityBitsArray.append(self.computeParityBit(index,bitArray))
      print(self.merge(bitArray,parityBitsArray))
if __name__ == "__main__":
    hm = HammingMachine()
    test   = [1,0,0,1,1,1,0,0,0,1]
    hm.encode(test)
