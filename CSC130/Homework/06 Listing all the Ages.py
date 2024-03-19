##############################################################################
# author: Caleb Matherne
# date: 11/3/2021
# description: Listing all the Ages
"""
NOTE: I wanted to try to make this program as reduntant as possible so that it will not break.
      I bet you THREE WHOLE NICKLES that you won't be able to break my program. Good luck :)
      (no cheating)
"""
#############################################################################

# A function that prompts the user for the number of people this program
# will be comparing.
def getquant():
    while(True):
        try:
            x= float(input("How many people are you comparing? "))
            if isinstance(x,str)==True:
                print("ERROR: Quantity should be an integer")
            elif x<=0:
                print("ERROR: Quantity should greater than zero")
            elif x%1!=0:
                print("ERROR: Quantity should be an integer")
            else:
                return int(x)
                break
        except ValueError:
            print("ERROR: Quantity should be an integer")
    print("-"*45)

# A function that receives the size of a list, and repeatedly prompts the user
# for that number of names. It then returns the complete list of names.
def getnames(quant):
    nlist=[]
    for x in range(quant):
        nlist.append(input("What is the name of person number {}: ".format(x+1)))
    print("-"*45)
    return(nlist)


# A function that receives the size of a list, and repeatedly prompts
# the user for that number of ages. It then returns the complete list of
# ages.
def getages(quant):
    alist=[]
    x = 1
    while x <= quant:
        try:
            age = float(input("What is the age of person number {}: ".format(x)))
            if (age)%1==0:
                alist.append(int(age))
            else:
                alist.append(age)
            x+=1
        except ValueError:
            print("ERROR: Age should be a number")
    print("-"*45)
    return(alist)

################################ MAIN ################################
# Ask for the number of people using one of the functions defined above.
quantity = getquant()

# Ask for the names of the people using one of the functions defined
# above.
namelist = getnames(quantity)

# Ask for the ages of the people using one of the functions defined
# above.
agelist = getages(quantity)

# Identify the names of the youngest and oldest people in the list.
print("{} is the youngest at {} years old".format(namelist[agelist.index(min(agelist))],agelist[agelist.index(min(agelist))]))
print("{} is the oldest at {} years old".format(namelist[agelist.index(max(agelist))],agelist[agelist.index(max(agelist))]))

# Display information about the lists.
print("The average age is {}".format(sum(agelist)/len(agelist)))
