/*
Author: Mandrescu Mihai Petru.
Group: 242.
Date: 01.05.2014
*/

/*
cod preluat din cartea(bibliografie[1]):
BALCAN Maria Florina, HRISTEA Florentina, 
Aspecte ale Cautarii si Reprezentarii Cunostintelor in Inteligenta Artificiala,
Editura Universitatii din Bucuresti, 2004
*/

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
				extinde(Drum, DrumuriNoi),
				concat(Drumuri, DrumuriNoi, Drumuri1),
				breadthfirst(Drumuri1, Sol).

%extinde(+StareDrum,-ListaDrumuriDerivate)
extinde([Nod|Drum],DrumuriNoi):-
				bagof([NodNou,Nod|Drum], (s(Nod,NodNou), \+(membru(NodNou,[Nod|Drum]))),
				DrumuriNoi),
				!.
extinde(_,[]).

%rezolva1_d(+Nod,-DrumSolutie)
rezolva1_d(N,Sol):-depthfirst([],N,Sol).

%depthfirst(+Drum,+Nod, -Solutie)
depthfirst(Drum, Nod, [Nod|Drum]):-scop(Nod).
depthfirst(Drum, Nod, Sol):-
			s(Nod,Nod1),
			\+ (membru(Nod1,Drum)), 
			depthfirst([Nod|Drum],Nod1, Sol).
            
s(ListStiveV,ListStiveN) :- ia_bloc(ListStiveV,B,ListStiveAux,PozBVeche),pune_bloc(ListStiveAux,B,PozBVeche,ListStiveN).
                                        
ia_bloc([ [B|TStiva]|RestulDeStive ],B,[TStiva|RestulDeStive],0).
ia_bloc([Stiva|RestulDeStive],B,[Stiva|RestulDeStiveNecunoscut],PozBVeche) :- ia_bloc(RestulDeStive,B,RestulDeStiveNecunoscut,PozBVeche1),PozBVeche is PozBVeche1 + 1.

pune_bloc([Stiva|RestulDeStive],B,PozB,[ [B|Stiva]|RestulDeStive ]) :- PozB \== 0.
pune_bloc([Stiva|RestulDeStive],B,PozB,[Stiva|RestulDeStiveNecunoscut]) :-PozB1 is PozB - 1, pune_bloc(RestulDeStive,B,PozB1,RestulDeStiveNecunoscut).

scop([ [d,c],[a],[b] ]).

afisareElem([]).
afisareElem([H|T]) :- afisareElem(T),afisListaStive(H),nl.

pb_bloc(StInit) :- rezolva_b(StInit,Sol),afisareElem(Sol).

leng([],0).
leng([_|T],N) :- leng(T,N1), N is N1+1.

maxLen([],0).
maxLen([Stiva|RestStive],Max) :- maxLen(RestStive,MaxRest),leng(Stiva,Lg),((Lg>MaxRest)->(Max=Lg);(Max = MaxRest)).

afisNiv([[B|Stiva]|RestStive],Nivel,[Stiva|RestStive1]) :- leng([B|Stiva],NivelC), NivelC == Nivel,!,write(' '),write(B), afisNiv(RestStive,Nivel,RestStive1).
afisNiv([Stiva|RestStive],Nivel,[Stiva|RestStive1]) :- write('  '),afisNiv(RestStive,Nivel,RestStive1).
afisNiv([],_,[]) :- nl.

write_n(_,0).
write_n(C,N) :- write(C), N1 is  N-1, write_n(C,N1).

afisNivele(LStive,0) :- leng(LStive,NrStiva), NrElem is 2*NrStiva + 1, write_n('-',NrElem),nl.
afisNivele(LStive,Nivel) :- afisNiv(LStive,Nivel,LStiveNou),(Nivel > 0, Nivel1 is Nivel-1),afisNivele(LStiveNou,Nivel1).

afisListaStive(ListaStive) :- maxLen(ListaStive,Nmax), afisNivele(ListaStive,Nmax).