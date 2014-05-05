/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 05.05.2014
*/

/* This program changes the structure of a prolog fact. Given the fact as a name and grades to different subjects, the programme replaces the grades with the average. */

/*
The main predicate, medie_elev, generates a list of all the names of the students in the fact base. This list is used to retrieve information, such as the grades,
in the makeAverage predicate.
Using the name, we get, for each student, his grades. We input them in the calculateAverage predicate, that returns the arithmetic mean of the three numbers.
We retract the old 'elev' structure and assert a new one, using the Name and Avg. 
*/

:- dynamic elev/7.

elev(ion, matematica, 4, romana, 10, informatica, 8).
elev(petre, matematica, 8, romana, 2, informatica, 9).
elev(simona, matematica, 10, romana, 10, informatica, 10).
elev(bogdan, matematica, 2, romana, 3, informatica, 4).
elev(andreea, matematica, 9, romana, 7, informatica, 8).

/* Here we add another fact. Because we declared it dynamic, we use assert. */
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