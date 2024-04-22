/*
Contiune Section 2-2

Next, we can write some simple database predicates (functions) just by exploiting prolog's unification process.

Ex. (BOSS) Suppose that prolog has read a database (file) with the class and faculty info at LA Tech. The following is a sample of the entries in the database.
*/
course(
    csc330,
    days(mwf),
    time(930, 1045),
    instructor(terry, jason),
    room(iesb205),
    section(001),
    quarter(spring2024)
).

course(
    csc310,
    days(tr),
    time(1000, 1150),
    instructor(oneal, mike),
    room(iesb216),
    section(001),
    quarter(spring2024)
).

course(
    math308,
    days(tr),
    time(1600, 1750),
    instructor(terry,jason),
    room(iesb210),
    section(051),
    quarter(spring2024)
).

course(
    phys202,
    days(tr),
    time(800, 950),
    instructor(quigley, seth),
    room(iesb308),
    section(002),
    quarter(spring2024)
).

/*
Write prolog rules for the following tasks

1. getRoomByClass/2, where the first argument is a class and the second argument is matched with the room the class is located in. For example,
    ?- getRoomByClass(csc330, A).
    A = iesb205
*/

getRoomByClass(C, R) :- course(
    C, 
    _, 
    _, 
    _, 
    room(R), 
    _, 
    _
).

/*
Lecture 2-3: Prolog Operators and Arithmetic

NEW BUILT-IN PREDICATE

NAME: op/3
SYNTAX: op(<Precedence>, <Type>, <Name>)
    Used to define custom operators. In the PL file, begin with ?-

    Precedence: Integer value that defines the priority of the operator. The lower the number, the higher the priority.
    Type: An atom that describes the operator. Some choices are:
        yfx: infix, left associative
        fy: unary prefix, associative
        fy; unary, postfix, associative
    Name: An atom for the name of the operator you're defining.

NOTE: Operators can still be used the original way with the functor before the parentheses and arguments.
*/
?- op(150, yfx, likes).
likes(jace, cs). 
/* 
    ?- jace likes cs. 
    true 
*/
/*
Now that you've seen how to define your own operators, we can officially learn about built-in operators.

BUILT-IN OPERATORS FOR TERMS

NAME: = /2
TYPE: infix
SYNTAX: <TERM1> = <TERM2>
    Unifies the given terms.
        ?- X = jason.
        X = jason
        ?- =(X, jason)
        X = jason

NAME: == /2
TYPE: infix
SYNTAX: <TERM1> == <TERM2>
    Succeeds when the terms are literally equal.
        ?- X == jason.
        false
        ?- jason == jason.
        true

NAME: \= /2
TYPE infix
SYNTAX: <TERM1> \= <TERM2>
    Succeeds when the terms do not unify.
        ?- jason \= jace.
        true
        ?- jason \= jason.
        false

BUILT-IN OPERATORS FOR NUMBERS

Let's first list the comparison operators

    <   less than
    >   greater than
    =<  equal to or less than
    >=  greater than or equal to
    =:= is arithmetically equal to
    =\= is not arithmetically equal to

NOTE: These operators are predicates!

Next lets list the common math operators
    +       plus
    -       minus
    *       multiply
    /       divide
    //      integer division
    ^       exponentiation
    **      exponentiation
    abs/1   absolute value
    max/2   max of two numbers
    min/2   min of two numbers
    sqrt/1  square root of a number
    cos/1   cosine
    sin/1   sine
    pi      value of pi
    rem/2   remainder
    
NOTE: These are NOT predicates!!!!!!!!!!!!!!!!!!!!!!!!!!!

*/