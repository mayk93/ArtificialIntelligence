import random

# Example Functions:
    # Density Function:
def f(x):
    if x >= 0 and x <= 1:
        return 1
    else:
        return 0
    # Repartition Function:
def F(x):
    if x < 0:
        return 0
    elif x >= 0 and x <= 1:
        return x
    else:
        return 1
    # Inverted F:
def invertedF(x):
    if x < 0:
        return 0
    elif x >= 0 and x <= 1:
        return x
    else:
        return 1

def MReversed():
    U = random.uniform(0,1)
    X = invertedF(U)
    return X
    
def main():
    Results = []
    for i in range(0, 100):
        Results.append(MReversed())
    print(Results)

if __name__ == "__main__":
    main()
