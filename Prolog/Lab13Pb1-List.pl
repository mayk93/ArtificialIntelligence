/*
Pseudo-Author / Modificator : Mandrescu Mihai Petru
Grupa: 242
Data: 30.05.2014
*/

/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina,
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/

/*
Predicate si structuri folosite:
1. st(JucatorCurent,ListaNumerelor,ScorulJucatoruluiCurent,ScorulJucatoruluiOpus,Nivelul,Max)
1.1 - 1.4 sunt intelese de la sine.
1.5 - Nivelul Maxim al arborelui de decizie.
1.6 - Daca este randul lui Max sau nu. Folosim aceasta variabila pentru a alege ori cea mai buna variannta ( in cazul copiilor lui Min adica randul lui Max ) ori cea mai rea varianta altfel. 

2. minimax(+Poz, -SuccBun, -Val)
2.1 - Configuratia listei, de exemplu: [1,2,3,4]
2.2 - Cel mai bun succesor. De exemplu, pentru lista de mai sus, putem lua fie '1' fie '4', deci succesorii ar fi [2,3,4] sau [1,2,3]. Cel mai bun succesor va fi [1,2,3] ( presupunand ca vrem sa maximizam scorul )
2.3 - Valoarea returnata, 4 in cazul de mai sus.

3. mutari(Poz,ListaPoz)
Returneaza toate mutarile posibile. Foloseste bagof pentru a genera mutari returnate de mutare, care intoarce mutari posibile.

4. celmaibun(ListaPoz,SuccBun,Val)
Acest predicat alege cel mai bun succesor disponibil si ii calculeaza scorul.

5. staticval(Poz,Val)
In momentul in care generarea succesorilor nu mai este posibila, am ajuns in stare finala si trebuie sa alegem varianta cea mai buna.
*/

mutare_max(st(Max,_,_,_,_,Max)).
mutare_min(st(J,_,_,_,_,Max)):- J\==Max.

mutari(Poz,LPoz):- bagof(Xpoz,mutare(Poz,Xpox),Lpoz).
mutare(st(JC,Lnr,SJC,SJO,N,Max),st(Jopus,Lnr1,SJO,SJC1,N1,Max)) :- N>0, N1 is N-1, jucator_opus(JC,Jopus),alege_nr(Lnr,Nr,Lnr1), SJC1 is SJC+Nr.

jucator_opus(J1,J2).
jucator_opus(J2,J1).

alege_nr([H|T],H,T).
alege_nr([_|T],E,LT) :- ultim_elem(T,E,LT).
ultim_elem([E],E,[]).
ultim_elem([H|T],E,[H|LT]) :- ultim_elem(T,E,LT).

staticval(st(Max,_,SJC,_,_,Max),SJC) :- !.
staticval(st(_,_,_,SJO,_,_),SJO).

minimax(Poz,SuccBun,Val) :- mutari(Poz,ListaPoz) ,!, celmaibun(ListaPoz,SuccBun,Val);  
staticval(Poz,Val).

celmaibun([Poz],Poz,Val) :- minimax(Poz,_,Val),!.
celmaibun([Poz1|ListaPoz],PozBun,ValBuna) :- minimax(Poz1,_,Val1) , celmaibun(ListaPoz,Poz2,Val2) , maibine(Poz1,Val1,Poz2,Val2,PozBun,ValBuna).

maibine(Poz0,Val0,Poz1,Val1,Poz0,Val0) :- ( mutare_min(Poz0) , Val0>Val1,! ) ; ( mutare_max(Poz0), Val0<Val1,! ). 
maibine(Poz0,Val0,Poz1,Val1,Poz1,Val1).