/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 30/04/2014 */

/* This program generates a bouquet of flowers based on a set of rules.   */

/* Help predicate: */
/* help(+X) */

help(X) :- write('buchet(+B)').

/* Corner Cases: */
/* corner(X) */

corner(X) :- write('None.').

/*
The bouquet is hard coded.
The generate either 3, 5 or 7 flowers, add them to a list and assign the list to B.
*/

:- use_module(library(random)).
:- use_module(library(lists)).

floare(lalea, galben, 3).%celelalte 3 sunt sepale, nu petale, pt curiosi :)
floare(lalea, rosu, 3).
floare(margareta, alb, 20).
floare(liliac, violet, 4).
floare(mac, rosu, 4).
floare(passiflora, alb, 5).
floare(stanjenel, violet, 6).
floare(orhidee,alb, 3).
floare(ghiocel,alb, 3).
floare(garoafa,alb, 31).
floare(garoafa,roz, 31).
floare(garoafa,rosu, 31).

etajera(e1,
[[fl(lalea, galben), fl(lalea,galben)],
[fl(garoafa, roz)],
[fl(lalea, rosu), fl(garoafa, rosu), fl(mac, rosu), fl(garoafa, rosu), fl(garoafa, rosu)],
[fl(liliac, violet), fl(stanjenel, violet), fl(stanjenel, violet), fl(liliac, violet), fl(stanjenel, violet)], [fl(margareta, rosu), fl(mac, rosu), fl(mac, rosu), fl(garoafa, rosu)],
[fl(liliac, violet), fl(stanjenel, violet), fl(liliac, violet)],
[fl(passiflora, alb), fl(orhidee, alb), fl(passiflora, alb), fl(ghiocel, alb)],
[fl(garoafa, roz), fl(garoafa, roz), fl(garoafa, roz)],
[fl(margareta, alb), fl(orhidee, alb), fl(passiflora, alb), fl(margareta, alb)]]).

etajera(e2,
[[fl(margareta, rosu), fl(mac, rosu), fl(mac, rosu), fl(garoafa, rosu)],
[fl(liliac, roz), fl(stanjenel, violet), fl(liliac, violet)],
[fl(lalea, galben), fl(lalea,galben)]]).

etajera(e2,
[[fl(ghiocel, alb), fl(ghiocel, alb), fl(margareta, alb)],
[fl(trandafir, roz), fl(garoafa, roz)],
[fl(liliac, violet), fl(liliac, violet), fl(stanjenel, violet)]]).

isMember(X,[]) :- fail.
isMember(X,[X|_]).
isMember(X,[H|T]) :- isMember(X,T).

choose([], []).
choose(List, Elt) :-
        length(List, Length),
        random(0, Length, Index),
        nth0(Index, List, Elt).

getFlowerNotT(NF,T) :-  setof(floare(X,Y,Z) , (floare(X,Y,Z) , X  \== T) , L) , choose(L,NF).
getWhiteFlowerNotT(NF,T) :- setof(floare(X,Y,Z) , (floare(X,Y,Z) , X  \== T, Y == alb) , L) , choose(L,NF).

getNewFlower([],NF) :- setof(floare(X,Y,Z) , floare(X,Y,Z) , L) , choose(L,NF).
getNewFlower([floare(T,C,P)|L],NF) :-  (C = alb)->( getFlowerNotT(NF,T) );( getWhiteFlowerNotT(NF,T) ).

buchet(B) :- ( getNewFlower([],NF0) , getNewFlower([NF0],NF1) , getNewFlower([NF1,NF0],NF2) , B = [NF2,NF1,NF0] );
                    ( getNewFlower([],NF0) , getNewFlower([NF0],NF1) , getNewFlower([NF1,NF0],NF2) , getNewFlower([NF2,NF1,NF0],NF3) , getNewFlower([NF3,NF2,NF1,NF0],NF4) , B = [NF4,NF3,NF2,NF1,NF0] );
                    ( getNewFlower([],NF0) , getNewFlower([NF0],NF1) , getNewFlower([NF1,NF0],NF2) , getNewFlower([NF2,NF1,NF0],NF3) , getNewFlower([NF3,NF2,NF1,NF0],NF4) , getNewFlower([NF4,NF3,NF2,NF1,NF0],NF5) , getNewFlower([NF5,NF4,NF3,NF2,NF1,NF0],NF6) , B = [NF6,NF5,NF4,NF3,NF2,NF1,NF0] ).
                    
/*

buchet(B).
B = [floare(ghiocel,alb,3),floare(orhidee,alb,3),floare(garoafa,rosu,31)] ? ;
B = [floare(passiflora,alb,5),floare(mac,rosu,4),floare(garoafa,alb,31),floare(stanjenel,violet,6),floare(garoafa,alb,31)] ? ;
B = [floare(garoafa,alb,31),floare(margareta,alb,20),floare(garoafa,rosu,31),floare(margareta,alb,20),floare(lalea,galben,3),floare(orhidee,alb,3),floare(garoafa,rosu,31)] ?

*/