(* 
Lecture 1-4: ML Recursion (and Lists)

NOTE: In ML/functional language, loops are frowned upon!!

NOTE: There is a builtsin function to return the length of a list called length.

 *)
 length; (*val it = fn : 'a list -> int*)
 length([2,3,5,7]) (*val it = 4 : int*)

 (*
 Ex. Write our own length function named my length using recursion.
 *)
 fun mylength L = if L=[] then 0 else 1+mylength(tl(L)); (*val mylength = fn : ''a list -> int*)
 mylength(nil); (*val it = 0 : int*)
 mylength([2,3,5,7]) (*val it = 4 : int*)

 (*
 ''a means that you are using the comparison operators that is only for certain types. (Compiler asking "Are you sure you wanna do this?")
 
 This style is still not completely proper. A better way to define functions in ML is to use pattern matching. The syntax for pattern matching is
    fun <identifier> <pattern1> = <exp1>
        | <edentifier> <pattern2> = <exp2>
        <...>
        | <identifier> <pattern-n> = <exp-n>

and allowed <patterns> are constants/literals or expressions with ::

Ex. Let's repeat the previous example using pattern matching.
 *)
 fun mylength2 [] = 0
    | mylength2 (x::xs) = 1+mylength2(xs); (*val mylength2 = fn : 'a list -> list*)

mylength([2,3,5,7]) (*val mylength2 = 4 : int*)

(*
Note that x is not used, so you can replace it with _ (wildcard)
*)
fun mylength2 [] = 0
    | mylength2 (_::xs) = 1+mylength2(xs);

(*
NEW SYNTAX: The case reserved word sort of plays the role of "switch" and has syntax
    case <expression> of <match>
and then <match> will have syntax
    <pattern1> => <exp1> | <pattern2> => <exp2> | <...> | <pattern-n> => <exp-n>

This is just an alternate way to do pattern matching (if you have a lot of cases to code).
The previous example can be coded with case as follows
*)
fun mylength3 L = case L of [] => 0 | (_::xs) => 1 + mylength3(xs);
mylength3([2,3,5,7]);

(*
Ex. (in-class) Write a recursive function using pattern matching with name/type
    lsum : int list -> int
that inputs a list of integers and returns their sum. For example,
    - lsum([2,3,5,7]);
    val it = 17 : int
*)
fun lsum [] = 0
    | lsum (x::xs) = x+lsum(xs);
(*or*)
fun lsum2 L = case L of [] => 0 | (x::xs) => x + lsum2(xs);
lsum2([2,3,5,7]);

(*
Ex. (For pattern matching instead of lists) Write a recursive function using pattern matching with name/type
    fact : int -> int
that inputs a non-negative integer and returns its factorial value. For example
    - fact(4);
    val it = 24 : int
*)
fun fact 0 = 1 | fact m = m*fact(m-1)

(*
Ex. Write a recursive function using pattern matching with name/type
    lpairsum : (int * int) list -> int
that inputs a list of integer pairs and returns the sum of all integers. For example,
    - lpairsum([(2,3),(5,7)]);
    val it = 17 : int
*)
fun lpairsum [] = 0
    | lpairsum ((x,y)::xs) = x+y+lpairsum(xs);
(*or*)
fun lpairsum2 L = case L of [] -> 0 | ((x,y)::xs) => x+y+lpairsum2(xs)

(*
NEW SYNTAX: and
Allows you to do more than one declaration simultaneuosly.
*)
val a = 3 and b = 4 (*val a = 3 : int, val b = 4 : int*)
(*
Ex. Write mutually recursive functions with pattern matching named isOdd and isEven that input non-negative integers and returns the proper boolean value. For example.
    -isOdd(0);
    val it = false : bool
    -isEven(4);
    val it = true : bool
*)
fun isOdd 0 = false | isOdd n = isEven(n-1) 
    and 
    isEven 0 = true | isEven n = isOdd(n-1); (*val isOdd = fn : int -> bool, val isEven = fn : int -> bool*)
(*
This wouldn't work if isOdd and isEven were defined separately bc they reference each other.
*)
isOdd(2) (*val it = false : bool*)