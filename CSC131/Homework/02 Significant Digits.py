##########################################################################
# author: Caleb Matherne 
# date: 12/8/2021
# desc: Significant Digits Homework
#########################################################################
#from random import randint, seed
import random
SHOWLIST = False 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.

# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.

def getinput(prompt1,prompt2):
    inputlist = []
    inputlist.append(int(input(prompt1)))
    inputlist.append(int(input(prompt2)))
    return inputlist
    # not sure why this cant just be two individual input("")


# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.

def printrow(name,numlist):
    print(name,"\t",end="")
    for x in range(len(numlist)):
        print(numlist[x],end="\t")
    print("\r")
        


# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.

def getrandom(quantity,seed):
    randlist=[]
    random.seed(seed)
    global MIN
    global MAX
    for x in range(quantity):
        randlist.append(random.randint(MIN,MAX))
    return randlist



# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.

def getMSDfreq(randlist):
    MSDfreq = [0]*10
    for num in range(len(randlist)):
        MSDfreq[int(str(randlist[num])[0])] += 1
        #This line took me 2 hours to make. I wish I were joking...
    return MSDfreq
    


# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.

def getLSDfreq(randlist):
    LSDfreq = [0]*10
    for num in range(len(randlist)):
        LSDfreq[int(str(randlist[num])[-1])] += 1
    return LSDfreq



###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
userinputs = getinput("How big a list do you want to create? ","What seed should be used for its creation? ")



#   create the list of random numbers
randlist = getrandom(userinputs[0],userinputs[1])



#   If SHOWLIST is selected, print out the list of numbers
if SHOWLIST==True:
    print(f"Original List:\n{randlist}")
    print("-"*85)



#   print the head of the table which just shows the numbers 0-9
printrow("", ['0','1','2','3','4','5','6','7','8','9'])
print("-"*85)



#   Calculate the MSD and LSD, and print out their statistics.
printrow("MSD",getMSDfreq(randlist))
printrow("LSD",getLSDfreq(randlist))