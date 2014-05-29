/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina, 
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/

/* 
Pseudo-Author / Modificator: Mandrescu Mihai Petru 
Grupa: 242
Data: 29.05.2014
*/

/*
Aici am construit succesorii.
Pentru fiecare nod, am scris vecinii acestuia in al doilea parametru a faptului s/2.
Am definit nodurile scop ca fiind 'i' si 'f'.
*/
s(a,b).

s(b,a).
s(b,c).
s(b,i).

s(c,b).
s(c,d).

s(d,c).
s(d,g).
s(d,e).

s(e,d).
s(e,f).
s(e,h).

s(f,e).

s(g,d).
s(g,h).

s(h,g).
s(h,e).

scop(i).
scop(f).


%membru(+Element,+Lista)
membru(H,[H|_]).
membru(X,[_|T]):-membru(X,T).

%cale(+Nod,-NodScop,-Solutie).
cale(Nod,Nod,[Nod]).
cale(NodInitial,NodUltim, [NodUltim|Drum]):-
cale(NodInitial,NodPenultim, Drum),
s(NodPenultim,NodUltim),
write('Testeaza solutie: ') , write([NodUltim|Drum]) ,nl,
( (scop(NodUltim) , write('Da'), nl);(\+scop(NodUltim) , write('Nu'), nl) ),
write('Extinde: ') , write(NodUltim) ,nl, nl,
\+ membru(NodUltim,Drum).

%depthfirst_iterative_deepening(+NodStart, -Solutie)
depthfirst_iterative_deepening(NodStart, Sol):- cale(NodStart,NodScop,Sol),scop(NodScop),!.

/* Interogari */
/*
depthfirst_iterative_deepening(a,S).                                 
Testeaza solutie: [b,a]
Nu
Extinde: b

Testeaza solutie: [b,a]
Nu
Extinde: b

Testeaza solutie: [a,b,a]
Nu
Extinde: a

Testeaza solutie: [c,b,a]
Nu
Extinde: c

Testeaza solutie: [i,b,a]
Da
Extinde: i

S = [i,b,a] ? y
*/