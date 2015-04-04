/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 05.05.2014
*/

/* This problem mimics a for loop. */

/*
First, we check if we are at the End. If we care, the program tries to perform the specified action.
However, because we also added \+Action, succes is not required.
There are no additional instructions in the terminal case predicate so the program will halt.
In the non terminal case, again, we try to perform the action but are not bound by it.
We increment the current index ( Start ) and the new index, I is used to call
the forLoop again.
*/

forLoop(End,End,Action) :- Action;\+Action.
forLoop(Start,End,Action) :- (Action;\+Action) , I is Start+1 , forLoop(I,End,Action).

/* Queries */
/*
forLoop(0,5,write(1)).
111111
yes
*/