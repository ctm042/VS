Lecture 1-1: ML Expression and Operators

ML is a functional programming language, i.e., it evaluates given expression.

Every ML Expression must end with ;

val 
    means value

it 
    the variable in the ML environment that contains the last expression expression evaluated 

:

    the ml symbol that associates a value with a type

*ML is a strongly typed language

BASIC/PRIMITIVE TYPES OF ML

int 
    constructed by a sequence of intergers.

bool 
    only thw values: true, false.

string 
    constructed by surrounding a sequence of characters with double quotes 

char 
    constructed by #"<character>"

real 
    construction steps are:
        1) starts with optional ~
        2) A sequence of one or more digits 
        3) a) A decimal point and one or more digits 
        b) The letter E or e, an optional ~, and one or more digits 

unit 
    only one value: ()

INTERGER OPERATORS
+ - * div mod

REAL OPERATORS 
+ - * /

*UP arrow will reprint previous expressions

*Whitespace is ignored 

STRING OPERATOR
^

LOGICAL OPERATORS 
andalso orelse

COMPARISON OPERATORS 
= < > <= >= <>

NOTE: Cannot use <> = on reals!
