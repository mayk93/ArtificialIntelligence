/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 26.04.2014
*/

lista1N(N,L):- lista1Naux(N,1,L).
lista1Naux(N,C,[C|T]):- C<N, C1 is C+1, lista1Naux(N,C1,T).
lista1Naux(N,N,[N]).

/* Queries */

/*
| ?- lista1N(5,L).
L = [1,2,3,4,5] ? 
*/