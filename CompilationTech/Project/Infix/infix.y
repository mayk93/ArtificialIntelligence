/* 
    Proiect Tehnici de Compilare
    Calculator cu notatie poloneza inversa
    Mandrescu Mihai Petru - 342
*/

/* Aceasta este prologul. */
/*
    YYSTYPE este o directiva de preprocesor care spune utilizatului Bison
    ca tipul de date "default" este double. Daca nu am fi folosit aceasta
    directiva de preprocesor, tipul de date default ar fi fost int, si operatii
    precum "12.2 3.4 +" ar fi rezultat intr-o eroare.
    
    Tot in prolog avem trecute si librariile pe care le foloseste programul
    generat.
*/
%{
#define YYSTYPE double
#include <math.h>
#include <ctype.h>
#include <stdio.h>
%}

/* Aceasta este sectiunea pentru declaratii Bison. */
/*
    Aici am declarat terminalul NUM. Daca acest terminal ar fi reprezentat de
    un singur caracter, nu ar fi trebuit sa il declaram.
*/
%token NUM
%left '-' '+'
%left '*' '/'
%left NEG     /* negation--unary minus */
%right '^'    /* exponentiation        *

/* Aceasta este rectiunea pentru reguli gramaticale */
/*
    In aceasta sectiune, am definit input, ce introducem in programul generat,
    ca fiind: 
    Fie o intrare goala ( empty string )
    Fie un input urmat de o linie.
    
    La randul sau, linia ( o linie de text care poate sau nu sa fie acceptata
    de program ) poate fi:
    Fie '\n' ( o linie goala ), fie o expresie urmata de enter.
    In cazul doi, se afiseaza "--->" urmat de valoare expresiei ( $1 ), cu
    o precizie de 10 zecimale (%/10g).
    
    In final, productiile pentru o expresie spun asa:
    1. O expresie poate fi un NUM ( terminal, un numar, valoarea ei ). In acest
       caz, valoarea expresiei este chiar valoare lui NUM.
    2. O expresie poate fi alcatuita din alte doua expresii, urmate de un +.
       In acest caz, valoarea expresiei va fi adunarea valorii celor doua
       expresii care o formeaza.
       Analog pentru -,*,/ si ^.
    3. O expresie fi o expresie urmata de un "n". In acest caz, valoare
       expresiei este negativul valorii expresiei din dreapta.        
*/
%%
input:    /* nimic */
        | input line
;

line:     '\n'
        | exp '\n'  { printf ("--->%.10g\n", $1); }
;

exp:      NUM             { $$ = $1;         }
        | exp exp '+'     { $$ = $1 + $2;    }
        | exp exp '-'     { $$ = $1 - $2;    }
        | exp exp '*'     { $$ = $1 * $2;    }
        | exp exp '/'     { $$ = $1 / $2;    }
      /* Exponentiation */
        | exp exp '^'     { $$ = pow ($1, $2); }
      /* Unary minus    */
        | exp 'n'         { $$ = -$1;        }
;
%%

/* Acesta este epilogul */
/* 
    Analizorul lexical, yylex, sare spatiile si taburile si
    intoarce un double pentru NUM.
*/
yylex ()
{
  int c;

  /* Sar spatiile goale  */
  while ((c = getchar ()) == ' ' || c == '\t')  
    ;
  /* Procesez numerele */
  if (c == '.' || isdigit (c))                
    {
      ungetc (c, stdin);
      scanf ("%lf", &yylval);
      return NUM; /* Intorc un numar */
    }
  /* Am ajuns la sfarsit */
  if (c == EOF)                            
    return 0;
  /* Intorc caracterul citit */
  return c;                                
}

/* Functie de gestionare a erorilor, este chemata de yyparse. */
yyerror (s)
     char *s;
{
  printf ("%s\n", s);
}

/* De aici se cheama parserul */
main ()
{
  yyparse ();
}
