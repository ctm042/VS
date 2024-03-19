#################################################################################
# name: Caleb Matherne
# date: 10/11/2021
# description: Number Properties Program
#################################################################################

# A function that prompts the user for a number and returns it.
def get_num():
    return int(input("Enter a number: "))


# A function that receives two numbers as arguments, and returns the
# larger of the two numbers.
"""
I found that i didnt need to use this definition.
Honestly, I forgot about it and managed to work around it without any problems.
"""
def get_greater(a,b):
    if a > b:
        x = a
    else:
        x = b
    return x

# A function that receives three numbers as arguments, and returns the
# largest of the three numbers.
def get_greatest(a,b,c):
    if (a > b) and (a > c):
        x = a
    elif (b > a) and (b > c):
        x = b
    else:
        x = c
    return x

# A function that receives three numbers as arguments, and returns the
# product of the two largest arguments.
def get_max_product(a,b,c):
    return get_greatest(a*b,a*c,b*c)
    

# A function that receives an argument and returns a string representing
# whether that argument is even or odd.
def get_evenodd(a):
    if (a%2) == 0:
        x = "even"
    else:
        x = "odd"
    return x
        
# A function that receives an argument and determines whether that
# argument is a prime number.
def is_prime(a):
    n=2
    x=True
    while (x!=False and a>n):
        if a%n==0:
            x = False
        else:
            n += 1
    return x

##################################### MAIN PROGRAM #######################
# Functions that were defined above should be executed below in an order
# that satisfies the original problem statement. Additional statements
# can be included if needed.
##########################################################################

# Prompt for three different numbers and store them appropriately.
num1 = get_num()
num2 = get_num()
num3 = get_num()

# Print out the table header information.
print("--------------------\nNum\tEven\tPrime\n--------------------")

# Print out the table contents for each of the three numbers.
print("{}\t{}\t{}".format(num1,get_evenodd(num1),is_prime(num1)))
print("{}\t{}\t{}".format(num2,get_evenodd(num2),is_prime(num2)))
print("{}\t{}\t{}".format(num3,get_evenodd(num3),is_prime(num3)))

print("--------------------")

# Print out the identity of the largest number and the largest product
# from the given numbers.
print("The largest number is {}".format(get_greatest(num1,num2,num3)))
print("The largest possible product is {}".format(get_max_product(num1,num2,num3)))
