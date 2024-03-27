(*Happy Birthday Dustin. Enjoy 22*)


(*Continue lecture 1.3: functions and anonymous functions! and remember that functions are expressions! yay*)
(*=======================================================================================================================*)
(*chr is a function so it is an expression but it just takes an int and returns its character (#'a) *)
chr(97);
chr;

(*                  
Write a function named apply that inptus a function and returns a tuple and then retuns the input function applied to the value 



val apply = fn : ('a -> 'b) * 'a -> 'b
first input: function that takes in an alpha and returns a beta 
second input: alpha value 
output: beta value 

the compiler doesn't know what the function does or the parameters, so it assigns those greek values (alpha,beta,gamma,etc)
(variable,variable) = tuple 
*)

fun apply (f,a) = f(a);

fun g x = x+1;
fun h x = 3*x;

apply (g,7);
apply(chr,97);
(*=======================================================================================================================*)
(*don't use global variables a lot the below example doesn't change anything, but could act very silly later*)

val k = 4;
fun f8 y = y+k;
val k = 20;
f8(3);

(*=======================================================================================================================*)

(*
Anonymous functions!!!
AKA Functions defined on the fly
AKA Functions without a name 

fn (parameters) => expression

remember, "it" pulls the last expression used 
*)

fn x  => x+1;
it(8);

apply(fn x => x*x, 10);


(*Write a function named getfun that inputs a number  and then returns a function*)

fun getfun c = fn x => c*x;

val f9 = getfun(69);

f9(10);

(*
Ex. (in-class) Write a function that inputs a string s and then returns the function that concatonates its input string w to return ws 
*)

fun suffix s = fn w => w^s;
val pastFun = suffix("ed");
pastFun("box");

(*Ex. (in-class) Write a function that inputs boolean p and returns the function XOR(q) = p xor q*)

fun getFun3 q = fn p => if (p = q) then false else true;
val f10 = getFun3(true);
f10(true);
(*it gave me a warning, but ignore it! :3*)

(*Write a function that inputs a boolean b . if b is true it returns function f(x,y)=x+y if b is false it returns f(x,y) = x*y name it getFun4  *)
fun getFun4 b = if (b) then fn(x,y) => x+y else fn(x,y) => x*y;
val f11 = getFun4(false);
f11(3,5);


(*End of lecture*)
(*=======================================================================================================================*)
