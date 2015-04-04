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
O parte din cod a fost modificat.

Modificarile au fost facute cu ajutorul urmatoarele tutoriale:

http://www.csupomona.edu/~jrfisher/www/prolog_tutorial/5_3.html
http://www.science.uva.nl/~arnoud/education/ZSB/2006/GamePlaying.pdf
https://www.youtube.com/watch?v=hM2EAvMkhtk

O parte din cod a fost preluat din urmatoarele surse ( Cu modificari si comentarii adaugate ) :

http://rosettacode.org/wiki/Tic-tac-toe#Prolog
https://courses.cs.washington.edu/courses/cse341/03sp/slides/PrologEx/tictactoe.pl.txt
https://github.com/myok12/7langs7weeks/blob/master/prolog/advanced.md

*/

/* Algoritmul Alpha-Beta */
alfabeta(Poz, Alfa, Beta, SucBun, Val) :- mutari(Poz, [P1 | LPoz]), !,
							alfabeta(P1, Alfa, Beta, _ , V1),
							update(Alfa, Beta, P1, V1, NAlfa, NBeta),
							bunsucc(LPoz, NAlfa, NBeta, P1, V1, SucBun,Val).
alfabeta(Poz, Alfa, Beta, SucBun, Val) :- staticval(Poz, Val).

bunsucc([], _ , _ , P1, V1, P1, V1) :- !.
bunsucc([Poz | LPoz], Alfa, Beta, Poz1, Val1, PozBuna, ValBuna) :-
						alfabeta(Poz, Alfa, Beta, _ , Val),
						bun_dela(Poz, Val, Poz1, Val1, Poz2, Val2),
						destuldebun(LPoz, Alfa, Beta, Poz2, Val2, PozBuna, ValBuna).
			
/* Atinge limita superioara */
destuldebun(_, Alfa, Beta, Poz, Val, Poz, Val) :- muta_min(Poz), Val > Beta,!.

/* Atinge limita inferioara */
destuldebun(_, Alfa, Beta, Poz, Val, Poz, Val) :- muta_max(Poz), Val < Alfa, !.

destuldebun(LPoz, Alfa, Beta, P, Val, PozBuna, ValBuna) :-
				update(Alfa, Beta, P, Val, NAlfa, NBeta),
				bunsucc(LPoz, NAlfa, NBeta, P, Val, PozBuna, ValBuna).
				
/* Actualizez valorile Alfa si Beta */
update(Alfa, Beta, Poz, Val, Val, Beta) :- muta_min(Poz), Val > Alfa, !.
update(Alfa, Beta, Poz, Val, Alfa, Val) :- muta_max(Poz), Val < Beta, !.
update(Alfa, Beta, _ , _ , Alfa, Beta).

bun_dela(Poz, Val, Poz1, Val1, Poz, Val) :- muta_min(Poz), Val > Val1, !.
bun_dela(Poz, Val, Poz1, Val1, Poz, Val) :- muta_max(Poz), Val < Val1, !.
bun_dela(_ , _ , Poz1, Val1, Poz1, Val1).

/* Aici generez mutari posibile. 'Mutari' imi alcatuieste lista de mutari posibile in baza predicatului 'mutare' care genereaza cate o mutare. */
/* 'Pos' este o structura, echivalentul lui 'st' din laborator. Il folosesc pentru a retine Jucatorul ( P - Player ) , Tabla si Nivelul. */
/* N, Nivelul, este citit de la inceput, cate nivele va avea arborele de decizie, adica cat de mult 'vede' in viitor algoritmul.  */
mutari(Poz, PozList) :- bagof(P, mutare(Poz, P), PozList).
mutare(pos(P, Tabla, N), pos(O, Tabla1, N1)) :- N > 0,\+ final(Tabla, _ ),other_player(P, O), N1 is N - 1, replace(Tabla, P, Tabla1).
	
other_player(x, 0).
other_player(0, x).

replace([b | Rest], P, [P | Rest]).
replace([X | Rest], P, [X | Rest1]) :- replace(Rest, P, Rest1).

/* Calculul valorii nodului, in functie de scorul ficarei linii, coloane, diagonale. */
/* In tutorialele urmarite, scorul unei mutari era calculat in alt mod ( sau era acelasi dar nu mi-am dat eu seama ) . */
/* Am incercat sa implemntez ce ne-ati spus in cadrul laboratorului, ca scorul trebuie calculat in functie de liniile / coloanele / diagonalele libere. */
staticval(pos( _ , B, N), Val) :- final(B, P), !, castigator(P, N, Val).
staticval(pos( Player , Tabla, _ ), Val) :- linia1(Tabla, Player, L1), linia2(Tabla, Player, L2), linia3(Tabla, Player, L3),
		                                                    coloana1(Tabla, Player, C1), coloana2(Tabla, Player, C2), coloana3(Tabla, Player, C3), 
                                                            diagonala1(Tabla, Player, D1), diagonala2(Tabla, Player, D2),
		                                                    Val is L1 + L2 + L3 + C1 + C2 + C3 + D1 + D2.

/* Starile finale , hard-codate */
/* Primele trei reprezinta castig prin alinierea pe linie. */
/* Urmatoarele trei reprezinta alinierea pe coloana. */
/* Ultimele doua alinierea pe diagonala. */
/* P este simbolul gasit la pozitia respectiva, si acesta trebuie sa fie diferit de b , adica "blank" */        		
final([P, P, P | _ ], P):- P \== b,!.
final([ _ , _ , _ , P, P, P | _ ], P) :- P \== b,!.
final([ _ , _ , _ , _ , _ , _ , P, P, P], P) :- P \== b,!.
final([ P, _ , _ , P, _ , _ , P | _ ], P) :- P \== b,!.
final([ _ , P, _ , _ , P, _ , _ , P | _ ], P) :-P \== b,!.
final([ _ , _ , P, _ , _ , P, _ , _ , P], P) :- P \== b,!.
final([P, _ , _ , _ , P, _ , _ , _ , P], P) :- P \== b,!.
final([ _ , _ , P, _ , P, _ , P | _ ], P) :- P \== b,!.

/* In lapsa unui castigator determinat de 'final'-urile de mai sus, putem spune ca jocul s-a terminat cand nu mai exista spatii libere pe tabla. */
final(Tabla, b) :- \+ (member(b, Tabla)).

castigator(x, N, Val) :- !, Val is -10 * (N + 1).
castigator(0, N, Val) :- !, Val is 10 * (N + 1).
castigator( _ , _ , 0).

/* Calculun liniilor, coloanelor si diagonalelor bune / libere. Folosesc aceste predicate penru determinare unei mutari bune. */
/* De exemplu, linia 1 (linia1) este libera daca simbolurile gasite pe ea, C1, C2 si C3 nu sunt simboluri ale celuilalt jucator. */
linia1([C1, C2, C3 | _ ], Player, 1) :- other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
linia1( _ , _, 0).

linia2([_ , _ , _ , C1, C2, C3 | _ ], Player, 1) :- other_player(Player, Other), \+ member(Other, [C1, C2, C3]), !.
linia2( _ , _, 0).

linia3([ _ , _ , _ , _ , _ , _ , C1, C2, C3], Player, 1) :-other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
linia3( _ , _, 0).

coloana1([ C1, _ , _ , C2, _ , _ , C3 | _ ], Player, 1) :-other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
coloana1( _ , _, 0).

coloana2([ _ , C1, _ , _ , C2, _ , _ , C3 | _ ], Player, 1) :-other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
coloana2( _ , _, 0).

coloana3([ _ , _ , C1, _ , _ , C2, _ , _ , C3], Player, 1) :-other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
coloana3( _ , _, 0).

diagonala1([ C1, _ , _ , _ , C2, _ , _ , _ , C3], Player, 1) :-other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
diagonala1( _ , _, 0).

diagonala2([ _ , _ , C1, _ , C2, _ , C3 | _ ], Player, 1) :-other_player(Player, Other), \+ member(Other, [C1, C2, C3]),!.
diagonala2( _ , _, 0).

/* Tipul nodului (min sau max) */
muta_min(pos(x, _ , _ )).
muta_max(pos(0, _ , _ )).

/* Predicatul principal */
/* De aici in jos este jocul in sine ( optiuni, afisare, etc ) care doar face apel la algoritm. */

run:- startJoc(P), adancime(N), initial(Tabla), scrie_tabla(Tabla),joc(pos(P, Tabla, N)).

startJoc(P) :- write('Bun venit la acest joc de X si 0. Oamenii joaca cu X. Noi jucam cu 0. Scrie simbolul care doresti sa imceapa: '), nl, write('Raspunde cu x sau 0.'), nl,  read(P).

adancime(N) :- write('Cat de tare vrei sa te bat? ( In limbaj academic, numarul de nivele ale arborelui de decizie ) '), read(N).

/* Initierea tablei cu 'b' adica blank. */
initial([b, b, b, b, b, b, b, b, b]).

joc(pos(P, Tabla, _ )) :- final(Tabla, P1), !, scrie_castig(P1).
joc(pos(x, Tabla, N)) :- !,det_mutare(Tabla, Succ), scrie_tabla(Succ), joc(pos(0, Succ, N)).
joc(pos(0, Tabla, N)):- alfabeta(pos(0, Tabla, N),-100,100,pos(x, Succ, _ ),Val) , scrie_mutare(Succ, Val), joc(pos(x, Succ, N)).

scrie_castig(b) :- !, write('Egalitate.'), nl.
scrie_castig(x):- !, write('Ai avut noroc ... '), nl.
scrie_castig(_ ):- write('Deus ex machina, LOOSER!!!'), nl.

det_mutare(Tabla, Succ) :- repeat, det_coord(L, C), N is L * 3 + C , verifica(N, Tabla, Succ),!.
			
scrie_mutare(Tabla, Val) :- write('Randul tau: '), nl,scrie_tabla(Tabla), nl.

getChosenLine(L) :- write('Linia: ') , read(L).
getChosenColumn(C) :- write('Coloana: ') , read(C).
det_coord(L , C) :- getChosenLine(L) , getChosenColumn(C).

verifica(0, [b | Rest], [x | Rest]) :- !.
verifica(N, [X | Tabla], [X | Succ]) :- N1 is N - 1, verifica(N1, Tabla, Succ).

scrie_tabla(Tabla) :- repl(Tabla, ' ', [E1, E2, E3, E4, E5, E6, E7, E8, E9]),
        write('  0 1 2'), nl,
		write('0 '), write(E1), write(' '), write(E2), write(' '), write(E3),nl,
		write('1 '), write(E4), write(' '), write(E5), write(' '), write(E6),nl,
		write('2 '), write(E7), write(' '), write(E8), write(' '), write(E9), nl.

repl([], _ , []) :- !.
repl([b | Rest], X, [X | Rest1]) :- !, repl(Rest, X, Rest1).
repl([E | Rest], X, [E | Rest1]) :- repl(Rest, X, Rest1).

/* Interogari */
/*
 run.
Bun venit la acest joc de X si 0. Oamenii joaca cu X. Noi jucam cu 0. Scrie simbolul care doresti sa imceapa: 
Raspunde cu x sau 0.
|: x.
Cat de tare vrei sa te bat? ( In limbaj academic, numarul de nivele ale arborelui de decizie ) |: 5.
  0 1 2
0      
1      
2      
Linia: |: 0.
Coloana: |: 0.
  0 1 2
0 x    
1      
2      
Randul tau: 
  0 1 2
0 x 0  
1      
2      

Linia: |: 2.
Coloana: |: 2.
  0 1 2
0 x 0  
1      
2     x
Randul tau: 
  0 1 2
0 x 0  
1   0  
2     x

Linia: |: 2.
Coloana: |: 1.
  0 1 2
0 x 0  
1   0  
2   x x
*/