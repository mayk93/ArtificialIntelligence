/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 30/04/2014 */

isMember(X,[]) :- fail.
isMember(X,[X|_]).
isMember(X,[H|T]) :- isMember(X,T).