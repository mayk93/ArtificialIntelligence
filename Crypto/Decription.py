dictionary = "15letterWords.txt"

cA = "3C585A58691B0CA8A8ADC1913B8092"
cB = "3C585A58691B0CA6A1AFC29D2C889D"
cC = "3C4C4B497C0611AFA9A6CD8A318D87 "
cD = "305A5E5F700010B8A9AAC594319587"
cE = "305A5B526B0007BEA1A4C58B2C889D "
cF = "305A4C4F7C0717AAAEADC38D2B8D87"
cG = "3E51515E6F080FA2BAA9D891378F8D"

encrypted = [cA,cB,cC,cD,cE,cF,cG]

c1Decimal = []
c2Decimal = []
c3Decimal = []
c4Decimal = []
c5Decimal = []
c6Decimal = []
c7Decimal = []

def xor(decimalArray0,decimalArray1):
    return [x^y for x,y in zip(decimalArray0,decimalArray1)]

for index in range(0,len(cA)-1,2):
    hexString = "0x" + cA[index]+cA[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c1Decimal.append(decimalValue%255)

for index in range(0,len(cB)-1,2):
    hexString = "0x" + cB[index]+cB[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c2Decimal.append(decimalValue%255)

for index in range(0,len(cC)-1,2):
    hexString = "0x" + cC[index]+cC[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c3Decimal.append(decimalValue%255)

for index in range(0,len(cD)-1,2):
    hexString = "0x" + cD[index]+cD[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c4Decimal.append(decimalValue%255)

for index in range(0,len(cE)-1,2):
    hexString = "0x" + cE[index]+cE[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c5Decimal.append(decimalValue%255)

for index in range(0,len(cF)-1,2):
    hexString = "0x" + cF[index]+cF[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c6Decimal.append(decimalValue%255)

for index in range(0,len(cG)-1,2):
    hexString = "0x" + cG[index]+cG[index+1]
    hexString = hexString.lower()
    decimalValue = int(hexString,16)
    c7Decimal.append(decimalValue%255)

'''
print(c1Decimal)
print(c2Decimal)
print(c3Decimal)
print(c4Decimal)
print(c5Decimal)
print(c6Decimal)
print(c7Decimal)
'''

m1_xor_m2 = xor(c1Decimal,c2Decimal)
m2_xor_m3 = xor(c2Decimal,c3Decimal)
m3_xor_m4 = xor(c3Decimal,c4Decimal)#Candidate
m4_xor_m5 = xor(c4Decimal,c5Decimal)
m5_xor_m6 = xor(c5Decimal,c6Decimal)
m6_xor_m7 = xor(c6Decimal,c7Decimal)#Candidate
m7_xor_m1 = xor(c7Decimal,c1Decimal)#Candidate

'''
print(m1_xor_m2)
print(m2_xor_m3)
print(m3_xor_m4)# Candidate
print(m4_xor_m5)
print(m5_xor_m6)
print(m6_xor_m7)# Candidate
print(m7_xor_m1)# Candidate
'''

dictionaryFile = open(dictionary,'r')
for line in dictionaryFile:
    for word in line.split(' '):
        cribWord = word 
        crib = [ord(c) for c in cribWord]
        if crib in range(65,91) or (97,123):
            candidate = xor(m3_xor_m4,crib)
            possibleWord = ''.join(chr(i) for i in candidate)
            #print(possibleWord," from ",word)

#anarily
'''
#inadmissibility
'''

inadmissibilityWord = "inadmissibility"
hipothesis_inadmissibility = [ord(c) for c in inadmissibilityWord]

key = xor(hipothesis_inadmissibility,c4Decimal)
print(key)

hexKey = [hex(i) for i in key]
print(hexKey)

testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c1Decimal))
print(testResult)
testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c2Decimal))
print(testResult)
testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c3Decimal))
print(testResult)
testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c4Decimal))
print(testResult)
testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c5Decimal))
print(testResult)
testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c6Decimal))
print(testResult)
testResult = ""
testResult = ''.join(chr(i) for i in xor(key,c7Decimal))
print(testResult)
