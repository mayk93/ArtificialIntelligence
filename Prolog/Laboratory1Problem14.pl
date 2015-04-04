/*
Author: Mandrescu Mihai Petru
Group: 242
Date: 08.05.2014
*/

luna(decembrie,31).
luna(ianuarie,31).
luna(februarie,28).
luna(februarie,29).

luna(martie,31).
luna(aprilie,30).
luna(mai,31).

luna(iunie,30).
luna(iulie,31).
luna(august,31).

luna(septembrie,30).
luna(octombrie,31).
luna(noiembrie,31).

nr_zile1(Lun,NrZ) :- luna(Lun,NrZ).

/*
nr_zile1(februarie,X).
X = 28 ? y
yes
*/