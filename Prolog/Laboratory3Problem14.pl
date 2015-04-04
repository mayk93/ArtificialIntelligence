/*
list_ingrediente('salata de rosii',[c(rosii, 1, kg), c(ceapa, 0.25, kg), c(ulei, 150, ml), c(marar, 0.05, kg), c(sare, 0.01, kg)]).
list_ingrediente('ardei umpluti',[c(rosii, 0.5, kg),c(ardei, 8, buc), c(orez, 0.5, kg), c(patrunjel, 0.05, kg), c(ceapa, 0.25, kg), c(ulei, 200, ml), c(sare, 0.01, kg), c(ciuperci, 1, kg)]).
list_ingrediente('ciuperci_prajite',[c(patrunjel, 0.05, kg), c(ceapa, 0.2, kg), c(ulei, 150, ml), c(sare, 0.02, kg), c(ciuperci, 1.5, kg)]).
list_ingrediente('pilaf',[c(orez, 0.5, kg),c(patrunjel, 0.05, kg), c(ceapa, 0.3, kg), c(ulei, 100, ml), c(sare, 0.02, kg)]).
list_ingrediente('humus',[c(naut, 0.5, kg),c(patrunjel, 0.05, kg), c(ulei, 200, ml), c(sare, 0.03, kg)]). 

assertAllIngredientsAux([],_).

assertAllIngredientsAux([H|T], NrR) :-  c(IngNum, Cant, Unm) = H , ( ingredient(IngNum,Cantitate, Unm),\+var(Cantitate) )->(   NewCant is NrR*Cant+Cantitate , retract(ingredient(IngNum, Cantitate, Unm) ) , assert( ingredient(IngNum, NewCant, Unm) ) );( assert( ingredient(IngNum, Cant, Unm) ) ) , assertAllIngredientsAux(T , NrR).

assertAllIngredients([H|T], NrR) :-c(IngNum, Cant, Unm) = H, NewCant is NrR*Cant ,assert(ingredient(IngNum,NewCant,Unm)), assertAllIngredientsAux(T, NrR).

lista_cumparaturiAux([ ],_).

lista_cumparaturiAux([H|T], NrR) :-list_ingrediente(Ret,Lst), assertAllIngredientsAux(Lst, NrR), lista_cumparaturiAux(T,NrR).

lista_cumparaturi([H|T]) :- (Ret,NrR) = H, list_ingrediente(Ret,Lst), assertAllIngredients(Lst,NrR), lista_cumparaturiAux(T, NrR).
*/

list_ingrediente('salata de rosii',[c(rosii, 1, kg), c(ceapa, 0.25, kg), c(ulei, 150, ml), c(marar, 0.05, kg), c(sare, 0.01, kg)]).
list_ingrediente('ardei umpluti',[c(rosii, 0.5, kg),c(ardei, 8, buc), c(orez, 0.5, kg), c(patrunjel, 0.05, kg), c(ceapa, 0.25, kg), c(ulei, 200, ml), c(sare, 0.01, kg), c(ciuperci, 1, kg)]).
list_ingrediente('ciuperci_prajite',[c(patrunjel, 0.05, kg), c(ceapa, 0.2, kg), c(ulei, 150, ml), c(sare, 0.02, kg), c(ciuperci, 1.5, kg)]).
list_ingrediente('pilaf',[c(orez, 0.5, kg),c(patrunjel, 0.05, kg), c(ceapa, 0.3, kg), c(ulei, 100, ml), c(sare, 0.02, kg)]).
list_ingrediente('humus',[c(naut, 0.5, kg),c(patrunjel, 0.05, kg), c(ulei, 200, ml), c(sare, 0.03, kg)]). 

getIngredientsMultiplied([],_,[]).
getIngredientsMultiplied([H|T],NrReteta,OutPut) :- c(Tip , Cantitate, UnitMsr) = H , T1 = Tip , C1 is Cantitate *NrRetea , UM1 = UnitMsr, [(T1,C1,UM1)|OutPut1] , getIngredientsMultiplied(T,NrReteta,Output1).

sum([H1|L1],[H2|L2],[Hr|Lr]) :- (Nume1) 

lista_cumparaturi([],[]).
lista_cumparaturi([H|T] , OldResult) :- (Reteta,NrReteta) = H , list_ingrediente(Reteta , ListaDeIng) , getIngredientsMultiplied(ListaDeIng,NrReteta,OutPut) , lista_cumparaturi(T,Result) , sum(OutPut,OldResult,Result).