covert="secret" + "EOF"
covert_bin = ""

for c in covert:
    covert_bin += (bin(ord(c))[2:]).zfill(8)

print(covert, covert_bin)

covert_unbin = ""
       
for i in range(0, len(covert_bin), 8):
    covert_unbin += chr(int(f'0b{covert_bin[i:i+8]}', 2))

print()
print(covert_bin, covert_unbin)