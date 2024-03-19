import os

def Select():
    choice = input("1 : IEEE to Decimal\n2 : Decimal to IEEE\n")
    if choice == "1": IEEE2Dec()
    else: Dec2IEEE()

def IEEE2Dec():
    sign = str(input("Sign bit = "))
    exp = str(input("Exponent bits = "))
    frac = str(input("Fraction bits = "))
    os.system('cls')

    norm, zero, inf, nan = GetCase(exp, frac)
    
    print(f"Sign bit =      {sign}")
    print(f"Exponent bits = {exp}")
    print(f"Fraction bits = {frac}")
    print(f"Normalized = \t{norm},\nZero = \t\t{zero},\nInfinite = \t{inf},\nNaN = \t\t{nan}\n")

    if nan: #NaN
        v = "NaN"

    elif inf: #Infinite
        s = 1 if int(sign) == 0 else -1
        v = "+Infinity" if s == 1 else "-Infinity"
    
    elif zero: #Zero
        s = 1 if int(sign) == 0 else -1
        v = "+0" if s == 1 else "-0"
    
    elif not norm: #Denormalized
        s = 1 if int(sign) == 0 else -1
        bias = GetBias(len(exp))
        e = 1 - bias
        mantissa = BinDToDecD(frac)

        print("bias = 2^(k-1)-1")
        print(f"bias = {bias}")
        print("e = 1 - bias")
        print(f"e = 1 - {bias}")
        print(f"e = {e}\n")

        print("V = -1^s * 0+frac * 2^e")
        print(f"V = {s} * {mantissa} * 2^{e}")
        v = ((s) * (mantissa) * (2**e))
    
    else: #Normalized
        s = 1 if int(sign) == 0 else -1
        bias = GetBias(len(exp))
        expdec = BinToDec(exp)
        e = expdec - bias
        mantissa = BinDToDecD(frac)

        print("bias = 2^(k-1)-1")
        print(f"bias = 2^({len(exp)}-1)-1")
        print(f"bias = {bias}")
        print("e = exp - bias")
        print(f"e = {expdec} - {bias}")
        print(f"e = {e}\n")

        print("V = -1^s * 1+frac * 2^e")
        print(f"V = {s} * {1+mantissa} * 2^{e}")
        v = ((s) * (1+mantissa) * (2**e))
    
    print(f"V = {v}")

def Dec2IEEE():
    num = str(input("Number to convert = "))
    explen = int(input("Exponent length = "))
    fraclen = int(input("Fraction length = "))
    os.system('cls')
    
    sign = 1 if num[0] == "-" else 0
    num = num.lstrip("-")

    if "." in num:
        whole, decimal = num.split(".")
    else:
        whole = num
        decimal = 0

    e = len(str(DecToBin(whole)))-1
    bias = GetBias(explen)
    exp = e + bias

    expbits = DecToBin(exp)
    mantissabits = str(DecToBin(whole)) + str(DecDToBinD(decimal, fraclen))
    mantissabits = mantissabits[1:]

    print(num)
    print(str(DecToBin(whole)) + "." + str(DecDToBinD(decimal, fraclen)))
    print(f"1.{mantissabits}")
    print(f"e = {e}")

    print("bias = 2^(k-1)-1")
    print(f"bias = 2^({explen}-1)-1")
    print(f"bias = {bias}")
    print("exp = e + bias")
    print(f"exp = {e} + {bias}")
    print(f"exp = {exp}\n")
    
    print(f"Sign bit =      {sign}")
    print(f"Exponent bits = {expbits}")
    print(f"Fraction bits = {mantissabits}")


### Helper functions ###
def GetCase(exp, frac):
    Normalized = True
    Zero = False
    Infinite = False
    NaN = False

    if exp.count("0") == len(exp): #x|000|xxx
        Normalized = False
        if frac.count("0") == len(exp): #x|000|000
            Zero = True
    elif exp.count("1") == len(exp): #x|111|xxx
        Normalized = False
        if frac.count("0") == len(exp): #x|111|000
            Infinite = True
        else: #x|111|001 - 111
            NaN = True

    return Normalized, Zero, Infinite, NaN

def GetBias(num):
    return 2**(int(num)-1)-1

def BinToDec(bin):
    return int(bin, 2)

def DecToBin(num):
    return int(bin(int(num))[2:])

def BinDToDecD(bin):
    total = 0
    for i in range(len(bin)):
        if int(bin[i]) == 1:
            total += 2**((i+1)*-1)
    return total

def DecDToBinD(fractionalPart, precision): 
    binary = ""  
    fractionalPart = float("0." + str(int(fractionalPart)))
    while (precision):
        fractionalPart *= 2
        bit = int(fractionalPart)
        if (bit == 1) :   
            fractionalPart -= bit  
            binary += '1'
        else : 
            binary += '0'
        precision -= 1
    return binary  

Select()
