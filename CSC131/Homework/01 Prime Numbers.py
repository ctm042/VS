#######################################################################
# author: Caleb Matherne
# date: 12/03/2021 
# desc: How Many Prime Numbers?
########################################################################

#########################
""" BARE-MINIMUM CODE """
#########################
""" Satisfies the given sample questions and requirements"""
"""

# A function to prompt the user for a number and return that value to
# the calling statement.
def prompt(a):
    return int(input(a))

# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
def primecheck(p):
    state = True
    if p == 1:
        state = False
    elif p == 2:
        state = True
    else:
        for div in range(2,int(p)):
            if p%div==0:
                state = False
    return state

################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.
num = prompt("What limit are you interested in? ")
primelist = []
for x in range(2,int(num)):
    if primecheck(x)==True:
        primelist.append(x)
print(f"There are {len(primelist)} prime numbers less than {num}")
print(primelist)

"""

#############
""" EXTRA """
#############
""" Because I like to be extra. Kept in debug from building and added 
countermeasures to prevent it from breaking if the user wants to try
entering stupid things into the input like float values or strings.
Add quotations before and after the bare-minimum code and romeve the
quotations from the extra code to try it. I dare you to try and break
it. No cheating of course. :) """



debug = True
# Change this to True if you want #

def prompt(a):
    while True:
        try:
            a = float(input(a))
            return a
        except:
            print("Please enter a number.")

def primecheck(p):
    state = True
    if p == 1:
        state = False
    elif p == 2:
        state = True
    else:
        for div in range(2,int(p)):
            if p%div==0:
                # start debug #
                if debug==True:
                    print(f"{p} mod {div} = {p%div}")
                # end debug #
                state = False
    # start debug #
    if debug==True and state == True:
        print(f"Found no divisor for {p}\n","-"*5,f"{p} is Prime","-"*5,"\n")
    if debug==True and state == False:
        print("","-"*3,f"{p} is not Prime","-"*3,"\n")
    # end debug #
    return state

num = prompt("What limit are you interested in? ")
if num > int(num):
    numr = int(num) + 1
    # start debug #
    if debug==True:
        print(f"{num} was rounded up to {numr}")
    # end debug #
else:
    numr = num
primelist = []
for x in range(2,int(numr)):
    if primecheck(x)==True:
        primelist.append(x)
print(f"There are {len(primelist)} prime numbers less than {num}")
print(primelist)

