inputString = "a"

lambdaTransition = 0

states  = [1,2,3,4]
symbols = ['a','b']
delta = {'a':[(1,1),(1,2),(1,3)],'b':[(2,3)],lambdaTransition:[(1,2),(1,4)]}
initialState = 1
finalStates = [3]

'''
For use in delta, for example:
delta['a'] = transitionWithA ( [1,1),(1,2),(1,3)] )
transitionWithA[1] = (1,2)
transitionWithA[possibleCurrentState] = 1
transitionWithA[possibleNextState] = 2
'''
possibleCurrentState = 0
possibleNextState = 1

def nfa():
    return 0

def possibleTransitions(currentSymbol,currentState):
    possibleTransitions = []
    for symbol in delta:
        if str(symbol) == currentSymbol:
            for transition in delta[symbol]:
                if currentState == transition[possibleCurrentState]:
                    possibleTransitions.append(transition[possibleNextState])
    for transition in delta[lambdaTransition]:
        if currentState == transition[possibleCurrentState]:
            possibleTransitions.append(transition[possibleNextState])
    return list(set(possibleTransitions))

def main():
    nfa(inputString)

if __name__ == "__main__":
    main()
