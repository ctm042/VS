/*
Comments in prolog files are with slash star

Lecture: Intro to Prolog

Start swipl interpreter : swipl
Stop swipl interpreter : halt.

Programming in prolog consists of:
    - Declare facts
    - Define rules
    - Ask questons

We will write a small AI program so that we can ask it who are Ben Solo's grandparents.
*/

/* Step 1: Declare facts */
parent(anakin, luke).
parent(anakin, leia).
parent(padme, luke).
parent(padme, leia).
parent(leia, ben).
parent(han, ben).

/* Step 2: Define rules */
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

/* Step 3: Ask questions.... done in the inteprpreter */