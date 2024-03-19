#!/bin/bash

echo Printing #echo is printing
read var1 #input from user
read -p "Can also prompt with message: " var2
read -p "Multiple variables: " var2 var3 #varN
echo "var2 = $var2, var3 = $var3" # $ means the value of the variable
echo "shell = $SHELL, logname = $LOGNAME, pwd = $PWD" #are system variables
var4=4 #set variables in code with NO SPACES
echo "$0 is the name of this script"
#$1 - $9 are other parameters that are called with the script
echo "# of parameters = $#" #quantity of parameters
echo "string of parameters = $*" #all parameters on one string
echo "aray of string parameters = $@" #all parameters in an array
echo "status of most recently executed command = $?" #boolean
echo "pid = $$" #process id of current process
echo 'variable 1 = $var1'
echo "variable 1 = $var1"


#if-then-else
if test -f "$1"; then
    echo "parameter $1 is a file"
elif [ -f "$1" ]; then
    echo "parameter $1 is still a file"
elif [ -d "$1" ]; then
    echo "parameter $1 is a directory"
else
    echo "parameter $1 is not a file nor a directory"
fi

#Relational Operators
#Numeric operators
# -gt : Greater than
# -ge : Greater than or equal
# -lt : Less than
# -le : Less than or equal
# -eq : Equal
# -ne : Not equal
#String operators
# = or ==     : Equal
# !=          : Not equal
# str1 < str2 : str1 is less than str2
# str1 > str1 : str1 is greater than str2
# -n str      : str length is greater than 0
# -z str      : str length is 0

#Compound Logical Expressions
# && : and
# || : or
# must be enclosed with [[  ]]

#File Flags
# -d : True if 'file' is a directory
# -f : True if 'file' is an ord. file
# -r : True if 'file' is readable
# -w : True if 'file' is writable
# -x : True if 'file' is executable
# -s : True if length of 'file' is nonzero

#Case statement
#case word in
#   pattern1) commands1
#   ;;
#   pattern2) commands2
#   ;;
#   pattern3) commands3
#   ;;
#esac
#multiple patterns can be listed via: |

#while [ expression ]; do
#   commands
#done

#until [ expression ]; do
#   commands
#done

#for variable in argument list; do
#   commands
#done

#Break = transfer control to the statement AFTER the done statement
#        terminate execution of the loop

#Continue = skip the test statements for the current iteration
#           continues execution of the loop

#Functions
#function-name () {
#   statements
#}
#function-name
#Must be defined before they can be referenced
#Usually placed at the beginning of the script
#Parameters provided via function call are accessible inside function as $1, $2, $3, …
# $# reflects number of parameters of the function
# $0 still contains name of script (not name of function)

#Local variables can be defined with the local keyword

#Shift eats $1 and shifts the parameters to fill 