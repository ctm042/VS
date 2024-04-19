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
At the prompt, we type ; which forces a fail and backtrack.

Line 54 is the next match: parent(padme, luke),parent(luke, ben)
Then tries to unify parent(luke, ben). Failure, then backtrack.

Line 55 is the next match: parent(padme, leia), parent(leia, ben).
Then parent(leia, ben) succeeds. Output A = padme. At prompt we type ; which forces a fail and backtrack.

Line 56 is the next match: parent(leia, ben), parent(ben, ben).
Then parent(ben, ben) fails. Then backtrack.

Line 57 is the next match: parent(han, ben), parent(ben, ben).
Then parent(ben, ben) fails. Then backtrack.

There are no more matches. As far as prolog knows, the right side of the :- has failed, and so the final response is false.

Ex.Suppose that prolog has read the following file/database into the interpreter.
*/

boy(alex).
boy(brandon).
girl(claire).
girl(denise).
couple(P, Q) :- boy(P), girl(Q).

/*
Predict the response from the prolog interpreter to the following goals.

?- boy(aaron).
    false
    .
?- boy(alex).
    true.

?- girl(G).
    G = claire ;
    G = denise.

?- couple(alex, G).
    G = claire ;
    G = denise.

?- couple(B, G).
    B = alex,
    G = denis ;
    B = alex,
    G = claire ;
    B = aaron,
    G = denis ;
    B = aaaron,
    G = claire ;
        <All possible boy-girl matches>

PREDICATES (analog to functions in ML)
Predicates are expressions in prolog that evaluate to true or false, aka succeed or fail.
This type of evaluation is the basis for driving prolog programs. First, let's look at some built-in predicate, then proctice writing our own.

BUILT-IN PREDICATES

halt/0
    Exits the compiler/interpreter

consult/1
    loads a file /database into the interpreter

write/1
    The argument is a prolog term and the predicate will write the term to the current output stream. Always succeeds except on backtracking.
        write(jace).
            jace
            true.

        write('Hello World').
            Hello World
            true.

n1/0
    Writes a new line to the current outpun stream. Always succeeds except on backtracking.

Note: You can use the write/1 and n1/0 predicates to debug your prolog code by displaying intermediate variable binding during execution. You can also use them to pretty-up displays.

Ex. Rewrite the grandparent rule in our star wars example so that it will print the intermediate parent bindings between the grandparent and grandchild during execution.
COMMENT OUT THE ORIGINAL GRANDPARENT RULE.
 */
grandparent(X, Y) :- parent(X, Y), parent(Z, Y), write(Z), nl.

/*
Just for looks, let's add some bells and whistles so that it looks like we have an AI response.
*/
grandparent(X, Y) :- parent(X, Y), parent(Z, Y), write(Y), write(' is a child of '), write(Z), write(' who is a child of '), nl.

/*
Let's practice writing our own prolog rules to accomplish tasks, starting with the star wars example. When writing prolog rules, one approach to think about it is:
    <for this goal to succeed> :- <these goals must be satisfied>

Ex. Add predicate isParent/1 that succeeds when its argument is the parent of anyone in the database. For example,
    ?- isParent(ben).
    false.

    ?- isParent(padme).
    true.
*/
isParent(A) :- parent(A, B).

/*
Note: The wildcard symbol in prolog is the underscore. A variable that appears only once will cause a "singleton" warning because it's not being used.
*/
isParent(A) :- parent(A, _).

/*
Ex. Write a predicate named areSiblings/2 that succeeds when the arguments have at least one parent in common.
*/
areSiblings(A,B) :- parent(C,A), parent(C,B).

/*
Ex. (Abstract) Suppose that the following predicates are already defined properly.
    male(X)     % X is a male
    female(X)   % X is a female
    parent(X,Y) % X is a parent of Y
    diff(X,Y)    % X and Y are different people.

Use these predicates to write the following rules. Note that sex matters and one cannot be a mother, father, etc. of oneself.

1. mother(X, Y) that succeeds when X is the mother of Y
        mother(X, Y) :- female(X), parent(X,Y).

2. isMother/1 that succeeds when its argument is the mother of someone
        isMother(X) :- female(X), parent(X, _).
            OR
        isMother(X) :- mother(X, _).

3. sisters/2 that succeeds when the arguments are sisters with at least one parent in common
        sisters(X,Y) :- female(X), female(Y), parent(Z,X), parent(Z,Y), diff(X,Y).
*/