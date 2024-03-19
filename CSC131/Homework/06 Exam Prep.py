######################################################################
# author: Caleb Matherne
# date: 3/8/2022
# desc: Exam Prep Simulation Game
#####################################################################

DEBUG = True   # Activate intermediate output 

import random

def simulation(a,b,c,d,e):
    print("="*65)
    scores = []

    #runs multiple simulations
    for num in range(e):
        #get results from calculation
        test_studied, test_questions, test_correct = calculate(a,b,c,d)
        #keeping track of the score per test
        scores.append(len(test_correct))

        #print stats if debug=true
        if DEBUG==True:
            printstats(num, test_questions, test_studied, test_correct)     
    if DEBUG==True:
        print(f"Simulation scores were:\n{scores}")

    #count how many times correct answers > passreq
    passedcounter = 0
    for score in scores:
        if score >= d:
            passedcounter += 1

    print("="*65)
    print(f"You passed the test {(passedcounter/e)*100}% of the time.")


def printstats(n, a, b, c):   
    print(f"Simulation No. {n+1}\nQuestions you were asked: {a}\nQuestion you studied: {b}\nQuestions you passed: {c}\nWhich means you scored {len(c)}/{len(a)}")
    print("-"*65)


def calculate(a,b,c,d):
    #generate a list of test questions (0,bankquant)
    calc_bank = range(a)

    #makes a list of studied questions from the bank
    calc_studied = random.sample(calc_bank, b)

    #makes a list of questions from the bank
    calc_questions = random.sample(calc_bank, c)

    #makes a list of questions that both lists have in common
    calc_correct = generate_score(calc_studied, calc_questions)

    #return the data to simulation
    return calc_studied, calc_questions, calc_correct


def generate_score(b, c):
    correctlist = []
    #if the studied question is in the list of questions on the test, append it.
    for num in b:
        if num in c:
            correctlist.append(num)
    return correctlist

############
### MAIN ###
############

print("Simulation Set Up:")
print("="*65)

#user input
bankquant = int(input("What is the size of the question bank? "))
studiedquant = int(input("How many of those questions hae you studied? "))
testquant = int(input("How many questions does the test have? "))
passreq = int(input("How many questions must you answer correctly to pass the test? "))
print("="*65)
simquant = int(input("How many simulations do you want to run? "))

#execute simulation
simulation(bankquant,studiedquant,testquant,passreq,simquant)