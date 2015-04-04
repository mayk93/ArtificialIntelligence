% Author: Mandrescu Mihai Petru 242
% Date: 11/03/2014

/*
Acest program este rezolvarea exercitiului obligatoriu 15, Laboratorul 1. Acest
program cere evaluarea unui predicat cu trei argumente care ne spune daca o data
are un format corect.
*/

/*
Predicate auxiliare care sa ofere exemple de date de intrare:
*/

exemplu('DC') :- write('11,03,2014').
exemplu('DI') :- write('32,03,2014').

/*
Unde:
DC     : Data Corecta
DI     : Data InCorecta
Cazuri particulare:
*/

exemplu('Deg') :- write('29,02,2014').

/*
Unde "Deg" vine de la caz degenerat.
Am trecut acest caz in clasa degeneratelor intrucat ocazional exista data de
29 februarie.
*/

%------Predicat solutie-----------

an(X)       :- integer(X),(0 < X).

anBisect(X) :- integer(X),(0 < X),(0 =:= X mod 4).

anNormal(X) :- anBisect(X),!,fail.
anNormal(_).

lunaMare(X) :- integer(X),(0 < X),(X =< 12),(9 =\= X),(11 =\= X),((1 =:= (X mod 2));(8 =:= X);(10 =:= X);(12 =:= X)).

lunaMica(X) :- integer(X),(0 < X),(X =< 12),(8 =\= X),(10 =\= X),(12 =\= X),((0 =:= (X mod 2));(9 =:= X);(11 =:= X)).

zi(X,Y)     :- integer(X),(0 < X),(2 =\= Y),(((X < 32),lunaMare(Y));((X < 31),lunaMica(Y))).

februarie(X,Y,Z)   :- integer(X),integer(Y),integer(Z),(0 < X),(2 == Y),( (anBisect(Z),(29 == X));(anNormal(Z),an(Z),(X < 29)) ).

dataCorecta(X,Y,Z) :- (zi(X,Y),an(Z));(februarie(X,Y,Z)).

%---------------------------------


/*
Probabil nu este cea mai frumoasa rezolvare.

Am construit predicatele an, anBisect si anNormal. an verifica corectitudinea
anului. Am fost nevoit sa construiesc predicatul an pentru ca predicatul anNormal
este construit prin negarea predicatului anBisect. Insa, negand an bisect pot
obtine ca -24 este un anNormal sau 'dfds' este un anNormal. Utilizarea conjunctiei
anNormal(),an() a fost folosita in predicatul februarie: "(anNormal(Z),an(Z),(X < 29))".

Am separat cazul degenerat al lunii februarie ( in speta 29.02.YYYY ). Pentru 
februarie exista un predicat special care permite ziua de 29 in ani bisectie si 
o respinge in anii normali.

Am separat lunile mici ( 30 de zile ) de cele mari ( 31 de zile ).

Initial, uitasem ca incepand cu August se schimba si am crezut ca lunile impare sunt
mari si cele pare mici. Am realizat dupa ( dupa ce am verificat 31.09.2014 si am primit "yes")
ca incepand cu August lunile pare devin mari si cele impare mici. Am decis sa tratez manual
aceasta eroare si am adaugat verificarile, de exemplu "(8 =:= X);(10 =:= X);(12 =:= X)".

Predicatul zi primeste atat o zi (X) cat si o luna(Y) si accepta 31 de zile pentru
lunile mari si 30 pentru lunile mici.

Predicatul dataCorecta trebuie sa evalueze corect pentru lunile normale sau
pentru februarie.  
*/

%Exemple de interogari
/*
| ?- exemplu('DC').
11,03,2014
yes
-----
| ?- dataCorecta(13,05,2014).
yes
-----
| ?- dataCorecta(30,02,2012).
no
-----
| ?- dataCorecta(29,02,2016).
yes
*/


