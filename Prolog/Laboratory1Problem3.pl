/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

membru(ionel,echipa1).
membru(gigel,echipa1).
membru(danel,echipa2).
membru(tudorel,echipa2).
adversari(X,Y):- membru(X,Z1), membru(Y,Z2), Z1 \== Z2.
colegi(X,Y):- membru(X,Z1), membru(Y,Z2), Z1 == Z2, X \== Y.

/*
Problema:

colegi(X,Y).
X = ionel,
Y = ionel 

Rezolvata prin:

X \== Y.

colegi(X,Y).                                                             
X = ionel,       
Y = gigel ? y
yes
*/