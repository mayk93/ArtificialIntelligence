/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 26/04/2014 */

/* This program provides information concerning the input.   */

/* Help predicate: */
/* help(+X) */

help(X) :- write('getInformation(+WhateverYouDesire)').

/* Corner Cases: */
/* corner(X) */

/*
For variables is use the built in predicate var. If var(X) is verified, the program outputs Variable.
For numbers, the program checks against integer or float. If either of these is true, the input is a number.
For atoms, the program makes use of the built in predicate atome_codes, that returns a list of ASCII codes for the characters of the string that make up the input.
These codes are used to determine the nature of the character.
The vowels were hard-coded and consonants and other symbols are determined through elimination.
*/

/* ASCII codes */

/* Vowels */
vowel(V) :- (V =:= 65);(V =:= 69);(V =:= 73);(V =:= 79);(V =:= 85)
                  ;
                  (V =:= 97);(V =:= 101);(V =:= 105);(V =:= 111);(V =:= 117).

/* Consonant */
consonant(C) :- ( (C >= 65) , (C =< 122) ),(\+vowel(C)).

/* Other */
other(O) :- ( \+consonant(O) ),( \+vowel(O) ).

countVowels([],0).
countVowels([Hv|T],V) :-  countVowels(T,V1) , ( (vowel(Hv) , V is V1 + 1) ; (\+(vowel(Hv)) , V is V1) ).

countConsonants([],0).
countConsonants([Hc|T],C) :-  countConsonants(T,C1) , ( (consonant(Hc) , C is C1 + 1) ; (\+(consonant(Hc)) , C is C1) ).

countOther([],0).
countOther([Ho|T],O) :-  countOther(T,O1) , ( (other(Ho) , O is O1 + 1) ; (\+(other(Ho)) , O is O1) ).

display(V,C,O) :- write('Vowels: '),write(V),nl,
                          write('Consonants: '),write(C),nl,
                          write('Other: '),write(O),nl.

getInformation(X) :- var(X),write('Variable.').
getInformation(X) :- ( (integer(X));(float(X)) ),write('Number').
getInformation(X) :- atom(X), atom_codes(X,ListOfCodes), countVowels(ListOfCodes,V), countConsonants(ListOfCodes,C), countOther(ListOfCodes,O), display(V,C,O).

/*
getInformation('aeiouAEIOUbcdBCD!@#').
Vowels: 10
Consonants: 6
Other: 3

---

getInformation(X).
Variable.
true ? y

---

getInformation(7).
Number
yes

---

getInformation(7.5).
Number
yes
*/