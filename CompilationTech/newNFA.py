import tkinter as tk

#GUI
root = tk.Tk()
root.geometry("300x300")

#Debug purposes
'''
inputString = "1111111111"

lambdaTransition = 0

states  = [1,2,3,4]
symbols = ['0','1']
delta = {'0':[(3,4),(4,5)],'1':[(1,2),(1,4),(5,6),(6,6)],lambdaTransition:[(1,2),(2,3),(4,5)]}
initialState = 1
finalStates = [3]
'''

#Macros
lambdaTransition = 0
noLambdaTransitions = -1
possibleCurrentState = 0
possibleNextState = 1
startSymbolIndex = 0
initialState = 1
maxRecursions = 500
maxLambdaRecursions = 500

#Input NFA from file
fileName = "input.txt"
states  = []
symbols = []
delta = {}
initialState = 0
finalStates = []

inputString = "" # Is added from GUI

'''
First line of file are the available states.
Second line of file are the available symbols.
The following lines are the delta function:
    Each line represents the transitions for a given symbol.
    Example:
    a 3 4 4 5 means that for state 3 reading symbol 'a' we can go to state 4
              and from state 4 reading symbol 'a' we can go to state 5
    
'''
def getInput(fileName):
    inputFile = open(fileName, 'r')
    
    global states
    global symbols
    global delta
    global initialState
    global finalStates
    
    states = [int(state) for state in list(inputFile.readline().split(' '))]
    symbols = [str(symbol) for symbol in [int(symbolInt) for symbolInt in list(inputFile.readline().split(' '))]]
    for symbol in symbols:
        rawTransitions = list(inputFile.readline().split(' '))
        if len(rawTransitions) % 2 == 0:
            print("Invalid Input. There must be a symbol and an even number of transitions on the line.")
            return
        else:
            currentSymbol = rawTransitions[0] # The first item on the list is the symbol
            delta[currentSymbol] = list(zip(*2*[iter([int(transition) for transition in rawTransitions[1:]])]))
    # Read lambda transitions. Write -1 if there are no lambda transitions.
    rawLambdaTransitions = list(inputFile.readline().split(' '))
    if noLambdaTransitions in [int(transition) for transition in rawLambdaTransitions]:
        pass
    else:
        if len(rawLambdaTransitions) % 2 == 1:
            print("Invalid Input. There must be an even number of lambda transitions on the line.")
            return
        else:
            lt = list(zip(*2*[iter([int(transition) for transition in rawLambdaTransitions])]))
            delta[lambdaTransition] = lt#list(zip(*2*[iter([int(transition) for transition in rawLambdaTransitions[1:]])]))
    initialState = list(inputFile.readline().split(' '))
    if len(initialState) != 1:
        print("Invalid Input. There must only one initial state.")
        return
    else:
        initialState = int(initialState[0])
    finalStates = list(inputFile.readline().split(' '))
    if len(finalStates) <= 0 or '' in finalStates:
        print("Invalid Input. There must be at least one final state.")
        return
    else:
        finalStates = [int(finalState) for finalState in finalStates]
    
'''
For use in delta, for example:
delta['a'] = transitionWithA ( [1,1),(1,2),(1,3)] )
transitionWithA[1] = (1,2)
transitionWithA[possibleCurrentState] = 1
transitionWithA[possibleNextState] = 2
'''

reachedFinalState = False

def nfa(inputString,currentSymbolIndex,currentState):
    if currentSymbolIndex >= len(inputString) - 1 and currentState in finalStates:
        global reachedFinalState
        reachedFinalState = True
        return
    '''
    Here, I still have symbols to check
    '''
    if currentSymbolIndex < len(inputString):
        currentPossibleTransitions = possibleTransitions(inputString[currentSymbolIndex],currentState)
        currentPossibleLambdaTransitions = possibleLambdaTransitions(currentState)
        newSymbolIndex = currentSymbolIndex + 1
        
        for transition in currentPossibleTransitions:
            global maxRecursions
            maxRecursions = maxRecursions - 1
            if maxRecursions > 0:
                nfa(inputString,newSymbolIndex,transition)
        for lambdaTransition in currentPossibleLambdaTransitions:
            global maxLambdaRecursions
            maxLambdaRecursions = maxLambdaRecursions - 1
            if maxLambdaRecursions > 0:
                nfa(inputString,currentSymbolIndex,lambdaTransition)
    else:
        '''
        Here, I run out of symbols to parse, so I check if I am in a final state,
        or if I can make lambda transitions to get to a final state
        '''
        currentPossibleLambdaTransitions = possibleLambdaTransitions(currentState)
        if len(currentPossibleLambdaTransitions) > 0:
            for transition in currentPossibleLambdaTransitions:
                global maxLambdaRecursions
                maxLambdaRecursions = maxLambdaRecursions - 1
                if maxLambdaRecursions > 0:
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

def checkInput(inputString):
    for symbol in inputString:
        if symbol not in symbols:
            print("0:",symbol,"not in",symbols)
            return False
    for transition in delta[symbol]:
        if transition[possibleCurrentState] not in states:
            print("1:",transition[possibleCurrentState],"not in",states)
            return False
        if transition[possibleNextState] not in states:
            print("2:",transition[possibleNextState],"not in",states)
            return False
    if initialState not in states:
        print("3:",initialState,"not in",states)
        return False
    for state in finalStates:
        if state not in states:
            print("4:",state,"not in",states)
            return False
    return True

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.inputEntry = tk.Entry()
        self.inputEntry.pack()
        
        self.NFArunApplication = tk.Button(self)
        self.NFArunApplication["text"] = "Run Application"
        self.NFArunApplication["command"] = self.runApplication
        self.NFArunApplication.pack()

        self.QUIT = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.QUIT.pack()

    def runApplication(self):
        global inputString
        inputString = self.inputEntry.get()
        if(checkInput(inputString)):
            pass
        
def display():
    global root
    app = Application(master=root)
    app.mainloop()
    
def main():
    getInput(fileName)
    display()
    nfa(inputString,startSymbolIndex,initialState)
    print(reachedFinalState)
    
if __name__ == "__main__":
    main()
