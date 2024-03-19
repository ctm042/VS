####################################################################
# author: Caleb Matherne
# date: 11/7/2021
# desc: Random Grade Assignments Homework
###################################################################

from random import randint

# constants defined to limit the scope of the randomly generated grades.
LOWEST_GRADE = 65
HIGHEST_GRADE = 100

# A function that prompts the user for the number of students in the
# class and returns that value to the calling statement.
def get_quant():
    while(True):
        try:
            x= float(input("How many students are in this imaginary class? "))
            if isinstance(x,str)==True:
                print("ERROR: Amount should be an integer")
            elif x<=0:
                print("ERROR: Amount should greater than zero")
            elif x%1!=0:
                print("ERROR: Amount should be an integer")
            else:
                return int(x)
                break
        except ValueError:
            print("ERROR: Amount should be an integer")

# A function that receives the number of students as an argument, and
# creates a list of random integers of that size. The complete list is
# returned to the calling statement.
def get_grades(x):
    grades = []
    for a in range(x):
        grades.append(randint(LOWEST_GRADE,HIGHEST_GRADE))
    return grades

# A function that receives a single grade as its argument, and returns a
# letter corresponding to the correct letter grade.
def get_letter(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'

# A function that receives a list of values, and prints them in order
# separated by a tab space.
def print_values(x):
    for a in range(len(x)):
        print(str(x[a]),"\t", end = "")
    print("")

# A function that recieves a list of numerical values (corresponding to
# the numerical grades), and creates a list of corresponding letter
# grades. This list of letter grades is then returned to the calling
# statement.
def list_letters(x):
    y = []
    for a in range(len(x)):
        y.append(get_letter(x[a]))
    return y

# A function that recieves a list of numerical values, and returns the
# mean/average of that list.
def get_avg(x):
    return format((sum(x)/len(x)),'.1f')

############################# main ############################
# using functions defined above, get the class size, numerical grade
# list, and letter grade list.
students = get_quant()
grade_list = get_grades(students)
letter_list = list_letters(grade_list)

# Print out both numerical and letter grades as well as the average.
print("Numerical Grades:")
print_values(grade_list)
print("Letter Grades:")
print_values(letter_list)
print("The average grade for the class is {}".format(get_avg(grade_list)))
