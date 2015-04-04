/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 27/04/2014 */

/* This program displays a matrix.   */

/* Help predicate: */
/* help(+X) */

help(X) :- write('mainPredicate(+Matrix) where Matrix is a List of Lists.').

/* Corner Cases: */
/* corner(X) */

corner(X) :- write('None.').

/*
Matrix will be a Lists of Lists. Thus, the Head H of the Matrix is a List. The mainPredicate feeds the Head, a Lists, to the
displayLine predicate. This predicate writes the Head of the Head, an element, adds a space and calls it`s self recursivly
untill the List if empty.
*/

/* --- Solution --- */
displayLine([]).
displayLine([HeadOfHead|Head]) :- write(HeadOfHead),write(' '),displayLine(Head).

mainPredicate([]).
mainPredicate([Head|Matrix]) :- displayLine(Head),write('\n'),mainPredicate(Matrix).
/* --- -------- --- */

/* --- Queries --- */
/*
mainPredicate([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).
0 1 2 3 
4 5 6 7 
8 9 10 11 
12 13 14 15 
yes

mainPredicate([[0,1],[4,5,6,7],[8,9],[12,13,14]]).             
0 1 
4 5 6 7 
8 9 
12 13 14 
yes
*/