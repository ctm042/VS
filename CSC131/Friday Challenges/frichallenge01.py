my_string = input("What is your sentence? ")
find = input("What letter do you want to find? ")
print(f"There are {(str.lower(my_string)).count(str.lower(find))} {find}'s in the sentence {my_string}.")
