################################################################################
# Name: Caleb Matherne
# Date: 10/5/2021
# Description: Easy Does It Reloaded
################################################################################

# A function that prompts the user for a name and returns it to the
# calling statement.
def getname():
    name = input("Please enter your name: ")
    return (name)

# A function that prompts the user for a score and returns it to the
# calling statement.
def getscore():
    score = float(input("Enter you score: "))
    return (score)

# A function that receives two numbers and returns the average of those
# two values to the calling statement.
def getavg(a,b):
    return (a+b)/2
    
# A function that receives a string and a number (the name and the
# average score) and prints it out on the screen in the appropriate format.
def comp(name,avg):
    print("Hi, {}. Your average score is {}.".format(name,avg))

#############################################################################
#       MAIN PART OF PROGRAM
# Functions that were defined above should be executed below in an order
# that satisfies the problem statement. Additional statements can be
# included below as well if needed.
#############################################################################

# prompt for name
name = getname()

# prompt for two scores
score1 = getscore()
score2 = getscore()

# calculate the average
avg = getavg(score1,score2)

# display the final output
comp(name,avg)
