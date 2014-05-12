/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

pisica('Miaunel').
tigru('Tigrila').
felina(X):-pisica(X).
felina(X):-tigru(X).

/*
 ?- felina('Miaunel').
yes
| ?- felina('Tigrila').
yes
*/