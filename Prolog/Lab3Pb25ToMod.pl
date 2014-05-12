%Nume Radu Vlad 242
%Data 02.05.2014


:-op(100,xfy,duel).
:-op(100,xfy,castigator_este).

test(R):-jucator(_,_,_,_,_) = R.

Z castigator_este Y :- test(Y), Z = Y.
Z castigator_este X duel Y :- call(Z1 castigator_este Y),jucator(Jucator1,Forta_jucator1,Magie_jucator1,Inteligenta_jucator1,Sanatate_jucator1) = X,
                              jucator(Jucator2,Forta_jucator2,Magie_jucator2,Inteligenta_jucator2,Sanatate_jucator2) = Z1,
				              Scor_jucator1 is ((Forta_jucator1 + Magie_jucator1)/2+Inteligenta_jucator1) * Sanatate_jucator1/100,
                              Scor_jucator2 is ((Forta_jucator2 + Magie_jucator2)/2+Inteligenta_jucator2) * Sanatate_jucator2/100,
				              ((Scor_jucator1 > Scor_jucator2,New_hp is round(Sanatate_jucator1 - Scor_jucator2/Scor_jucator1*10),Z = jucator(Jucator1,Forta_jucator1,Magie_jucator1,Inteligenta_jucator1,New_hp));
							   (Scor_jucator1 < Scor_jucator2, New_hp is round(Sanatate_jucator2 - Scor_jucator1/Scor_jucator2*10),Z = jucator(Jucator2,Forta_jucator2,Magie_jucator2,Inteligenta_jucator2,New_hp))).
							  
                   
:-op(100,fy,'+++').
:-op(100,xfy,nivel_nou).

J nivel_nou X :- test(X), J = X.					   
J nivel_nou '+++' X :- call(J1 nivel_nou X),jucator(Jucator,Forta,Magie,Inteligenta,Sanatate) = J1,
                       Forta_new is round(Forta + Forta * 0.1),
					   Magie_new is round(Magie + Magie * 0.1),
					   Inteligenta_new is round(Inteligenta + Inteligenta * 0.1),
					   J = jucator(Jucator,Forta_new,Magie_new,Inteligenta_new,Sanatate).
							   
:-op(100,yfx,bea).
:-op(100,xfy,se_vindeca).

J se_vindeca X :- test(X), J = X.
J se_vindeca X bea Y :- call(J1 se_vindeca X),jucator(Jucator,Forta,Magie,Inteligenta,Sanatate) = J1,
                        Sanatate_new is Sanatate + Y,
						J = jucator(Jucator,Forta,Magie,Inteligenta,Sanatate_new).
						
for(N2,N2,Scop):-Scop;\+Scop.						
for(N1,N2,Scop):-(Scop;\+Scop),N3 is N1+1,for(N3,N2,Scop).


/*Interogari

| ?- Z castigator_este jucator(bob,100,50,14,40) duel jucator(gogu,40,20,100,80).
Z = jucator(gogu,40,20,100,77) ? 
yes
| ?- Z castigator_este jucator(bob,100,50,14,40) duel jucator(gogu,40,20,100,80) duel jucator(sttt,23,45,32,56).
Z = jucator(gogu,40,20,100,72) ? 

ÄŽ| ?- J nivel_nou '+++' '+++' '+++' jucator(gogu,43,65,32,64).
J = jucator(gogu,57,87,43,64) ? 
yes

| ?- J se_vindeca jucator(gogu,321,54,12,543) bea 5 bea 6 bea 232.
J = jucator(gogu,321,54,12,786) ? 
yes


*/

					   
					   
					   
