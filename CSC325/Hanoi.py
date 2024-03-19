"""
Anish Katuwal, Caleb Matherne, Poojitha Soma
PS#2 (C-4.14)
Dec 14, 2023

If you guys think this is wrong or want to improve it, feel free to. I'm not 100% sure this is how it is intended to be implemented.
"""

def hanoi(n, start=1, end=3):
    if (n == 1): 
        print(f"Move {start} to {end}") 
        return
    spare = 6 - (start + end)
    hanoi(n-1, start, spare)
    print(f"Move {start} to {end}")
    hanoi(n-1, spare, end)

hanoi(3)