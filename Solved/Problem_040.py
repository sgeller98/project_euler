# Project Euler Problem 40

strn = "0."
i = 1

while len(strn) < 1000002:
    strn += str(i)
    i += 1

result = (
    int(strn[1 + 1])
    * int(strn[10 + 1])
    * int(strn[100 + 1])
    * int(strn[1000 + 1])
    * int(strn[10000 + 1])
    * int(strn[100000 + 1])
    * int(strn[1000000 + 1])
)

print(result)
