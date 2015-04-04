/*
Author: Mandrescu Mihai Petru, 242
Date: 30.03.2014
*/

/*
This programme will represent a matrix in three different ways.
This programme will make use of the theoretical knowledge provided in the
second laboratory. 
*/

/*
Auxiliary predicate that will serve as an example generator:
example(+Type)
*/

example(1) :- write('[[1,2,3][4,5,6][7,8,9]]').

/*Corner Cases:*/
example('Corner 1') :- write('matrix([name that does not exist],column,row,value)').
example('Corner 2') :- write('matrix(name,column,row,[value allready initialized])').

/* --- Solution 1 --- */

/* 
This solution is fairly intuitive, it employes a list of lists to
model a matrix.
We define a matrix as being a list of lists.
We define the value at each cell.
We call the predicate by specifieing the name of the matrix,
the cell coordinates and giving an emplty variabile, say X, 
where the result will be put in.
*/

/* ------Solution Predicate----------- */

matrix(matrixOne,[[1,2,3],[4,5,6],[7,8,9]]). 

getElement(matrixOne, 0, 0, 1).
getElement(matrixOne ,0, 1, 2).
getElement(matrixOne, 0, 2, 3).
getElement(matrixOne, 1, 0, 4).
getElement(matrixOne, 1, 1, 5).
getElement(matrixOne, 1, 2, 6).
getElement(matrixOne, 2, 0, 7).
getElement(matrixOne, 2, 1, 8).
getElement(matrixOne, 2, 2, 9).

/* ---------------------------------- */

/* ----------------- */

/* --- Solution 2 --- */

/*
This is not an elegant solution.
There is no matrix, not in the real sense of the word.
Each element will in fact be a list of three elements,
the value and the two coordinates.
In addition, an element has a number, starting from 0.
The index of the number is used to backtrack.
The programme checks if the element at index
0 fits the coordinates given.
If so, it assigns to Value the value of the element
( The first element of Vector ).
If not, it recursively calls the predicate with an increased index.
*/

getN([],N,X)    :- write('No such thing'),nl.
getN([H|T],1,X) :- X is H,nl.
getN([H|T],N,X) :- N1 is N-1, getN(T,N1,X). 

element('matrixTwo',0,[1,0,0]).
element('matrixTwo',1,[2,0,1]).

element('matrixTwo',2,[3,1,0]).
element('matrixTwo',3,[4,1,1]).

getElement(Name,N,X,Y,Value) :- element(Name,N,Vector), getN(Vector,2,HereX), getN(Vector,3,HereY), ((X =:= HereX, Y =:= HereY) -> getN(Vector,1,Value) ; (N1 is N+1,getElement(Name,N1,X,Y,Value))).

/* ---------------------------------- */

/* ----------------- */

/* --- Solution 3 --- */

/*
This solution is similar to the first.
The difference is that it uses only the index of the element and not the
coordinates.
In order to retrieve the element from the matrix, an index search is performed.
The appropriate coordinates in the matrix will be calculated using the formula:
X = index mod length ( X axis ).
Y = index divide depth ( Y axis ).
*/

getN([],N,X)    :- write('No such thing'),nl.
getN([H|T],1,X) :- X is H,nl.
getN([H|T],N,X) :- N1 is N-1, getN(T,N1,X). 

element('matrixThree',0,0).
element('matrixThree',1,1).
element('matrixThree',2,2).
element('matrixThree',3,3).
element('matrixThree',4,4).
element('matrixThree',5,5).
element('matrixThree',6,6).
element('matrixThree',7,7).
element('matrixThree',8,8).
element('matrixThree',9,9).

axisX(X) :- X is 3.
axisY(Y) :- Y is 3.

getElement(Name,Index,Value,X,Y) :- element(Name,Index,Value),axisX(L),axisY(D),X is mod(Index,L),Y is Index/D.   
