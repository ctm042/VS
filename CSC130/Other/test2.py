import random
listlen = int(input("How long is the list? "))
randlist = []
for a in range(listlen):
    randlist.append(random.randint(1,9))
print(randlist)
