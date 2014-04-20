pred(N1,Lr) :- read(X),
               (
               (X == gata,!,Lr=[],N1=0);
               (X==0,!,write("Eroare."),fail);
               (integer(X),!,Lr=[X|L],pred(N1,L));
               (atom(X),pred(N,Lr),N1 is N+1)
               ).
