/*
,,,

NAME: seen/0
NAME : tolt/0
    Closes the current output stream and resets it to default.

Ex: Small examples of writing to a file.
*/

go :- tell('file.txt'), write('Hello world.'), nl, nl, nl, put(97), told.

/*
Ex: Write a prolog program that takes two filenames as arguments, will read four prolog terms from the input file in the first argument, then write those terms to the output file in the second argument.
*/

goagain(Infile, Outfile) :- see(Infile), tell(Outfile), read(X), write(X), nl, read(Y), write(Y), nl, read(Z), write(Z), read(W), write(W), seen, told.

/*
If we do not know the contents of a file in advance, then we must know how our built-in predicates respond to reaching the end of the file:
    read(X): X will unify with the atom end_of_file
    get(X) and get0(X): X will unify with -1

Ex: Wrie a prolog program that will read all the integer terms contained in a file, will sum them, and then will print the sum to the terminal.
*/

% Launcher will open the streams, read the first term, call the hepler function and initialize the sum, write the final answer, close the streams.
launch(Filename) :- see(Filename), tell(user), read(X), helper(X, 0, R), write(R), nl, seen, told.

% Helper recursive case
helper(X, N, R) :- X \= end_of_file, R1 is N+X, read(Y), helper(Y, R1, R).

% Helper base case
helper(end_of_file, N, N).