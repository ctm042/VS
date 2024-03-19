"""
Name : Caleb Matherne
Date 9/29/2021
Description
"""

name = input("What is your name? ")
#prompt for name
score1 = int(input("Hi, {}. What did you score on your first test? ".format(name)))
#prompt for first score (score1)
score2 = int(input("Alright. And what did you score on your second test? "))
#prompt for second score (score2)
print("With test scores {}% and {}%, your average average in the class is {}%".format(score1,score2,(score1+score2)/2))
#restate scores. average and print
