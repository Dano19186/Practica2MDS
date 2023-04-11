import re

entrada = input()
patron = r"\b(C\/|Calle)\s\b([A-ZÁ-ÚÑ][a-zá-úñ]+)\b,?\s+([n|N]º?\s?\d+|\d+),\s+(\d{5})\b"
r = re.findall(patron, entrada)
i = 0
while i < len(r):
    num = ""
    for c in r[i][2]:
        if c.isdigit():
            num = num + c
    print(r[i][3]+"-"+r[i][1]+"-"+num)
    i += 1
