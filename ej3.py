import re

entrada = input()
patron = "\\b(\\d{4})-(\\d{2})-(\\d{2})\\b"
r = re.findall(patron, entrada)
year, mes, day = r[0][0], r[0][1], r[0][2]
invertido = day+"."+mes+"."+year
sol = re.sub(patron, invertido, entrada)
print(sol)
