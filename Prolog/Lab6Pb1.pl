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

%concat(+Lista1,+Lista2,-Listarez)
concat([],L,L).
concat([H|T],L,[H|T1]):-concat(T,L,T1).

%membru(+Element,+Lista)
membru(H,[H|_]).
membru(X,[_|T]):-membru(X,T).

%rezolva_b(+Start,- Sol)
rezolva_b(Start, Sol):-breadthfirst([[Start]],Sol).

%breadthfirst(+Listadrumuri,-DrumSolutie)
breadthfirst([[Nod|Drum]|_], [Nod|Drum]):- scop(Nod).
breadthfirst([Drum|Drumuri], Sol) :- 
                write('Coada actuala: ') , write([Drum|Drumuri]), nl, /* Coada actuala sunt Drumurile. De exemplu, am putea avea drumul [c,b,a] ( adica a->b->c ) sau [i,b,a]. [c,b,a] este verificat prima oara deoarece s(b,c) apare inainte de s(b,i). */
                write('Se extinde drumul: '), write(Drum), nl, /* Extindem primul drum din coada. */
				extinde(Drum, DrumuriNoi),
				concat(Drumuri, DrumuriNoi, Drumuri1),
                write('Se adauga in coada: ') , write(DrumuriNoi), nl, nl, /* Rezultatul extinderii este adaugat cozii. */
				breadthfirst(Drumuri1, Sol).

%extinde(+StareDrum,-ListaDrumuriDerivate)
extinde([Nod|Drum],DrumuriNoi):-
				bagof([NodNou,Nod|Drum], (s(Nod,NodNou), \+(membru(NodNou,[Nod|Drum]))),
				DrumuriNoi),
				!.
extinde(_,[]).

/* Interogari: */
/*
rezolva_b(a,Sol).                                                
Coada actuala: [[a]]
Se extinde drumul: [a]
Se adauga in coada: [[b,a]]

Coada actuala: [[b,a]]
Se extinde drumul: [b,a]
Se adauga in coada: [[c,b,a],[i,b,a]]

Coada actuala: [[c,b,a],[i,b,a]]
Se extinde drumul: [c,b,a]
Se adauga in coada: [[d,c,b,a]]

Sol = [i,b,a] ? y
yes
*/