/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 03.05.2014
*/

/*
This problem mimics the switch statement found in imperative languages.
*/

/*
First, we define the ':::' operator.
The precedence was set randomly.
In the switch predicate, we assert, that is create a fact. If X is, say, 10, we shall have in the knowledge base fact(10).
Secondly, we 'run' H, which is of the form A ::: B. It does not matter what B is since the program will see the ':::' operator
and run according to it.
Running H is actually computing A ::: B.
When computing ':::' the program will look for fact(A). If A has the same value as X, it will find
the fact, in which case B is executed. Afer execution, the fact is removed from the knowledge base.
In case fact(A) is not in the knowledge base at the time, B is not executed and a 'no' is returned.
This serves in the if statement H is placed in. If H does not return 'no', ie B was executed, we write a new line.
Otherwise, if 'no' is returned, we know we did not find the corect case so we contiune 'going down' the list
in search for other cases.
In the end of the list is reached, we print default.
*/

:- op(100,xfx,:::).

A ::: B :- fact(A) , B , retract( fact(A) ).

switch(X,[]) :- write('Default.').
switch(X,[H|T]) :- assert( fact(X) ) , (H)->(nl);(switch(X,T)). 

/* Queries: */

/*
switch(1,[1:::write(4), 2 ::: write(678)]).                               4        
yes
| ?- switch(2,[1:::write(4), 2 ::: write(678)]).
678

switch(1, [1 ::: write(miau-miau),2 ::: listing, 3 ::: (Rez is X*X,format('Rez este ~d',[Rez]),nl)]).
miau-miau
true ? y
yes
| ?- switch(2, [1 ::: write(miau-miau),2 ::: listing, 3 ::: (Rez is X*X,format('Rez este ~d',[Rez]),nl)]).
A:::B :-
        pred(A),
        call(user:B),
        retract(user:pred(A)).

pred(2).
pred(2).
pred(2).
pred(2).
pred(2).
pred(2).
*/
