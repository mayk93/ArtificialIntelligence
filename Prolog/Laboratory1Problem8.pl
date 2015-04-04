/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/


unificare(X,Y):- X=Y.
unificare1(X,X).
produs1(X,Y,Rez):- Rez = X*Y.
produs2(X,Y,R) :- produs1(X,Y,Rez) , R is Rez.
/*
unificare1 este echivalent cu unifcare(X,X). Daca argumentele sunt lafel, va returna true.

Predicatul 'produs1' nu functioneaza corect deoarece foloseste '=' in loc de 'is'.
'is' forteaza evaluarea expresiei X*Y.

produs2(4,5,X).
X = 20 ? y
yes
*/