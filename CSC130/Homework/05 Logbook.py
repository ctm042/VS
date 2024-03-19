########################################################################
# author: Caleb Matherne
# date: 10/29/2021
# description: Logbook Homework Assignment
########################################################################

from math import log10

def getfixedvar(string):
    var = str(float(input(string)))
    fixedvar = str(var.lstrip('0'))
    if fixedvar.index('.')==0:
        fixedvar = '0'+fixedvar
    return float(fixedvar)



# A function that prompts the user for the minimum value and returns it
# to the calling statement. Function to also deal with range checking to
# make sure that minimum value provided is greater than 0

def getmin():
    while(True):
        minvar = getfixedvar("What is the minimum value? ")
        if minvar > 0:
            return minvar
            break
        else:
            print("ERROR: Minimum should be greater than 0")



# A function that prompts the user for the maximum value and returns it
# to the calling statement. Function receives argument that is used in
# range checking to make sure maximum value provided by user is greater
# than minimum value (provided in function argument)

def getmax(minvar):
    while(True):
        maxvar = getfixedvar("What is the maximum value? ")
        if maxvar > minvar:
            return maxvar
            break
        else:
            print("ERROR: Maximum should be greater than {}".format(minvar))



# A function that prompts the user for the step size and returns it to
# the calling statement. Function also deals with range checking to make
# sure that step size provided is greater than 0.

def getstep():
    while(True):
        stepvar = getfixedvar("What is the step size? ")
        if stepvar > 0:
            return stepvar
            break
        else:
            print("ERROR: Step size should be greater than 0")


            
# A function that receives a number as an argument and returns the log
# of that number rounded to 4 decimal places.

def getlog(num):
    return format(round(log10(float(num)),4),'.4f')
    #return (num)



# A function that receives the value at the left size of the log table
# (i.e. the value whose logarithms should be calculated). The function
# then creates a row of logarithmic values for that argument counting
# upwards in steps of 1 significant figure more than the argument. i.e.
# if the argument is 1.3, then the row gives values of the logs for
# 1.30, 1.31, 1.32, 1.33, ..., 1.39. If the argument is 2.456, then it
# gives logs for 2.4560, 2.4561, 2.4562, 2.4563, ..., 2.4569

def construct_row(leftnum):
    leftnum=str(leftnum)
    if leftnum.rfind('0')+1 != len(leftnum):
        leftnum = (str(leftnum)+'0')
    print(format(float(leftnum), '.4f'),"",
          getcolumn(leftnum,'0'),""*3,
          getcolumn(leftnum,'1'),""*3,
          getcolumn(leftnum,'2'),""*3,
          getcolumn(leftnum,'3'),""*3,
          getcolumn(leftnum,'4'),""*3,
          getcolumn(leftnum,'5'),""*3,
          getcolumn(leftnum,'6'),""*3,
          getcolumn(leftnum,'7'),""*3,
          getcolumn(leftnum,'8'),""*3,
          getcolumn(leftnum,'9'))

def getcolumn(num,column):
    num = round(float(num),4)
    num = str(num)+'0'
    index = num.rfind('0')
    num = num[:index] + column
    return getlog(num)
    

    
# A function that receives the minimum, maximum and step size as
# arguments, and prints the table (making use of the function that
# creates a single row defined earlier)

def construct_table(minvar,maxvar,stepvar):
    while minvar <= maxvar:
        construct_row(minvar)
        minvar += stepvar



####################### MAIN #########################################
# Get the minimum, maximum and step size from the user using functions
# defined earlier.

minnumber = getmin()
maxnumber = getmax(minnumber)
step = getstep()


# create the table using the function defined eariler.

print("       ",0,
      "     ",1,
      "     ",2,
      "     ",3,
      "     ",4,
      "     ",5,
      "     ",6,
      "     ",7,
      "     ",8,
      "     ",9,
      "\n","-"*85)
construct_table(minnumber,maxnumber,step)
