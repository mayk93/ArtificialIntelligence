/* Author: Mandrescu Mihai Petru, Grupa 242 */
/* Date: 30/04/2014 */

/* This program is about videos and uses AI to produce information regarding these videos.   */

/* Help predicate: */
/* help(+X) */

help(X) :- (X == a , write('Added in code.') );
                (X == b , write('lista_utilizatori(+L)') );
                (X == c , write('clasa_video(-CV,-L)') );
                (X == d , write('autor_apreciat(-A,-C)') );
                (X == e , write('getVideoByViews(_)') );
                (X == f , write('getViewedAndPositiveVideos(-L)') );
                (X == g , write('averageDuration(-AD)') );
                (X == h , write('video_utiliz_implicati(-Struct)') );
                (X == i , write('getVideosOfUser(+User) - Must read input') );
                (X == j , write('getUsersWithLongVideos(+InputList,-L)') );
                (X == k , write('lista_liste_video(-LP)') ).

/* Corner Cases: */
/* corner(X) */

corner(X) :- write('None.').


 /* --- Knowledge Base --- */
%videoclip (titlu, autor, numar_vizualizari, durata in timp(minute), aprecieri_pozitive, aprecieri_negative).
%atentie, durata in timp e data ca numar zecimal de minute, nu minute si secunde

videoclip('pisici zglobii', catworshiper12_a, 200008, 2.20 , 5234,123).
videoclip('ceata lui pitigoi', gradinita10, 150101, 4, 1508, 34).
videoclip('unde a fugit ariciul', gradinita10, 40102, 2.9, 1208, 22).
videoclip('teoria relativitatii', dep_fizica, 2304, 10.7, 105, 10).
videoclip('salvati pisicile', catworshiper12_a, 123008, 4.30 , 5234,123).
videoclip('povestea unui pui de pisica', catworshiper12_a, 204005, 2.20 , 4534,83).
videoclip('justin bieber - o melodie', crazyteen07, 1302718, 3.4 ,12003, 22000).
videoclip('ghost captured on camera', trolololo, 171234, 1.5, 1, 71233).
videoclip('amv - supereroi', lili_andra, 14033, 2.45, 570,33).
videoclip('clipuri anime', lili_andra, 1202, 5.45, 100,100).
videoclip('trailer - batman invata inteligenta artificiala', fmi_hollywood, 2040, 7.8, 2012, 20).
videoclip('justin bieber - alta melodie', crazyteen07, 2401277, 3.5 ,11093, 32123).

/* Point A */

videoclip('pisici dragalase', catworshiper12_a, 190017, 3.39 , 6143,213).

isMember(X,[]) :- fail.
isMember(X,[X|_]).
isMember(X,[H|T]) :- isMember(X,T).

/* Point B */

lista_utilizatori(L) :- setof(A,T^V^D^ApP^ApN^videoclip(T,A,V,D,ApP,ApN),L).

/* Point C */

clasa_video(ClasaVideo,ListaVideoclipuri) :- isMember( ClasaVideo , [apreciat,neapreciat,neutru] ),
                                                                      setof( T , A^V^D^ApP^ApN^( videoclip(T,A,V,D,ApP,ApN) , ( (ApP > ApN , ClasaVideo == apreciat) ; (ApP < ApN , ClasaVideo == neapreciat) ; (ApP == ApN , ClasaVideo == neutru) ) ) , ListaVideoclipuri ).

/*

%De ce nu functioneaza aceasta varianta? Functioneaza doar pentru 'apreciat'. Daca dau ';' imi spune 'no'.

clasa_video(ClasaVideo,ListaVideoclipuri) :-  isMember(ClasaVideo,[apreciat,neapreciat,neutru]),
                                                                      ( (ClasaVideo == apreciat) , ( setof( T , A^V^D^ApP^ApN^( videoclip(T,A,V,D,ApP,ApN) , ApP > ApN ) , ListaVideoclipuri ) ) );
                                                                      ( (ClasaVideo == neapreciat) , ( setof( T , A^V^D^ApP^ApN^( videoclip(T,A,V,D,ApP,ApN) , ApP < ApN ) , ListaVideoclipuri ) ) );
                                                                      ( (ClasaVideo == neutru) , ( setof( T , A^V^D^ApP^ApN^( videoclip(T,A,V,D,ApP,ApN) , ApP =:= ApN ) , ListaVideoclipuri ) ) ).                                                                      

*/

/* Point D */

sum([], 0).
sum([H|T], Sum) :- sum(T, Rest) , Sum is H + Rest.

autor_apreciat(Autor,Calificativ) :- isMember(Calificativ,[apreciat,neapreciat,neutru]),
                                                      lista_utilizatori(L) , 
                                                      isMember(Autor,L),
                                                      setof( ApP , Autor^T^V^D^ApN^videoclip(T,Autor,V,D,ApP,ApN) , ListaApP ),
                                                      setof( ApN , Autor^T^V^D^ApP^videoclip(T,Autor,V,D,ApP,ApN) , ListaApN ),
                                                      sum(ListaApP , SApP),
                                                      sum(ListaApN, SApN),
                                                      ((SApP - SApN) > 0)->(Calificativ == apreciat);(Calificativ == neapreciat).
                                                                    
/* Point E */

getVideoByViews(_) :- setof([V,A],T^V^D^ApP^ApN^videoclip(T,A,V,D,ApP,ApN),L) , write(L).

/* Point F */

videosThatHaveAtLeastXViews(X,ListOfVideos) :- setof(T , A^V^D^ApP^ApN^(videoclip(T,A,V,D,ApP,ApN),V >= X) , ListOfVideos).
videosThatAreAppreciated(ListOfVideos) :-setof( T , A^V^D^ApP^ApN^(videoclip(T,A,V,D,ApP,ApN), ApP > ApN ) , ListOfVideos ).

intersection([], _, []).
intersection([Head|L1tail], L2, L3) :-
        memberchk(Head, L2),
        !,
        L3 = [Head|L3tail],
        intersection(L1tail, L2, L3tail).
intersection([_|L1tail], L2, L3) :-
        intersection(L1tail, L2, L3).
        
getViewedAndPositiveVideos(L) :- videosThatHaveAtLeastXViews(50000,L1) ,  videosThatAreAppreciated(L2), intersection(L1,L2,L).

/* Point G */

listLength([], 0).
listLength([H|T], Ll) :- listLength(T, Ll1) , Ll is 1 + Ll1.

averageDuration(Ad) :- setof(D , T^A^V^ApP^ApN^videoclip(T,A,V,D,ApP,ApN) , ListOfDurations) , sum(ListOfDurations,S) , listLength(ListOfDurations,LodL) , Ad is S/LodL.

/* Point H */

getLast(X,[LastElement]) :- X = LastElement.
getLast(X,[H|T]) :- getLast(X,T).

getImplicationScore(T,Score,L) :- videoclip(T,_,V,_,ApP,ApN) , Score is  (V - (ApP + ApN)) , setof([Score,T] , A^D^videoclip(T,A,V,D,ApP,ApN) , L ).

video_utiliz_implicati(StructuraVideoclip) :- getImplicationScore(Title,Score,ListOfScoresAndTitles), getLast(BestTitleScoreList,ListOfScoresAndTitles), getLast(BestTitle,BestTitleScoreList), StructuraVideoclip = videoclip(BestTitle,_,_,_,_,_).

/* Point I */

getListOfVideosByUser(User,L) :- setof(T, V^D^ApP^ApN^videoclip(T,User,V,D,ApP,ApN),L).
getVideosOfUser(X) :- read(User), getListOfVideosByUser(User,L), write(L).

/* Point J */

usersThatHaveAtLeastXMinutes(X,ListOfVideos) :- setof(A , T^V^D^ApP^ApN^(videoclip(T,A,V,D,ApP,ApN),D >= X) , ListOfVideos).

getUsersWithLongVideos(InputList,OutputList) :- usersThatHaveAtLeastXMinutes(4,LongUsers) , intersection(LongUsers,InputList,OutputList).
         
/* Point K */

lista_liste_video(ListaPerechi) :- setof([A,T],V^D^ApP^ApN^videoclip(T,A,V,D,ApP,ApN),ListaPerechi).

/* Queries */

/*
lista_utilizatori(L).
L = [catworshiper12_a,crazyteen07,dep_fizica,fmi_hollywood,gradinita10,lili_andra,trolololo] 

clasa_video(CV,L).
L = ['amv - supereroi','ceata lui pitigoi','pisici dragalase','pisici zglobii','povestea unui pui de pisica','salvati pisicile','teoria relativitatii','trailer - batman invata inteligenta artificiala','unde a fugit ariciul'],
CV = apreciat ? ;
L = ['ghost captured on camera','justin bieber - alta melodie','justin bieber - o melodie'],
CV = neapreciat ? ;
L = ['clipuri anime'],
CV = neutru ? y
yes

autor_apreciat(A,C).
A = catworshiper12_a,
C = apreciat ?

getVideoByViews(X).
[[1202,lili_andra],[2040,fmi_hollywood],[2304,dep_fizica],[14033,lili_andra],[40102,gradinita10],[123008,catworshiper12_a],[150101,gradinita10],[171234,trolololo],[190017,catworshiper12_a],[200008,catworshiper12_a],[204005,catworshiper12_a],[1302718,crazyteen07],[2401277,crazyteen07]]
true ?

getViewedAndPositiveVideos(L).
L = ['ceata lui pitigoi','pisici dragalase','pisici zglobii','povestea unui pui de pisica','salvati pisicile']

averageDuration(AD).
AD = 4.299166666666667 ?

video_utiliz_implicati(Struct).
Struct = videoclip('pisici zglobii',_A,_B,_C,_D,_E) ?

getVideosOfUser(X).                                                       |:  catworshiper12_a
     .
[pisici dragalase,pisici zglobii,povestea unui pui de pisica,salvati pisicile]
true ? yes

getUsersWithLongVideos([crazyteen07, dep_fizica, little_flower, mihai22, fmi_hollywood] , L).
L = [dep_fizica,fmi_hollywood] ? y
yes

lista_liste_video(ListaPerechi). 
ListaPerechi = [[catworshiper12_a,'pisici dragalase'],[catworshiper12_a,'pisici zglobii'],[catworshiper12_a,'povestea unui pui de pisica'],[catworshiper12_a,'salvati pisicile'],[crazyteen07,'justin bieber - alta melodie'],[crazyteen07,'justin bieber - o melodie'],[dep_fizica,'teoria relativitatii'],[fmi_hollywood,'trailer - batman invata inteligenta artificiala'],[gradinita10,'ceata lui pitigoi'],[gradinita10|...]|...] ?
*/