/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 26/04/2014 */

/* This program computes the Nth element of a recursive sequence.   */

/* Help predicate: */
/* help(+X) */

help(X) :- write('s(+Nth,-Result)').

/* Corner Cases: */
/* corner(X) */

corner(X) :- write('s(0,R) and s(1,R) because they are precomputed.').

/* --- Interface --- */
/*
getLastDigit(+Number,-LastDigit). 

Returns last digit of given number. In the case of positive integers, the last digit is simply the number modulo 10. In the case of negative integers, the remainder of
division by -10 is taken and multiplied by -1.
                                                       
s(0,0) and s(1,3) are the two precomputed elements of the sequence. The first argument ( 0 or 1 ) is the number of the element and the second argument is the value ( 0 and 3 ) .

s(+N,-Result).

First, N1 and N2 are computed. We use them in the recursion. We call s(N1,Test); mathematically meaning Test = s[N-1]. Depending on the absolute value of Test, we either call s(N2,Y) and compute the Result using
the first rule, or call s(N2,X) and compute the result using the second rule. In the case of the second rule, we make use of the getLastDigit predicate.

---
    Prima mea incercare a fost sa fac predicatul s(N,Result) cu if: s(N,Result) :- ( N1 is N-1 , N2 is N-2 , s(N1,Test) ) , (abs(Test) =< 10)->(s(N2,Y) , Result is (2*Test-Y));(s(N2,X) , PreResult is (Test + X) , getLastDigit(PreResult,Result)).
    Insa, aceasta varianta nu functioneaza. Folosind trace am vazut ca nu ajunge niciodata pe else, ci N1 descreste la infinit.
    De ce se intampla asta?
---

*/
/* --- --------- --- */

/* --- Solution --- */
getLastDigit(Number,LastDigit) :- (Number < 0)->( LastDigit is -( mod(Number,-10) ) );( LastDigit is  mod(Number,10) ).
s(0,0).
s(1,3).
s(N,Result) :- ( N1 is N-1 , N2 is N-2 , s(N1,Test) ) , ( (( abs(Test) =< 10 ),( s(N2,Y) , Result is (2*Test-Y) )) ; (( abs(Test) > 10 ),( s(N2,X) , PreResult is (Test + X) , getLastDigit(PreResult,Result) )) ).
/* --- -------- --- */

/* --- Queries --- */

/*
?- s(4,X).                                                                   
X = 12 ? y
yes

---

?- s(10,X).
X = 4 ? y
yes

---
*/