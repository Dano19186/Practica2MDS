import re

entrada = input()
patron = "\\b\d{4}-\d{2}-\d{2}\\b"
patron2 = "\d{2,4}"
r = re.findall(patron, entrada)
l = " ".join(map(str, r))
separados = re.findall(patron2, l)
separados.reverse()
lsol = ".".join(map(str, separados))
sol = re.sub(patron, lsol, entrada)
print(sol)
