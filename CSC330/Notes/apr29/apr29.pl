/*
Contiune Lecture 2-5

Ex: Write mutually recursive predicates named isEven/1 and isOdd/1 where the argument is a non-negative integer and will succeed when the input is even/odd apprpriately. For example,
    ?- isEven(4).
        true.
    ?- isOdd(4).
        false.
*/

% Recursive cases
isEven(N) :- N>0, N1 is N-1, isOdd(N1).
isOdd(N) :- N>0, N1 is N-1, isEven(N1).

% Base case
isEven(0). % Base case for isOdd is no code!

/*
Ex: Write our own length predicate named mylength/2.
*/

% Recursive case
mylength([_|T], R) :- mylength(T, R1), R is R1 + 1.

% Base case
mylength([], 0).

/*
Ex: Write recursive prolog predicate named listsum/2 where the first argument is a list of numbers and the second argument is matched with their sum. For example,
    ?- listsum([2, 3, 5, 7], R).
        R = 17.
*/

% Recursive case
listsum([H|T], R) :- listsum(T, R1), R is H + R1.

% Base case
listsum([], 0).

/*
Ex: Write a recursive prolog predicate named sortedMerger/3 where the first two arguments are sorted lists of numbers, and the third argument is matched with their combined sorted list. 
The ML version was
    fun sortedMerge(A, []) = A
        | sortedMerge([], B) = B
        | sortedMerge(A as x::xs, B as y::ys) =
            if x<y then x::sortedMerge(xs, B) else y:: sortedMerge(A, ys)
*/

% Recursive case
sortedMerge([H1|T1], [H2|T2], R) :- H1 < H2, sortedMerge(T1, [H2|T2], R1), R = [H1|R1].
sortedMerge([H1|T1], [H2|T2], R) :- H1 >= H2, sortedMerge([H1|T1], T2, R1), R = [H2|R1].
    % Can simplify like
sortedMerge([H1|T1], [H2|T2], [H1|R1]) :- H1 < H2, sortedMerge(T1, [H2|T2], R1).
sortedMerge([H1|T1], [H2|T2], [H2|R1]) :- H1 >= H2, sortedMerge([H1|T1], T2, R1).

% Base case
sortedMerge(A, [], A).
sortedMerge([], B, B).

/*
Ex: Write your own member predicate named mymember/2, where the first argument is an element and the second argument is a list. It succeeds when the element is a member of the list. For example
    ?- mymember(5, [2, 3, 5, 7]).
        false.
    ?- mymember(9, [2, 3, 5, 7])
*/

% Recursive case
mymember(X, [H|T]) :- H \= X, mymember(X, T).

% Base case
mymember(X, [X|_]).

/*
Ex: (in-class) Write your own append predicate named myappend/3, where the first two arguments are lists, and the third argument is matched with their concatenation. For example,
    ?- myappend([a, b], [c, d, e], R).
        R = [a, b, c, d, e].
*/

% Recursive case
myappend([H1|T1], B, R) :- myappend(T1, B, [R|H1]).
myappend([], [H2|T2], R) :- myappend([], T2, [R|H2]).

% Base case
myappend([], [], R). % no worky :(

/*
Ex: (in-class) Write your own reverse predicate named myrev/2, where the first argument is a list, and the second argument is matched with its reversal. You may use append or myappend. For example,
    ?- myrev([a, b, c, d], R).
        R = [d, c, b, a].
*/

% 2.1, 2.2, 2.3, 2.4, 2.5