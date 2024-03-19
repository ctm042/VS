import random

scroll = int(input("What scroll?\n1 : Mystical\n2 : LD\n3 : Legendary\n\n"))
quant = int(input("\nHow many? : "))
print("\n")

nat5 = 0
nat4 = 0
nat3 = 0

for i in range(quant):
    if (scroll == 1) :
        key = random.randint(1,1000)
        if (key < 916) : nat3 += 1
        elif (key < 996) : nat4 += 1
        else : nat5 += 1

    elif (scroll == 2) :
        key = random.randint(1,10000)
        if (key < 9366) : nat3 += 1
        elif (key < 9966) : nat4 += 1
        else : nat5 += 1

    elif (scroll == 3) :
        key = random.randint(1,1000)
        if (key < 936) : nat4 += 1
        else : nat5 += 1
    
print(f"Nat 5's = {nat5}\nNat 4's = {nat4}\nNat 3's = {nat3}\n")