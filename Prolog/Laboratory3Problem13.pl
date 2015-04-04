/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 04.05.2014
*/

/* This program counts how many creatures there are in a list. */

/*
We go through the list, element by element.
Each element is a creature.
We use functor to obtain information regarding the element.
For the creature H we get the name of the creature ( NameOH, example: cat('catName'), NameOfH will be cat ).
We check to see if fact(NameOfH , Counter) exists in our knowledge base.
If it does not exist, we assert it, with Counter = 1, creating in our knowledge base the entry: fact(NameOfH,1).
If it exists, that is if we already came aross a creature of the same kind, we retract the fact
telling us we met it Count times and assert a new fact, telling us we met that creature in the list Count+1 times.
When all creatures in the list are examined, that is we have an empty list, we call the count predicate which
returns a list of lists of the form: [ [creature1 , 1] , [creature2 , 3] , [creature3 , 2] ] meaning  there was 1 creature1,
three creature2 and two creature3.  
*/

:-dynamic ( fact )/2.

count(L) :-  setof([X,Y],fact(X,Y),L).

afiseaza_fiinte([]) :- count(L) , write(L).
afiseaza_fiinte([H|T]) :- functor(H,NameOfH,_) , ( ( fact(NameOfH,Counter) )->( retract(fact(NameOfH,Counter)) , Counter1 is Counter + 1 , assert( fact(NameOfH,Counter1) )) ; ( assert( fact(NameOfH,1) ) ) )  , afiseaza_fiinte(T).

/* Queries */

/*
afiseaza_fiinte([catel(azorel), pisica(mitza), om(ionel, elev), om(liliana, profesoara), catel(pufisor), catel(gogo), om(gigel, elev), pisica(tom)]).
[[catel,3],[om,3],[pisica,2]]
yes
*/