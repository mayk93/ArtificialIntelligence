/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

a=X.
X = a ? y
yes
| ?- X=3.
X = 3 ? y
yes
| ?- X=X.
true ? y
yes
| ?- 3=2.
no

/*
'is' forteaza calculul expresiilor aritmetice.
*/