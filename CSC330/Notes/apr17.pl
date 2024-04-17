/*
Lecture 2-1: Prolog Unification

*Unification is the primary action this preformed by prolog when executed code.

*The prolog infix operator for unification is =

The following is a description of how unification process works
    - Two atoms unify if and only if they are (literally) the same.
        jason = jason. {true.}
        jason = jace. {false.}
    - Two numbers unify if and only if they are the same.
        42 = 42. {true.}
    - Two compound terms unify if and only if they have the same functor, the same arity (number of arguments), and their corresponding arguments unify (left-to-right).
        - likes(jason,cs) = likes(jason,cs). {true.}
        - likes(jason,cs) = likes(jason). {false.}
    - An unbounded variable (variables start with capital letter) and a term (terms start with a lowercase letter) that is not a variable always unify, and the variable is bounded (instantiated) to that term. The scope ends at the period. The variable is treated as the term it is bound to.
        - jason = X. {X = jason.}
        - likes(jason,cs) = Y. {Y = likes(jason,cs).}
        - likes(jason,cs) = likes(jason,X). {X = cs.}
        - likes(jason,cs) = likes(X). {false.} /* arity
        - likes(jason,cs) = likes(X,X). {false.}
        - likes(jason,cs) = likes(X,Y). {X = jason, Y = cs.}
    - Two variables always unify and are bounded to each other.
        - X = Y. {X = Y.}
    - Any other combination of terms fails to unify. 

The prolog operator of and is the comma
    - X = jason, Y = jace. {X = jason, Y = jace.}
    - X = jason, jason = winkelmann. {false.}

There are three possible results for unification:
    - If unification is successful and there are no variable instantiations, then the response from prolog is:
        true.
    - If unification is successful and there are variable instantiations, then then there is an implied true and the response is:
        <Var1> = <val1>, <Var2> = <val2>, <etc>.
    - If unification is not successful, then the response is:
        false.

Remember that statements we type into the prolog interpreter evaluate to true or false, aka, asking the interpreter if they succeed or fail.
    - class(csc330, time(930, 1045)) = class(csc330, X). {X = time(930, 1045).}



Lecture 2-2: Prolog Goals and Predicates
We will trace through our star wars example from the first day of prolog to loarn how it "executes" programs. Recall the style of programming in prolog
    1. Declare facts
    2. Define rules
    3. Ask question... which means that after we load a file into the prolog interpreter, we then type GOALS into the interpreter to see if the goals succeed, i.e. if the goals unify with the code in the file.
*/

parent(anakin, luke).
parent(anakin, leia).
parent(padme, luke).
parent(padme, leia).
parent(leia, ben).
parent(han, ben).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

/* lets look at different goals that we type into the interpreter and trace how prolog responds.

?- parent(anakin, luke).
    true ;
    false.

First it succefully unified with line 52 and responded true. The semicolon tells prolog to redo and try to unify again. There are no more matches in the rest of the code, and so the response is false. 

?- grandparent(A, ben).
    A = anakin ;
    A = padme ;
    false.

Unifies with line 58 (before the :-). The X is bound to A and Y is bound to ben. 
Prolog will now try to unify the goals after :- (pronounced as if) from left to right. If the right side succeeds, then the left side will succeed.
    The right side of the rule effectively has
        parent(A, Z), parent(Z, ben).
Line 52 is the next match: parent(anakin, luke), parent(luke, ben).
Now prolog tries to match praent(luke, ben), but fails
NOW BACKTRACKING: Prolog will now try to go back to the last successful goal and unify again for more possible matches.
Line 53 is the next match: parent(anakin, leia), parent(leia, ben)
Then prolog tries to match parent(leia, ben) and succeeds on line ?. NOW SUCCESS ON THE RIGHT SIDE OF:-!! Now prolog outputs any instantiated variables that we asked for in the original goal we tiped into the interpreter, which is
    A = anakin
*/