/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 26.04.2014
*/

desparte_perechi(E1,E2,[E1,E2|_]).
desparte_perechi(E1,E2,[_,_|T]):-desparte_perechi(E1,E2,T).
desparte_perechi(E1,_,[E1]).
desparte_perechi_p(E1,E2,[E1,E2|_]).
desparte_perechi_p(E1,E2,[_,_|T]):-desparte_perechi_p(E1,E2,T).
desparte_perechi_i(E1,E2,[A,B|T]):-desparte_perechi_i(E1,E2,T) ; E1=A,  E2=B.
desparte_perechi_i(E1,_,[E1]).
desparte_perechi_2(E1,E2,[E1,E2|_]).
desparte_perechi_2(E1,E2,[_|T]):- desparte_perechi_2(E1,E2,T).

/* Interface: */

/*
desparte_perechi(-El1,-El2,+Lista)
desparte_perechi_p(-El1,-El2,+Lista)
desparte_perechi_i(-El1,-El2,+Lista).
desparte_perechi_2(-El1,-El2,+Lista).
*/

/* Queries: */

/*
?- desparte_perechi(A,B,[1,2,3,4,5,6,7,8]).
A = 1,
B = 2 ? ;
A = 3,
B = 4 ? ;
A = 5,
B = 6 ? ;
A = 7,
B = 8 ?
*/