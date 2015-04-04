/*
Author : Mandrescu Mihai Petru
Group: 242
Date: 29.05.2014
*/

/*
Pentru ca nu am avut la dispozitie codul de la laborator, am incercat sa
fac problema folosind tutoriale de pe internet.
Am folosit urmatoarele tutoriale:

http://www.csee.umbc.edu/courses/771/current/presentations/prolog%20search.pdf ( Secvente de cod au fost preluate de aici )
http://www.cse.unsw.edu.au/~billw/cs9414/notes/mandc/mandc.html
http://learnfrommike.blogspot.ro/2012/09/solving-missionaries-and-cannibals.html
*/

/*
Starea este de forma: [CL,ML,B,CR,MR]
CL  - Canibali Stanga ( Left )
ML - Misionari Stanga
B    - Mal ( Bank )
CR , MR - Analog  CL si ML pentru dreapta ( Right )
*/
start([3,3,left,0,0]).
goal([0,0,right,3,3]).

/* Verificarea corectitudinii unei miscari */
legal(CL,ML,CR,MR) :- ML>=0, CL>=0, MR>=0, CR>=0, (ML>=CL ; ML=0), (MR>=CR ; MR=0).

/* Miscarile Posibile, presupunand ca barca are doua locuri */

/* Stanga spre dreapta */

/* Doi misionari */
move([CL,ML,left,CR,MR],[CL,ML2,right,CR,MR2]) :- MR2 is MR+2, ML2 is ML-2, legal(CL,ML2,CR,MR2).

/* Doi canibali */
move([CL,ML,left,CR,MR],[CL2,ML,right,CR2,MR]) :- CR2 is CR+2, CL2 is CL-2, legal(CL2,ML,CR2,MR).

/* Un misionar si un canibal */
move([CL,ML,left,CR,MR],[CL2,ML2,right,CR2,MR2]) :- CR2 is CR+1, CL2 is CL-1, MR2 is MR+1, ML2 is ML-1, legal(CL2,ML2,CR2,MR2).

/* Un misionar */
move([CL,ML,left,CR,MR],[CL,ML2,right,CR,MR2]) :- MR2 is MR+1, ML2 is ML-1, legal(CL,ML2,CR,MR2).

/* Un canibal */
move([CL,ML,left,CR,MR],[CL2,ML,right,CR2,MR]) :- CR2 is CR+1, CL2 is CL-1, legal(CL2,ML,CR2,MR).

/* Analog Dreapta spre stanga */

move([CL,ML,right,CR,MR],[CL,ML2,left,CR,MR2]) :- MR2 is MR-2, ML2 is ML+2, legal(CL,ML2,CR,MR2).

move([CL,ML,right,CR,MR],[CL2,ML,left,CR2,MR]) :- CR2 is CR-2, CL2 is CL+2, legal(CL2,ML,CR2,MR).

move([CL,ML,right,CR,MR],[CL2,ML2,left,CR2,MR2]) :- CR2 is CR-1, CL2 is CL+1, MR2 is MR-1, ML2 is ML+1, legal(CL2,ML2,CR2,MR2).

move([CL,ML,right,CR,MR],[CL,ML2,left,CR,MR2]) :- MR2 is MR-1, ML2 is ML+1, legal(CL,ML2,CR,MR2).

move([CL,ML,right,CR,MR],[CL2,ML,left,CR2,MR]) :- CR2 is CR-1, CL2 is CL+1, legal(CL2,ML,CR2,MR).

/* Apelul recursiv - alege o miscare si verifica sa nu fie Explorata deja. */
path([CL1,ML1,B1,CR1,MR1],[CL2,ML2,B2,CR2,MR2],Explored,MovesList) :- move([CL1,ML1,B1,CR1,MR1],[CL3,ML3,B3,CR3,MR3]), \+(member([CL3,ML3,B3,CR3,MR3],Explored)), path([CL3,ML3,B3,CR3,MR3],[CL2,ML2,B2,CR2,MR2],[[CL3,ML3,B3,CR3,MR3]|Explored],[ [[CL3,ML3,B3,CR3,MR3],[CL1,ML1,B1,CR1,MR1]] | MovesList ]).

/* O solutie a fost gasita , se apeleaza apfisarea */
path([CL,ML,B,CR,MR],[CL,ML,B,CR,MR],_,MovesList) :- output(MovesList).

/* Afisarea */
output([]) :- nl.
output([[A,B]|MovesList]) :- output(MovesList), write(B), write(' -> '), write(A), nl.

/* Apel catre predicatul principal 'path' . Se apeleaza cu [3,3,left,0,0] adica 3 canibali si 3 misionari in stanga cu scopul [0,0,right,3,3] adica 3 canibali si 3 misionari in dreapta iar prima configuratie este [3,3,left,0,0] */
find :- write('Initial: Canibals - Missionaries - Side <---> After Move: Canibals - Missionaries - Side ') , nl , path([3,3,left,0,0],[0,0,right,3,3],[[3,3,left,0,0]],_).

/* Queries: */
/*
Initial: Canibals - Missionaries - Side <---> After Move: Canibals - Missionaries - Side 

[3,3,left,0,0] -> [1,3,right,2,0]
[1,3,right,2,0] -> [2,3,left,1,0]
[2,3,left,1,0] -> [0,3,right,3,0]
[0,3,right,3,0] -> [1,3,left,2,0]
[1,3,left,2,0] -> [1,1,right,2,2]
[1,1,right,2,2] -> [2,2,left,1,1]
[2,2,left,1,1] -> [2,0,right,1,3]
[2,0,right,1,3] -> [3,0,left,0,3]
[3,0,left,0,3] -> [1,0,right,2,3]
[1,0,right,2,3] -> [1,1,left,2,2]
[1,1,left,2,2] -> [0,0,right,3,3]
yes
*/