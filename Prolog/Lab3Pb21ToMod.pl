/*
Num Radu Vlad 242
Data 02.05.2014

:-dynamic elev/4.

elev(ion, matematica4, romana10, informatica8).
elev(petre, matematica8, romana2, informatica9).
elev(simona, matematica10, romana10, informatica10).
elev(bogdan, matematica2, romana3, informatica4).
elev(andreea, matematica9, romana7, informatica8).


:-assert(elev(dorel, matematica3,romana3, informatica3)).

medie_elev :-findall(X,elev(X,_,_,_),List),redefine(List). 
redefine([]).
redefine([H|List]):-elev(H,NM,NR,NI), get_avg(NM,NR,NI,Avg),retract(elev(X,NM,NR,NI)),assert(elev(X,medie(Avg))),redefine(List).
get_avg(NM,NR,NI,Avg):-get_mark(NM,MM),get_mark(NR,MR),get_mark(NI,MI),Avg is (MM+MR+MI)/3.
get_mark(X,Y):-name(X,List),get_last(List,Last),Y is Last-48.
get_last([Last],X):-Last=:=48,X = 58;X = Last.
get_last([_|List],Last):-get_last(List,Last).

:-retract(elev(dorel,_,_,_)).
*/

:- dynamic elev/7.

elev(ion, matematica, 4, romana, 10, informatica, 8).
elev(petre, matematica, 8, romana, 2, informatica, 9).
elev(simona, matematica, 10, romana, 10, informatica, 10).
elev(bogdan, matematica, 2, romana, 3, informatica, 4).
elev(andreea, matematica, 9, romana, 7, informatica, 8).

:-assert(elev(gigel, matematica, 10, romana, 8, informatica, 10)).

calculateAverage(X,Y,Z,M) :- Sum is (X+Y+Z) , M is (Sum/3).

makeAverage([]).
makeAverage([Name|L]) :- elev(Name,M,NM,R,NR,I,NI) , calculateAverage(NM,NR,NI,Avg) , retract(elev(Name,M,NM,R,NR,I,NI)) , assert(elev(Name,Avg)) , makeAverage(L).

medie_elev :- findall(Name,elev(Name,_,_,_,_,_,_),L),makeAverage(L).


/* Queries */
/*
| ?- medie_elev.                                                               yes
| ?- listing(elev).
elev(ion, 7.333333333333333).
elev(petre, 6.333333333333333).
elev(simona, 10.0).
elev(bogdan, 3.0).
elev(andreea, 8.0).
elev(gigel, 9.333333333333334).

yes
*/