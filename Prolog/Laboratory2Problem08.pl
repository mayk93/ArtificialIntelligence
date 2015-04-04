/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 26.04.2014
*/

numar(4).
numar(-2).
numar(0).
numar(8). 

getAnswer(Z,exista):- numar(Z).
getAnswer(Z,nu_exista) :- \+numar(Z).

list_str([],[]).

list_str( [sum(X,Y)|T],[exp(X+Y=Z,Exist)|Texp] ) :- Z is X+Y, 
                                                                            getAnswer(Z,Exist),
                                                                            list_str(T,Texp).
                                                                            
list_str( [dif(X,Y)|T],[exp(X-Y=Z,Exist)|Texp]) :- Z is X-Y, 
                                                                       getAnswer(Z,Exist), 
                                                                       list_str(T,Texp).

list_str( [prod(X,Y)|T],[exp(X*Y=Z,Exist)|Texp] ) :- Z is X*Y, 
                                                                            getAnswer(Z,Exist), 
                                                                            list_str(T,Texp).

/* Queries */

/*
| ?- list_str([sum(5,3), prod(2,3),dif(4,5),dif(3,3), prod(2,2),sum(1,1)],L).
L = [exp(5+3=8,exista),exp(2*3=6,nu_exista),exp(4-5= -1,nu_exista),exp(3-3=0,exista),exp(2*2=4,exista),exp(1+1=2,nu_exista)] 
*/