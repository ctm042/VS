/*
Lecture 2-4: Prolog Data Structures/Lists

There are two main methods to construct lists in prolog
    * Put prolog terms within brackets separated by comas
        [jason, jace, 42, likes(cam, cs)]
            ?- X = [jason, jace, 42, likes(cam, cs)].
                X = [jason, jace, 42, likes(cam, cs)].
    * Use the cons operator for a term and a list of terms  
        [H|T]
            ?- [H|T] = [jason, jace, 42, likes(cam, cs)].
                H = jason,
                T = [jace, 42, likes(cam, cs)].
            ?- [H|T] = [jason].
                H = jason,
                T = [].
        NOTE: Like in ML, the end of every list has an empty list.

BUILT-IN PREDICATES FOR LISTS

length/2
    First argument is a list, and the second argument is unified with its length
        ?- length([[jason, 42, likes(cam, cs)]], N).
            N = 3.

reverse/2
    First argument is a list, and the second argument is unified with the reversal of the list.
        ?- reverse([2, 3, 5, 7], R).
            R = [7, 5, 3, 2].

append/3
    First two arguments are lists, and the third argument is unified with their concatenation
        ?- append([2, 3, 5, 7], [8], R).
            R = [2, 3, 5, 7, 8]        

last/2 
    First argument is a list, and the second argument is unified with its last element

select/3
    First argument is an element of a list, second argument is a list, and the third argument is unified with the list after the leement has been removed one at a time (with backtracking).
        ?- select(5, [2, 3, 5, 7], R).
            R = [2, 3, 7] ;
            false.
        ?- select(5, [2, 3, 5, 7, 5], R).
            R = [2, 3, 7, 5] ;
            R = [2, 3, 5, 7].

member/2
    First argument is an element of a list and second argument is a list. Succeeds when the leement is in the list.

maplist/3
    The first argument represents a function, the second argument is a list, and the third argument is unified with the list after the function has been applied to each element.
        
    Review: In ML, the map function looked like
        map f [2,3,5,7]

        f(X, Y) :- Y is X*X.
        ?- maplist(f, [2, 3, 5, 7], R).
            R = [4, 9, 25, 47].
        
    Review: In ML, the reduce function foldl and foldr looked like
        foldl g 0 [2, 3, 5, 7]
    where g was a two-variable function.

foldl/4
    The first argument represents the accumuliation function, the second argument is a list, the third argument is the initial value, and the fourth argument is unified with the result.
        g(CV, ACC, R) :- R is CV+ACC.
        ?- foldl(g, [2, 3, 5, 7], 0, R).
            R = 17.

Lecture 2-5: Prolog Recursion

Review: The recursive factorial function in ML can be written as
    fun fact 0 = 1
        | fact n = n*fact(n-1);

Ex: Write a recursive prolog predicate named fact/2, where the first argument is a non-negative integer and the second argument is unified with its factorial value. For example,
    ?- fact(0, A).
        A = 1.
    ?- fact(4, A).
        A = 24.
*/

% Recursive case
fact(N, R) :- N>0, N1 is N-1, fact(N1, R1), R is N*R1.

% Base case
fact(0, 1).

/*
NOTE: We customarily place the recursive case before the base to help prevent unnecessary backtracking.
*/