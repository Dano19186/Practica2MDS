import re

entrada = input()
sol = entrada
patron = "\\b(\\d{4})-(\\d{2})-(\\d{2})\\b"
r = re.findall(patron, entrada)
for i in range(len(r)):
    year, mes, day = r[i][0], r[i][1], r[i][2]
    origin = year+"-"+mes+"-"+day
    invertido = day+"."+mes+"."+year

    sol = re.sub(origin, invertido, sol)

print(sol)
