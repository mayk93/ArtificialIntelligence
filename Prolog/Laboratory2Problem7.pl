/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 26.04.2014
*/

inversa(L,Li):- invers_aux(L,[],Li).
invers_aux([H|T],L_aux,Li):- invers_aux(T,[H|L_aux],Li).
invers_aux([],Li,Li).

/* Queries */

/*
|?- inversa([1,2,3],L).
L = [3,2,1] ? 
*/