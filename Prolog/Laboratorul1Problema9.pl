% Author: Mandrescu Mihai Petru 242
% Date: 14/03/2014

/*
Acest program este rezolvarea exercitiului obligatoriu 9, Laboratorul 1. Acest
program cere evaluarea unui predicat cu doua argumente care "evalueaza" o
ecuatie.
*/

/*
Predicate auxiliare care sa ofere exemple de date de intrare:
*/

exemplu('1') :- write('"ec(2,B)."').
exemplu('2') :- write('"ec(2,4)."').
exemplu('3') :- write('"ec(A,B)."').

/*
Unde:
1     : Tipul 1
2     : Tipul 2
3     : Tipul 3
Cazuri particulare:
*/

exemplu('Deg') :- write('ec("abc","efg").').

/*
Unde "Deg" vine de la caz degenerat.
Am considerat un input "aiurea" ca fiind un caz degenerat, desi e putin fortat.
*/

%------Predicat solutie-----------

isInit(A) :- var(A),!,fail.
isInit(_).

notInt(A) :- integer(A),!,fail.
notInt(_).

varIsBad(A) :- isInit(A),notInt(A).

w(_) :- write('Invalid').

evaluate( A,B ) :- (varIsBad(A);varIsBad(B)), !, w(_).  
evaluate( A,B ) :- ec(A,B).

both(A,B)  :- integer(A),integer(B).
onlyA(A,B) :- integer(A),notInt(B).
onlyB(A,B) :- integer(B),notInt(A).
none(A,B)  :- notInt(A),notInt(B).

ec(A,B):- both(A,B),A-B =:= -2.
ec(A,B):- onlyA(A,B),B is 2+A.
ec(A,B):- onlyB(A,B),A is -2+B.
ec(A,B):- none(A,B),A = -1,B = 1.

%---------------------------------


/*
Predicatele principale sunt "evaluate" si "ec".
"evaluate" triaza inpurturile. Este un if_then_else.
In cazul in care oricare dintre cele doua variabile nu este buna
( predicatul varIsBad ), atunci se apeleaza predicatul w care
scrie "Invalid". Altfel, in cazul unui input valid, se trece la evaluarea
propriuzisa, predicatul ec.

Un input corect este un o ori un int, ori o variabila neinitializata.
O variabila initializata dar care nu este integer corespunde cazului degenerat.

Se disting 4 cazuri, descrise si in clasa:

1. Ambele variabile initializate. ( Predicatul "both" )
2. Doar A este initializat. ( Predicatul "onlyA" )
3. Doar B este initializat. ( Predicatul "onlyB" )
4. Nici una din A sau B nu este initializata. ( Predicatul "none" )

Programul va distinge cazul, si va acctiona in concordanta.

In cazul in care ambele sunt initializate, se verifica daca diferenta lor este -2.
In cazurile in care doar una din ele este initializata, se calculeaza una in functie de cealalta.
In cazuul in care nici una din ele nu este initializata, se dau valori satisfacatoare.
*/

%Exemple de interogari
/*
?- evaluate(2,B).
B = 4 ? 
-----
?- evaluate(A,5).
A = 3 ?
-----
?- evaluate(2,4).
yes
-----
?- evaluate(2,5).
no
*/
