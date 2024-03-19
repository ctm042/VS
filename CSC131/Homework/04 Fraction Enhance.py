######################################################################################################################
# Name: Caleb Matherne
# Date: 1/11/2022
# Description: Fraction Enhance 
######################################################################################################################

# the fraction class
class Fraction:
    def __init__(self, num=0, den=1):
        self.num = num
        if den == 0:
            den = 1
        self.den = den

    @property
    def num(self):
        return self._num
    @num.setter
    def num(self,value):
        self._num = value

    @property
    def den(self):
        return self._den
    @den.setter
    def den(self,value):
        if value != 0:
            self._den = value
    
    def __add__(self, other):
        numerator = (self.num * other.den) + (self.den * other.num)
        denominator = self.den * other.den
        sum = Fraction(numerator, denominator)
        sum.reduce()
        return sum

    def __sub__(self, other):
        numerator = (self.num * other.den) - (self.den * other.num)
        denominator = self.den * other.den
        dif = Fraction(numerator, denominator)
        dif.reduce()
        return dif

    def __mul__(self, other):
        numerator = self.num * other.num
        denominator = self.den * other.den
        prod = Fraction(numerator, denominator)
        prod.reduce()
        return prod

    def __truediv__(self, other):
        numerator = self.num * other.den
        denominator = self.den * other.num
        prod = Fraction(numerator, denominator)
        prod.reduce()
        return prod

    def reduce(self):
        for a in range(1,int(self.den/2)):
            if self.den % a == 0 and self.num % a== 0:
                gcd = a
        if self.num == 0:
            self.den = 1
        self.num = int(self.num/gcd)
        self.den = int(self.den/gcd)
        

    def __str__(self):
        return f"{self.num}/{self.den} ({self.num/self.den})"


# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)
print("f4:", f4)

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print()
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)
print("f4:", f4)