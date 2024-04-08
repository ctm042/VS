(*
Lecture 1-6: ML Input and Output

We will learn how to read and write to files so that ML can communicate with the outside world. 
Warning: Sometimes using VSCode with ML can cause unintended results.
First, there is a built'in ML function to load files into the interpreter via terminal. The function is
    use : string -> unit

    (SML to start SML and ^Z to exit)

There is a built-in function to print strings to the terminal.
    print : string -> unit
*)
print "hello world";

(*
Ex. Write an ML function with name and type
    pchar : char -> unit
that inpus a character, prints the character to the terminal, then returns unit.

*)
fun pchar c = print(str(c)^"\n");

(*
STRUCTURES
An ML structure is a built-in "library" that contains predefined functions that we can import into the ML stack
    - Int.toString;
    - Int.toString(42);

The syntax to load all of a structure's function onto the stack is 
    open <structure name>

NEW CONSTRUCT
    <exp1>; <expr2>; <...>; <expn>
Evaluates several expressions consecutively. Afterward, the final result evaluates to the last expression.

Ex. Write a recursive ML function with pattern matching with name and type
    pbools : bool list -> unit
that will input a list of bools, print them to the terminal, then return unit. For example
    - pbools [true, true, false];
    true
    true
    false
    val it = () : unit
*)
fun pbools [] = ()
    | pbools (x::xs) = (
        print(Bool.toString(x)^"\n");
        pbools(xs) (*no semicolon since this is the last one to be evaluated*)
    );
(*
Note: This construct can be used for debugging! 
You can add as many print statements as you want to display intermediate variable values. 
Just remember that the last expression must be the right type

FILE READING

NEW STRUCTURE: TextIO
NEW TYPE: instream

NEW LIBRARY FUNCTIONS
    TextIO.openIn : string -> instream
        Takes a file name as a string and then returns a reference to access the file.
    
    TextIO.closeIn : instream -> unit
        Closes a file that was used for reading and returns unit

    TextIO.endIoStream : instream -> bool
        Checks whether you've reached the end of the file

    TextIO.input : instream -> string (* aka vector *)
        Reads/consumes the entire file and returns as a string.

    TextIo.inputN : instream * int -> string (* vector *)
        Inputs a file and non-negative integer and then reads that number of characters from the file and returns them as a string.
*)

