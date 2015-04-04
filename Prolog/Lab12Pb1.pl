/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina, 
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/

/*
Pseudo-Author: Mandrescu Mihai Petru
Grupa: 242
Data: 30.05.2014
*/

scop([[1,2,3],[4,5,6],[7,8]]).

%bestfirst(+Nod_initial,-Solutie)
bestfirst(Nod_initial,Solutie):-
expandeaza([],l(Nod_initial,0/0),9999999,_,
da,Solutie).



%expandeaza(+Drum,+Arbore,+Limita,-A1,-Rezultat,-Solutie),



expandeaza(Drum,l(N,_),_,_, da,[N|Drum]):-scop(N).


expandeaza(Drum,l(N,F/G),Limita,Arb1,Rez,Sol):-
F=<Limita,
(bagof(M/C,(s(N,M,C), \+ (membru(M,Drum))),Succ),!,
listasucc(G,Succ,As),
cea_mai_buna_f(As,F1),
expandeaza(Drum,t(N,F1/G,As),Limita,Arb1, Rez,Sol);
Rez=imposibil).

expandeaza(Drum,t(N,F/G,[A|As]),Limita,Arb1,Rez,
Sol):-
F=<Limita,
cea_mai_buna_f(As,BF),
min(Limita,BF,Limita1),
expandeaza([N|Drum],A,Limita1,A1,Rez1,Sol),
continua(Drum,t(N,F/G,[A1|As]),Limita,Arb1,
Rez1,Rez,Sol).

expandeaza(_,t(_,_,[]),_,_,imposibil,_):-!.


expandeaza(_,Arb,Limita,Arb,nu,_):-
f(Arb,F),
F>Limita.


%continua(+Drum,+Arb,+Limita,-Arb1,-Rez1,-Rez,-Sol)

continua(_,_,_,_,da,da,Sol).

continua(P,t(N,F/G,[A1|As]),Limita,Arb1,nu,Rez,Sol):-
insereaza(A1,As,NAs),
cea_mai_buna_f(NAs,F1),
expandeaza(P,t(N,F1/G,NAs),Limita,Arb1,Rez,Sol).

continua(P,t(N,F/G,[_|As]),Limita,Arb1,imposibil,Rez,
Sol):-cea_mai_buna_f(As,F1),
expandeaza(P,t(N,F1/G,As),Limita,Arb1,Rez,Sol).


%listasucc(+G,+Succesori,-Arbore)
listasucc(_,[],[]).

listasucc(G0,[N/C|NCs],Ts):-
G is G0+C,
h(N,H),
F is G+H,
listasucc(G0,NCs,Ts1),
insereaza(l(N,F/G),Ts1,Ts).


%insereaza(+Arb,+ListArb, -ListArbrez)
insereaza(A,As,[A|As]):-
f(A,F),
cea_mai_buna_f(As,F1),
F=<F1,!.

insereaza(A,[A1|As],[A1|As1]):-insereaza(A,As,As1).

%min(+X,+Y,-M)
min(X,Y,X):-X=<Y,!.
min(_,Y,Y).

%f(+Arb, -F)
f(l(_,F/_),F). 
f(t(_,F/_,_),F). 

%cea_mai_buna_f(+Lista,-F)
cea_mai_buna_f([A|_],F):-f(A,F).
cea_mai_buna_f([],999999).




%membru(+Element,+Lista)
membru(H,[H|_]).
membru(X,[_|T]):-membru(X,T).