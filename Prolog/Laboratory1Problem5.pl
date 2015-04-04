/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

copil(ion).
copil(ana).
copil(mihai).
copil(alina).
fata(ana).
fata(alina).
baiat(X):- copil(X) , \+ (fata(X)).

/*
Problema era ca presupuneam ca tot ce nu e fata e baiat.
Trebuie sa verificam ca e si copil.

baiat(ion).
yes
*/