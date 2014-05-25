/* Algoritm Min-Max Joc Lista */

/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina, 
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/


%minimax(+Poz, -SuccBun, -Val)
minimax(Poz,SuccBun,Val):-
mutari(Poz,ListaPoz),!,
celmaibun(ListaPoz,SuccBun,Val);
staticval(Poz,Val).

%celmaibun(+ListaPoz, -Succesor, -Valoare)
celmaibun([Poz],Poz,Val):-
minimax(Poz,_,Val),!.

celmaibun([Poz1|ListaPoz],PozBun,ValBuna):-
minimax(Poz1,_,Val1),
celmaibun(ListaPoz,Poz2,Val2),
maibine(Poz1,Val1,Poz2,Val2,PozBun,ValBuna).

%maibine(+Poz1,+Val1, +Poz2, +Val2, -PozRez, -ValRez )
maibine(Poz0,Val0,Poz1,Val1,Poz0,Val0):-
mutare_min(Poz0),
Val0>Val1,!
;
mutare_max(Poz0),
Val0<Val1,!.
maibine(Poz0,Val0,Poz1,Val1,Poz1,Val1).

