% Author: Mandrescu Mihai Petru 242
% Date: 06/03/2014

%Acest program este rezolvarea exercitiului obligatoriu 17, Laboratorul 1. Acest program cere evaluarea predicatul "pasaj" care,
%in urma regulilor impuse, ne spune daca putem construi un pasaj intre asezarile X si Y:

%Aceasta este varianta 1 din 3.

%Predicate auxiliare care sa ofere exemple de date de intrare:
%exemplu(+Tip,+Ex)

exemplu('OO')     :- write('Bucuresti-Cluj').
exemplu('ONO')    :- write('Bucuresti-Bunesti').
exemplu('NONO')   :- write('Bunesti-Alunisu').
exemplu('ODxODy') :- write('Bucuresti-Mangalia').

%Unde:
%OO     : Oras - Oras ( Aceeasi Dimensiune )
%ONO    : Oras - Not Oras
%NONO   : Not Oras - Not Oras
%ODxODy : Oras Dimensiune x - Oras Dimensiune y ( x si y diferiti )

%Cazuri particulare:
exemplu('Deg') :- write('Bucuresti-Bucuresti').

%Unde "Deg" vine de la caz degenerat.

%------Predicat solutie-----------
localitate('Bucuresti',1921751).
localitate('Iasi',321580).
localitate('Cluj-Napoca',318027).
localitate('Turda',55770).
localitate('Alexandria',50591).
localitate('Mangalia',40037).
localitate('Bunesti',911).
localitate('Alunisu',172).

sat('Alunisu').
sat('Bunesti').

orasMare(X)      :- localitate(X,Y) , Y > 150000.
orasMijlociu(X)  :- localitate(X,Y) , Y > 50000 , Y < 150000.
orasMic(X)       :- localitate(X,Y) , Y > 10000 , Y < 50000.
orasFoarteMic(X) :- localitate(X,Y) , Y < 10000.

esteOras(X)        :- sat(X),!,fail.
esteOras(_).

aceasiPop(X,Y)   :- (orasMare(X),orasMare(Y));(orasMijlociu(X),orasMijlociu(Y));(orasMic(X),orasMic(Y));(orasFoarteMic(X),orasFoarteMic(Y)).

pasaj(X,Y)       :- esteOras(X),esteOras(Y),aceasiPop(X,Y).
%---------------------------------


/*
Rezolvarea este naturala, nu implica nici un fel de artificiu. Am urmat cuvant cu cuvant instructiunile programului.
Am inceput prin a declara localitatile.
Localitatile se identifica prin nume si populatie.
Apoi, am indicat ca Alunisu si Bunesti sunt sate.
Am definit predicate pentru fiecare tip de oras, predicatul fiind calculat in functie de populatie.
Am definit predicatul esteOras, care imi spune daca o localitate NU este sat.
Dat fiind faptul ca ProLog lucreaza in ipoteza lumii inchise, am definit acest predicat in functie de faptele sat(X).
Am definit predicatul aceasiPop care imi spune daca doua orase, X si Y, fac parte din aceeasi clasa.
Am definit predicatul pasaj dupa enunt: "numai intre orase" - Deci esteOras, dinou din pricina ipotezei lumii inchise.
					"numai intre doua orase de acelsi tip din punct de vedere al populatiei."
*/

%Exemple de interogari
/*
| ?- exemplu('OO').

Bucuresti-Cluj

yes
-----
| ?- exemplu('Deg').

Bucuresti-Bucuresti
yes
-----
| ?- orasMare('Alexandria').

no
-----
| ?- esteOras('Iasi').

yes
-----
| ?- pasaj('Bucuresti','Iasi').

yes
*/


/*============================================================================*/

% Author: Mandrescu Mihai Petru 242
% Date: 06/03/2014

%Acest program este rezolvarea exercitiului obligatoriu 17, Laboratorul 1. Acest program cere evaluarea predicatul "pasaj" care,
%in urma regulilor impuse, ne spune daca putem construi un pasaj intre asezarile X si Y:

%Aceasta este varianta 2 din 3.

%Predicate auxiliare care sa ofere exemple de date de intrare:
%exemplu(+Tip,+Ex)

exemplu('OO')     :- write('Bucuresti-Cluj').
exemplu('ONO')    :- write('Bucuresti-Bunesti').
exemplu('NONO')   :- write('Bunesti-Alunisu').
exemplu('ODxODy') :- write('Bucuresti-Mangalia').

%Unde:
%OO     : Oras - Oras ( Aceeasi Dimensiune )
%ONO    : Oras - Not Oras
%NONO   : Not Oras - Not Oras
%ODxODy : Oras Dimensiune x - Oras Dimensiune y ( x si y diferiti )

%Cazuri particulare:
exemplu('Deg') :- write('Bucuresti-Bucuresti').

%Unde "Deg" vine de la caz degenerat.

%------Predicat solutie-----------
localitate('Bucuresti','orasMare').
localitate('Iasi','orasMare').
localitate('Cluj-Napoca','orasMare').
localitate('Turda','orasMijlociu').
localitate('Alexandria','orasMijlociu').
localitate('Mangalia','orasMic').
localitate('Bunesti','sat').
localitate('Alunisu','sat').

popMare(X)       :- localitate(X,Y) , Y = 'orasMare'.
popMijlocie(X)   :- localitate(X,Y) , Y = 'orasMijlociu'.
popMica(X)       :- localitate(X,Y) , Y = 'orasMic'.
popFoarteMica(X) :- localitate(X,Y) , Y = 'orasFoarteMic'.
popSat(X)        :- localitate(X,Y) , Y = 'sat'.

esteOras(X)        :- popSat(X),!,fail.
esteOras(_).

aceasiPop(X,Y)   :- (popMare(X),popMare(Y));(popMijlocie(X),popMijlocie(Y));(popMica(X),popMica(Y));(popFoarteMica(X),popFoarteMica(Y)).

pasaj(X,Y)       :- esteOras(X),esteOras(Y),aceasiPop(X,Y).
%---------------------------------


/*
Aceasta solutie este aproximativ "complementara" fata de prima. Diferenta consta in faptul ca nu calculez tipul orasului pornind de la
populatie, ci invers. Determin marimea populatie in functie de marimea orasului si permit constructia pasajului doar intre orase
cu acelasi tip de populatie ( deci indirect de aceeasi marime ).
*/

%Exemple de interogari
/*
| ?- popMare('Bucuresti').

yes
-----
| ?- esteOras('Mangalia').

yes
-----
| ?- pasaj('Bucuresti','Turda').

no
*/

/*============================================================================*/

% Author: Mandrescu Mihai Petru 242
% Date: 10/03/2014

%Acest program este rezolvarea exercitiului obligatoriu 17, Laboratorul 1. Acest program cere evaluarea predicatul "pasaj" care,
%in urma regulilor impuse, ne spune daca putem construi un pasaj intre asezarile X si Y:

%Aceasta este varianta 3 din 3.

%Predicate auxiliare care sa ofere exemple de date de intrare:
%exemplu(+Tip,+Ex)

exemplu('OO')     :- write('Bucuresti-Cluj').
exemplu('ONO')    :- write('Bucuresti-Bunesti').
exemplu('NONO')   :- write('Bunesti-Alunisu').
exemplu('ODxODy') :- write('Bucuresti-Mangalia').

%Unde:
%OO     : Oras - Oras ( Aceeasi Dimensiune )
%ONO    : Oras - Not Oras
%NONO   : Not Oras - Not Oras
%ODxODy : Oras Dimensiune x - Oras Dimensiune y ( x si y diferiti )

%Cazuri particulare:
exemplu('Deg') :- write('Bucuresti-Bucuresti').

%Unde "Deg" vine de la caz degenerat.

%------Predicat solutie-----------
localitate('Bucuresti',['orasMare',1921751]).
localitate('Iasi',['orasMare',321580]).
localitate('Cluj-Napoca',['orasMare',318027]).
localitate('Turda',['orasMijlociu',55770]).
localitate('Alexandria',['orasMijlociu',50591]).
localitate('Mangalia',['orasMic',40037]).
localitate('Bunesti',['sat',911]).
localitate('Alunisu',['sat',172]).

membru(X, [Y|T]) :- X = Y; member(X, T).

tip(Z,'orasMare').
tip(Z,'orasMijlociu').
tip(Z,'orasMic').
tip(Z,'sat').

esteOras(X)      :- localitate(X,Y),membru('sat',Y),!,fail.
esteOras(_).

notSat(Z)        :- Z = 'sat',!,fail.
notSat(_).

aceasiPop(X,Y)   :- localitate(X,M),localitate(Y,N),tip(Z,K),notSat(K),membru(K,M),membru(K,N).

pasaj(X,Y)       :- localitate(X,M),localitate(Y,N),esteOras(X),esteOras(Y),aceasiPop(X,Y).
%---------------------------------


/*
Aceasta solutie este diferita fata de primele doua, care sunt relativ similare.
In aceasta solutie, baza de cunostiitnte legata de localitati este reprezentata sub forma
unor liste. O lista este compusa din tipul orasului si populatie. Predicatul 'membru'
imi permite sa aflu daca un element X este membru al listei cu capul Y si corpul T.
Am definit predicatul 'tip' care imi spune tipul orasului. Verific daca ceva
este oras ( predicatul 'esteOras' ) daca 'sat' nu este un membru al listei
care corespunde orasului cautat. Verific compatibilitatea oraselor cu
predicatul 'aceasiPop' care imi spune daca tipul K este in ambele liste si nu este
sat.
*/

%Exemple de interogari
/*
| ?- esteOras('Bucuresti').

yes
-----
| ?- esteOras('Bunesti').

no
-----
| ?- aceasiPop('Bucuresti','Mangalia').

no
-----
| ?- pasaj('Bucuresti','Cluj-Napoca').

yes
*/
