/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina, 
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/

/* 
Pseudo-Author / Modificator: Mandrescu Mihai Petru 
Grupa: 242
Data: 28.05.2014
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

%rezolva1_d(+Nod,-DrumSolutie)
rezolva1_d(N,Sol):-depthfirst([],N,Sol).

%depthfirst(+Drum,+Nod, -Solutie)
depthfirst(Drum, Nod, [Nod|Drum]):-scop(Nod).
depthfirst(Drum, Nod, Sol):- write('Stiva actuala: '), write([Nod|Drum]), nl,
			s(Nod,Nod1),
			\+ (membru(Nod1,Drum)),
            write('Se adauga nodul: '), write(Nod1), nl , nl,
			depthfirst([Nod|Drum],Nod1, Sol).
            
/* Interogari: */
/*
 rezolva1_d(a,Sol).                                               
Stiva actuala: [a]
Se adauga nodul: b

Stiva actuala: [b,a]
Se adauga nodul: c

Stiva actuala: [c,b,a]
Se adauga nodul: d

Stiva actuala: [d,c,b,a]
Se adauga nodul: g

Stiva actuala: [g,d,c,b,a]
Se adauga nodul: h

Stiva actuala: [h,g,d,c,b,a]
Se adauga nodul: e

Stiva actuala: [e,h,
*/