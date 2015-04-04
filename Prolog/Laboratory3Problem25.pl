/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 03.05.2014
*/

/* This program is an RPG duel simulator. */

/* These are two operators, duel to determine based on the given rules the winner an castigator_este to fetch the winner. */
:-op(100,xfy,duel).
:-op(100,xfy,castigator_este).

test(R):-jucator(_,_,_,_,_) = R.

/*
Here we retriev information on the two players in order to determine their score.
The score determines the winner.
The players of the winner is also updated in accordance with the game rules.
Z will be the winner.
*/
Z castigator_este Y :- test(Y), Z = Y.
Z castigator_este X duel Y :- call(Z1 castigator_este Y),jucator(Jucator1,Forta_jucator1,Magie_jucator1,Inteligenta_jucator1,Sanatate_jucator1) = X,
                              jucator(Jucator2,Forta_jucator2,Magie_jucator2,Inteligenta_jucator2,Sanatate_jucator2) = Z1,
				              Scor_jucator1 is ((Forta_jucator1 + Magie_jucator1)/2+Inteligenta_jucator1) * Sanatate_jucator1/100,
                              Scor_jucator2 is ((Forta_jucator2 + Magie_jucator2)/2+Inteligenta_jucator2) * Sanatate_jucator2/100,
				              ((Scor_jucator1 > Scor_jucator2,New_hp is round(Sanatate_jucator1 - Scor_jucator2/Scor_jucator1*10),Z = jucator(Jucator1,Forta_jucator1,Magie_jucator1,Inteligenta_jucator1,New_hp));
							   (Scor_jucator1 < Scor_jucator2, New_hp is round(Sanatate_jucator2 - Scor_jucator1/Scor_jucator2*10),Z = jucator(Jucator2,Forta_jucator2,Magie_jucator2,Inteligenta_jucator2,New_hp))).
							  

/* +++ is '+u+'. We use it to increment the value of every attribute except health. */                   
:-op(100,fy,'+++').
:-op(100,xfy,nivel_nou).

J nivel_nou X :- test(X), J = X.					   
J nivel_nou '+++' X :- call(J1 nivel_nou X),jucator(Jucator,Forta,Magie,Inteligenta,Sanatate) = J1,
                       Forta_new is round(Forta + Forta * 0.1),
					   Magie_new is round(Magie + Magie * 0.1),
					   Inteligenta_new is round(Inteligenta + Inteligenta * 0.1),
					   J = jucator(Jucator,Forta_new,Magie_new,Inteligenta_new,Sanatate).

/* Here we increment the health by Y, where Y is the ammount of water drank by the player. */							   
:-op(100,yfx,bea).
:-op(100,xfy,se_vindeca).

J se_vindeca X :- test(X), J = X.
J se_vindeca X bea Y :- call(J1 se_vindeca X),jucator(Jucator,Forta,Magie,Inteligenta,Sanatate) = J1,
                        Sanatate_new is Sanatate + Y,
						J = jucator(Jucator,Forta,Magie,Inteligenta,Sanatate_new).
						
for(N2,N2,Scop):-Scop;\+Scop.						
for(N1,N2,Scop):-(Scop;\+Scop),N3 is N1+1,for(N3,N2,Scop).


/* Queries */

/*
Z castigator_este jucator(ion,100,50,14,50) duel jucator(bob,100,50,14,40) duel jucator(gogu,40,20,100,80).
Z = jucator(gogu,40,20,100,73) ? y
yes

J nivel_nou '+++' '+++' jucator(ion,100,50,14,50).      
J = jucator(ion,121,61,17,50) ? y
yes
*/