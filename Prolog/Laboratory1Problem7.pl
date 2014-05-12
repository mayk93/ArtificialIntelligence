/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

produs(X,Y,Rez):- Rez is X*Y.
impartire(X,Y,Rez) :- Y =\= 0 , Rez is X/Y.

/*
'de ce nu merge in loc de is sa folosim =:= ? (explicati in comentariu) '
Deoarece '=:=' este '==' pentru aritmetica. Nu este operator de 'asignare'.

impartire(6,2,R).
R = 3.0 ? y
yes
| ?- impartire(6,0,R).
no
*/