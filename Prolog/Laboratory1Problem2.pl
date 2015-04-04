/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

mmicnr(X1,X2):- X1 < X2.
mmarenr(X1,X2):- X1 > X2.
mmicenr(X1,X2):- X1 =< X2.
mmareenr(X1,X2):- X1 >= X2.
egalexp(X1,X2):- X1 =:= X2.
diferitexp(X1,X2):- X1 =\= X2.
egalterm(X1,X2):- X1 == X2.
diferitterm(X1,X2):- X1 \== X2.

mmicterm(X1,X2):- X1 @< X2.
mmareterm(X1,X2):- X1 @> X2.
mmiceeterm(X1,X2):- X1 @=< X2.
mmareeterm(X1,X2):- X1 @>= X2.

/*
 ?- egalterm(2+3,5*1).
no

 ?- egalexp(2+3,5*1).
yes

Termenul '2+3' este diferit de termul '5*1'. Operatorul '==' verfica egalitatea de termeni.
Ca expresie, evaluate sunt egale, de aceea operatorul '=:=', aritmetic, le vede ca fiind egale.
*/