/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

nr_zile(NrL,NrZ) :- NrL is 2 , NrZ is 29.
nr_zile(NrL,NrZ) :- (NrL >= 1 , NrL =< 12) , ( 
                                                                    ( NrL >=1 , NrL =< 7, M is NrL mod 2, ( (M is 0, NrZ is 30) ; (M is 1, NrZ is 31) ) ) ; 
                                                                    ( NrL >=8 , NrL =< 12, M is NrL mod 2, ( (M is 0, NrZ is 31) ; (M is 1, NrZ is 30) ) ) 
                                                                    ).
                                                                    
/*
nr_zile(4,X).
X = 30 ? y
yes
*/