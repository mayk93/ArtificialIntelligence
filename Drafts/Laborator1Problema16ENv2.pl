/*
Author: Mandrescu Mihai Petru, 242
Date: 23.03.2014
*/

/*
This programme will calculate a predicate which, given 3 input parameters,
will produce 3 outputs.

The three input parameters are as follows:
        1. Grade
        2. Profile
        3. Health
        
The three output parameters will be:
        1. Course
        2. Location
        3. Equipment
        
Students are defined by the three input parameters.
The programme will decide what course they will attend, at what location
and what equipment will they be given. 
*/

/*
Auxiliary predicate that will serve as an example generator:
example(+Type)
*/
example('PMH')  :- write('Primary, Mathematical, Healthy').
example('SPPU') :- write('Secondary, Philological, Partially Unhealthy').
example('HASU') :- write('High School, Artistic, Severely Unhealthy').


/*Corner Cases:*/
example('Corner') :- write('College, Social-Sciences, aarf').

/*
This serves as an example for a unsupported input.
This programme deals only with K12 grades and only mathematical, philological
and arts profiles. Also, random inputs such as "aarf" are invalid.
*/

/*------Solution Predicate-----------*/

getCycle(G,Cy) :- (G >= 1 , G =< 4) -> Cy is 0 ; (G >= 5 , G =< 8) -> Cy = 1 ; (G >= 9 , G =< 12) -> Cy = 2 ; write('Invalid'),fail.

getCourse(Cy,P,C) :- (Cy =:= 0 , P = 'mathematic') -> C = 'mathematics' ; ((Cy =:= 1;Cy =:= 2) , P = 'mathematic') -> (C = 'mathematics' ; C = 'physics' ; C = 'computer science') ; (Cy =:= 0 , P = 'philological') -> C = '' ; (Cy =:= 1 , P = 'philological') -> C = 'literature' ; (Cy =:= 2 , P = 'philological') -> C = 'composition' ; ((Cy =:= 0 ; Cy =:= 1) , P = 'artistic') -> C = 'drawing' ; (Cy =:= 2 , P = 'artistic') -> C = 'painting' ; write('Invalid'),fail.

getLocation(Cy,C,H,L) :- ((Cy =:= 0;Cy =:= 1; Cy =:= 2),(C = 'mathematics';C = 'literature';C = 'painting'),(H = 'healthy';H = 'partially unhealthy c'; H = 'partially unhealthy uc')) -> L = 'Micul Aplinist' ; ((Cy =:= 0; Cy =:= 1),(C = 'drawing';C = 'mathematics';C = 'computer science';C = 'physics'),(H = 'healthy';H = 'partially unhealthy c'; H = 'partially unhealthy uc' ; H = 'severely unhealthy c' ; H = 'severely unhealthy uc')) -> L = 'Internat Central' ; ((Cy =:= 2),(C = 'physics'),(H = 'healthy';H = 'partially unhealthy c'; H = 'partially unhealthy uc' ; H = 'severely unhealthy uc')) -> L = 'Physics Institute' ; ((H = 'severely unhealthy c' ; H = 'severely unhealthy uc'),(C = 'mathematics' ; C = 'drawing' ; C = 'painting' ; C = 'composition' ; C = 'literature')) -> L = 'Hospital' ; (C = 'composition') -> L = 'Cenaclul Scriitorasul' ; write('Invalid'),fail.

getEquipment(H,P,E) :- (H = 'severely unhealthy c' ; H = 'severely unhealthy uc') -> E = 'laptop' ; (P = 'mathematic') -> E = 'laptop' ; (P = 'philological') -> E = 'ebook reader' ; (P = 'artistic') -> E = 'drawing kit' ; write('Invalid'),fail.

/*
Main Predicate:
decide(+G,+P,+H,-C,-L,-E)
The letters are abbreviations for:
G - Grade
P - Profile
H - Health
C - Course
L - Location
E - Equipment
*/
decide(G,P,H,C,L,E) :- getCycle(G,Cy) , getCourse(Cy,P,C) , getLocation(Cy,C,H,L) , getEquipment(H,P,E).

/*---------------------------------*/


/*
The predicate is solved by calculating four additional predicates:

        1. getCycle determines the school cycle ( primary = 0, secondary = 1, high school = 2 ) of the student, based on the grade he is in.
        2. getCourse calcuates, once the cycle is found, what courses are available for the student. It takes into account not only the cycle, but also
           his profile.
        3. getLocation is the predicate that uses the previously determined cycle and available courses, along with the student's health, to determine
           the camp locations he is fit to visit. It is not a very elegant predicate, being a long chain of if-then-else statements, but it functions.
        4. getEquipament uses the health and profile inputs to decide what special equipment the student needs.
        
"fail" was added at the end of each predicate to prevent incomplete calculations when asking for more solutions ( via ";"). For example,
if one were to remove fail and interrogate "decide(12,'mathematic','severely unhealthy c',C,L,E)." he would be given one complete result, "Hospital"
and several incomplete answers, in the sense the course would change but there would be no location available.
  
*/

/*
Interrogation examples:
*/

/*
?- decide(12,'mathematic','severely unhealthy c',C,L,E).
C = mathematics,
L = 'Hospital',
E = laptop .
-----
?- decide(8,'mathematic','healthy',C,L,E).
C = mathematics,
L = 'Micul Aplinist',
E = laptop ;

C = physics,
L = 'Internat Central',
E = laptop ;

C = 'computer science',
L = 'Internat Central',
E = laptop.
-----
?- decide(1,'artistic','partially unhealthy uc',C,L,E).
C = drawing,
L = 'Internat Central',
E = 'drawing kit'.
-----
?- decide(10,'philological','partially unhealthy c',C,L,E).
C = composition,
L = 'Cenaclul Scriitorasul',
E = 'ebook reader'.
-----
decide(7,'philological','severely unhealthy c',C,L,E).
C = literature,
L = 'Hospital',
E = laptop.
*/


/*============================================================================*/
