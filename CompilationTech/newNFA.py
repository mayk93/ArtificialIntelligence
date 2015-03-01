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
startSymbolIndex = 0
initialState = 1

reachedFinalState = False

def nfa(inputString,currentSymbolIndex,currentState):
    '''
    Here, I check if I entered an empty string.
    If I did, I must see if there are any lambda transitions from the initial state
    '''
    if len(inputString) == 0:
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
    '''
    Here, I still have symbols to check
    '''
    if currentSymbolIndex < len(inputString) and reachedFinalState == False:
        currentPossibleTransitions = possibleTransitions(inputString[currentSymbolIndex],currentState)
        newSymbolIndex = currentSymbolIndex + 1
        
        for transition in currentPossibleTransitions:
            nfa(inputString,newSymbolIndex,transition)
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
    for transition in delta[lambdaTransition]:
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
