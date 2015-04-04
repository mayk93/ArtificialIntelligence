%Nume Radu Vlad 242
%Data 02.05.2014

for(N2,N2,Scop):-Scop;\+Scop.						
for(N1,N2,Scop):-(Scop;\+Scop),N3 is N1+1,for(N3,N2,Scop).

/*Interogari
ÄŽ| ?- for(0,5,(write(45),nl)).
45
45
45
45
45
45
yes
*/