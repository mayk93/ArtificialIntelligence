inputString = "1111111111"

lambdaTransition = 0

states  = [1,2,3,4]
symbols = ['0','1']
delta = {'0':[(3,4),(4,5)],'1':[(1,2),(1,4),(5,6),(6,6)],lambdaTransition:[(1,2),(2,3),(4,5)]}
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
startSymbolIndex = 0
initialState = 1

reachedFinalState = False

def nfa(inputString,currentSymbolIndex,currentState):
    '''
    Here, I still have symbols to check
    '''
    if currentSymbolIndex < len(inputString):
        currentPossibleTransitions = possibleTransitions(inputString[currentSymbolIndex],currentState)
        currentPossibleLambdaTransitions = possibleLambdaTransitions(currentState)
        newSymbolIndex = currentSymbolIndex + 1
        
        for transition in currentPossibleTransitions:
            nfa(inputString,newSymbolIndex,transition)
        for lambdaTransition in currentPossibleLambdaTransitions:
            nfa(inputString,currentSymbolIndex,lambdaTransition)
    else:
        '''
        Here, I run out of symbols to parse, so I check if I am in a final state,
        or if I can make lambda transitions to get to a final state
        '''
        currentPossibleLambdaTransitions = possibleLambdaTransitions(currentState)
        if len(currentPossibleLambdaTransitions) > 0:
            for transition in currentPossibleLambdaTransitions:
                nfa(inputString,currentSymbolIndex,transition)
        else:
            if currentState in finalStates:
                global reachedFinalState
                reachedFinalState = True
                return
            else:
                return

def possibleTransitions(currentSymbol,currentState):
    possibleTransitions = []
    for symbol in delta:
        if str(symbol) == currentSymbol:
            for transition in delta[symbol]:
                if currentState == transition[possibleCurrentState]:
                    possibleTransitions.append(transition[possibleNextState])
    return list(set(possibleTransitions))

def possibleLambdaTransitions(currentState):
    possibleLambdaTransitions = []
    for currentLambdaTransition in delta[lambdaTransition]:
        if currentState == currentLambdaTransition[possibleCurrentState]:
            possibleLambdaTransitions.append(currentLambdaTransition[possibleNextState])
    return list(set(possibleLambdaTransitions))

def main():
    nfa(inputString,startSymbolIndex,initialState)
    print(reachedFinalState)

if __name__ == "__main__":
    main()
