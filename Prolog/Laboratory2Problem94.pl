/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 27/04/2014 */

/* This program simulates the eating behavior of goblins while at the same time proving Newtons Theory of Gravitation.   */

/* Help predicate: */
/* help(+Input) */

help('Input') :- write('mainPredicate(+InitialMatrix,-FinalMatrix)'),nl,write('InitialMatrix must be inputted as a List of Lists, where each sub list is a COLUMN and not a line of the Matrix.').
help('Output') :- write('FinalMatrix is a List of Lists and will be displayed as such. The sublists correspond to the columns of the FinalMatrix.').

/* Corner Cases: */
/* corner(X) */

corner(X) :- write('None.').

/*
The mainPredicate takes InitialMatrix, a List of Lists, as input and returns a FinalMatrix, also a List of Lists.
The solution is generated using  the following idea: We see how deep a column is, we count how many goblins there are, we count how many apples are above the  first goblin and
calculate the number of spaced needed using this information. If there are G goblins, A apples and S spaces we write S spaces, A apple and G goblins and form a column.
The process is repeated for each column.
*/

/* --- Solution --- */
constructMatrix([],FinalMatrix,FinalMatrix).
constructMatrix([H|InitialMatrix],IntermediaryMatrix,FinalMatrix) :- rewriteColumn(H,Result),constructMatrix(InitialMatrix,[Result|IntermediaryMatrix],FinalMatrix).

mainPredicate(InitialMatrix,FinalMatrix) :- constructMatrix(InitialMatrix,[],FinalMatrix1),invert(FinalMatrix1,FinalMatrix).

invert(L,NL) :- invert3(L,[],NL).
invert3([H|T],L,NL) :- invert3(T,[H|L],NL).
invert3([],NL,NL).

generateNewColumn(0,0,0,[]).
generateNewColumn(0,0,Spaces,NewColumn) :- Spaces1 is Spaces-1, generateNewColumn(0,0,Spaces1,NewColumn1), NewColumn = [-1|NewColumn1].
generateNewColumn(0,A,Spaces,NewColumn) :- A1 is A-1, generateNewColumn(0,A1,Spaces,NewColumn1), NewColumn = [0|NewColumn1].
generateNewColumn(G,A,Spaces,NewColumn) :- G1 is G-1, generateNewColumn(G1,A,Spaces,NewColumn1), NewColumn = [1|NewColumn1].

rewriteColumn(OldColumn,EvenNewerColumn) :- computeGoblinsAndApllesOnColumn(OldColumn,G,A,CD),Spaces is CD - G - A,generateNewColumn(G,A,Spaces,NewColumn),invert(NewColumn,EvenNewerColumn).

computeGoblinsAndApllesOnColumn([],0,0,0).
computeGoblinsAndApllesOnColumn([H|T],Goblin,Apple,ColumnDepth) :-( H == 1, computeGoblinsAndApllesOnColumn(T,Goblin1,Apple1,ColumnDepth1), Goblin is Goblin1 + 1, Apple is Apple1-Apple1, ColumnDepth is ColumnDepth1 + 1);(H == 0, computeGoblinsAndApllesOnColumn(T,Goblin,Apple1,ColumnDepth1),Apple is Apple1 +1,ColumnDepth is ColumnDepth1 + 1).
/* --- -------- --- */

/* Queries */

/*
mainPredicate([[0,0,1,0,0],[0,0,0,0,0],[0,1,0,0,1],[1,0,0,1,0],[0,0,1,1,0]],M).
M = [[-1,-1,0,0,1],[0,0,0,0,0],[-1,-1,0,1,1],[-1,-1,-1,1,1],[-1,0,0,1,1]] ? y
yes
*/