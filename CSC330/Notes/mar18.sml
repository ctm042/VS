(* lecture 1-3: ML Functions

Function declarations in ML have the syntax
	fun <identifier> <parameters> = <expression>
	
The type of this function when <parameters> has type T1 and <expression> has type T2 is T1 -> T2

Note: fn is ML's symbol for a function (whose details are hidden) 
 *)
fun spongebob x = x+1;
spongebob(48);
	val it = 49 : int
spongebob;
	val it = fn : int -> int
it(9)
	val it = 10 : int

(* 
Ex. Write a function with name/type
	rsquare : real -> real
that inputs a real number and returns its square value
 *)
fun rsquare x:real = x*x;
rsquare(5.0)
	val it = 25.0 : real
	
(* 
NOTE: You can use the : to associate a value with a type, but only do this when necessary.
NOTE: + and * are defaulted to int types

 *)

(* 
Ex. (in-class) Write a function with name/type                  (camelCase)
	toUpper : char -> char
that inputs a lowercase char and returns its uppercase version. Assume valid inputs.
	- toUpper(#"d")
	val it = #"D" : char
 *)
fun toUpper x = chr(ord(x) + 26)

(* 
Ex. Write a function with name/type
	max3 : int * int * int -> int
that inputs a 3-tuple of integers and returns the max value
	- max3(2,9,5);
	val it = 9 : int
 *)
fun max3 (a,b,c) = 
