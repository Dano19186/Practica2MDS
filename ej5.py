import re

entrada = input()
patron = "\\b(C\/|Calle) ([a-zA-z]+) (Nº \d{1,}|\d{1,}|N\d{1,}), (\d{5})\\b"
r = re.findall(patron, entrada)
i = 0
print(r)
while i < len(r):
    num = ""
    for c in r[i][2]:
        if c.isdigit():
            num = num + c
    print(r[i][3]+"-"+r[i][1]+"-"+num)
    i += 1
