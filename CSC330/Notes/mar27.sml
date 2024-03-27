(*
Countinue Lecture 1-4

MAP PUFNCION
The syntax for the map funciot is 
    map <function> <list>
that returns the list after the function has been applied to each element of the list
*)
map;
map (fn x => x*x) [2,3,5,7];

(*
Ex. (in-class) Use the map function to append "ed" at the end of every string on a list. 
For example, the input ["box","fix","lock"] should return ["boxed","fixed","locked"] 

REDUCE FUNCTIONS
The built in reduc functions in ML are called foldl and foldr. Their syntax is
    <foldl or foldr> <two-var function> <initial value> <list>
that takes the function and applies it continuously to every element of the list starting with the initial value.
*)
fold; (*val it = fn : ('a * 'b -> 'b ) -> 'a list -> 'b*)

fun myfun (cv, acc) = cv+acc;
myfun(3,4); (*val it = 7 : int*)

foldl myfun 0 [2,3,5,7]; (*val it = 17 : int*)
foldr myfun 0 [2,3,5,7]; (*val it = 17 : int*)

(*
Ex. Use one of the reduce functions to concatenate all strings in a list. For example,
    - <foldl or foldr> <f> <IV> ["use","the","force"];
    val it = "usetheforce" : string
*)
fun sfun1 (cv, acc) = cv^acc;
foldl sfun1 "" ["use","the","force"]; (*val it = "forcetheuse" : string*)
(*correct below*)
fun sfun2 (cv, acc) = acc^cv;
foldl sfun2 "" ["use","the","force"]; (*val it = "usetheforce" : string*)
(*or*)
fun sfun3 (cv, acc) = cv^acc;
foldr sfun3 "" ["use","the","force"]; (*val it = "usetheforce" : string*)

(*
Ex. Use one of the reduce functions to duplicate all the elements of a list. For example,
    - <foldl or foldr> <f> <IV> [2,3,5,7]
    val it = [2,2,3,3,5,5,7,7] : int list
*)
fun dfun (cv, acc) = (acc@cv)@cv;
foldl dfun [] [2,3,5,7];

(*
Lecture 1-5: Advanced Types

NEW TYPE: 'a option
This new type has "two" values
    NONE
    SOME x (* where x is of type 'a *)
*)
SOME 3; (* val it = SOME 3 : int option *)
SOME "winkelmann"; (* val it = SOME ""winkleman : string option *)
NONE; (* val it = NONE : 'a option *)
val L = [SOME 2, NONE, NONE, NONE, SOME 3, SOME 5, NONE, SOME 7, NONE]; (*val L = [SOME 2, NONE, NONE, NONE, SOME 3, SOME 5, NONE, SOME 7, NONE] : int option list*)
[2, 3, null, 4, null]; (*cant do bc all elements must be of the same type. ^this allows for this*)

(*
The option type allows "null values" that can represent "no answer", "no response", etc...
*)
length(L); (*val it = 9 : int*)

(*
Ex. Write a recursive function with pattern matching with name and type
    intopsum : int option list -> int
that inputs a list of int options and return the sum of all the integers in the list while ignoring any instances of NONE. For example,
    - intopsum L;
    val it = 17 : int
*)
fun intopsum [] = 0
    | intopsum (NONE::xs) = intopsum(xs)
    | intopsum ((SOME x)::xs) = x + intopsum(xs); (*val intopsum = fn : int option list -> int*)

intopsum(L); (*val it = 17 : int*)

(*
Ex. Write a recursive function with pattern matching with name and type
    stopsum : string option list -> string
that inputs a list of string options and returns the concatenation of all strings on the list while ignoring any instances of NONE. For example,
    - stopsum [NONE, SOME "hello", SOME "world", NONE];
    val it = "helloworld" : string
*)
fun stopsum [] = ""
    | stopsum (NONE::xs) = stopsum(xs)
    | stopsum ((SOME x)::xs) = x ^ stopsum(xs);

(*
Ex. Write a recursive function with pattern matching with name and type
    strip : 'a option list -> 'a list
that inputs a list of options and removes all SOMEs and NONEs leaving just the values in the list. For example,
    - strip L;
    val it = [2,3,5,7] : int list
*)
fun strip [] = []
    | strip (NONE::xs) = strip(xs)
    | strip ((SOME x)::xs) = x @ strip(xs); (*Not working*)
