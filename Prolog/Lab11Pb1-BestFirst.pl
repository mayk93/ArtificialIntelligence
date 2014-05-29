/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina, 
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/

/*
Pseudo-Author / Modificator : Mandrescu Mihai Petru
Grupa: 242
Data: 29.05.2014
*/

s(a,b,7).
s(a,c,4).
s(a,d,5).
s(b,f,6).
s(b,g,3).
s(g,i,2).
s(g,j,3).
s(c,b,2).
s(c,e,8).
s(c,f,5). 
s(d,e,5).
s(d,h,11).
s(e,f,4).
s(e,h,6).
s(f,h,10).

h(b,9).
h(c,10).
h(d,11).
h(e,6).
h(f,10). 
h(g,6).
h(i,4).
h(j,3).
h(h,0).

scop(h).

%bestfirst(+Nod_initial,-Solutie)
bestfirst(Nod_initial,Solutie):-
expandeaza([],l(Nod_initial,0/0),9999999,_,
da,Solutie).

%expandeaza(+Drum,+Arbore,+Limita,-A1,-Rezultat,-Solutie),

expandeaza(Drum,l(N,_),_,_, da,[N|Drum]) :- scop(N) , write('Scop atins'), nl.

expandeaza(Drum,l(N,F/G),Limita,Arb1,Rez,Sol):-
write('Se expandeaza frunza: ') , write(N) , write('('), write(F), write('/') , write(G), write(')'), nl ,
write('Se expandeaza subarborele: '), write(Drum), nl, nl,
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

/* Interofari */
/*
 bestfirst(a,S).                                                           Se expandeaza frunza: a(0/0)
Se expandeaza subarborele: []

Se expandeaza frunza: c(14/4)
Se expandeaza subarborele: [a]

Se expandeaza frunza: b(15/6)
Se expandeaza subarborele: [c,a]

Se expandeaza frunza: g(15/9)
Se expandeaza subarborele: [b,c,a]

Se expandeaza frunza: i(15/11)
Se expandeaza subarborele: [g,b,c,a]

Se expandeaza frunza: j(15/12)
Se expandeaza subarborele: [g,b,c,a]

Se expandeaza frunza: b(16/7)
Se expandeaza subarborele: [a]

*/