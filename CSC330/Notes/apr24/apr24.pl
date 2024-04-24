/*
Continue Section 2-3

When you want to do arithmetic/math in prolog, you need a special predicate to execute it (so that it knows you're not talking about atoms!)

NAME: is
TYPE: infix
SYNTAX: <TERM> is <ArithmeticExpression>
    The arithmetic expression is evaluated and then unified with <TERM>
        ?- X is 3+4.
        X = 7.
        ?- 7 is 3+4.
        true.

BUILT-IN OPERATORS FOR LOGIC
    ,   and
        ?- true, true
        true.
        ?- true, false
        false.

    ;   or
        NOTE: When writing prolog rules, we don't usually use ; because we can just write an additional rule on another line.
            Ex: If the following rules are already defined
                mother(X, Y).
                father(X, Y).
            And we want to write an isParent/2 predicate, one option is:
                isParent(X, Y) :- mother(X, Y); father(X, Y) % DONT DO THIS!
            Option 2 is:
                isParent(X, Y) :- mother(X, Y).
                isParent(X, Y) :- father(X, Y). % This is preferred/less complicated to interpret
    not not
        not(true).
        false.

Let's now use all these operators we've just learned to write more complicated prolog tasks.

Ex: Suppose that prolog has read the following database
*/
inOffice(biden, 2021, 2024).
inOffice(trump, 20217, 2020).
inOffice(obama, 2009, 2016).
inOffice(bush43, 2001, 2008).
inOffice(clinton, 1993, 2000).
inOffice(bush41, 1989, 1992).
capital(texas, austin).
prez(X, Y) :- inOffice(X, A, B), Y>=A, Y=<B.
/*
Predict the output of the following prolog goals.
    ?- inOffice(obama).
        ERROR: 
        false.
    ?- inOffic(obama, 2016, 2020).
        false.
    ?- inOffice(obama, M, N).
        M = 2009, 
        N = 2016.
    ?- prez(obama, 2010).
        true.
    ?- prez(P, 2010).
        P = obama ;
        false.
    ?- prez(obama, N).

PREDICATES WITH "OUTPUT"
In prolog when you want to write a "function" with "output", it is custom to write a predicate with an additional argument that is unified with the output you seek.

Ex: Write a prolog predicate named myFun/2, where the first argument is a number X and the second argument is 3X+1. For example,
    ?- myfun(7, R).
    R = 22.
Review: In ML, the code is
    fun myfun x = 3*x+1
*/
myfun(X, R) :- R is X*3+1.

/*
Ex: Write a predicate named isEven/1 that succeeds when its argument is an even integer.
For example,
    ?- isEven(4).
    true.
*/
isEven(N) :- 0 is rem(N,2).

/*
For error checking on integers, there is a built-in predicate named ineger/1 that succeeds when its argument is an integer term.
*/
isEven2(N) :- integer(N), 0 is rem(N,2).

/*
BUILT-IN PREDICATES FOR ATOMS

NAME: char_code/2
SYNTAX: char_code(C, N)
    C is a single character atom, N is an integer. This succeeds when C corresponds to the integer value N.

        ?- char_code(a, 97).
            true.
        ?- char_code(C, 97).
            C = a.
        ?- char_code(a, X).
            x = 97.

Ex: (in-class) Write a predicate named toUpper/2, where the first argument is a character (atom of length 1) and the second argument is matched with its uppercase version. For example,
    ?- toUpper(d, R).
        R = 'D'.
Review: In ML, the code to do this example was
fun toUpper c = chr(ord(c) - 32);
*/
toUpper(L, U) :- char_code(L, X), Y is X -32, char_code(U, Y).

/*
Ex. (in-class) Write a predicate named distance/3, where the first two arguments are coordinates, and the third argument is matched with the distance between them. For example,
    ?- distance((2, -2), (4, 2), R).
    R = 5.0
*/
distance((A, B), (X, Y), D) :- D is sqrt((A-X)^2 + (B-Y)^2).

/*
Here's another builtsin predicate for atoms

NAME: atomic-concat/3
SYNTAX: atomic_concat(<Atom1>, <Atom2>, R)
    Concatenate the atoms together and unify the result to R

Ex. Write a predicate named past/2, where the first argument is an atom, and the second argument is unified with the atom with 'ed' concatenated on the end. For example,
    ?- past(lock, R).
    R = locked.
*/
past(W, R) :- atomic_concat(W, ed, R).