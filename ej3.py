import re

entrada = input()
patron = "\\b(?:E |E-|E)?\d{4}\ ?\-? ?[A-Z]{3}"
r = re.findall(patron, entrada)
print(*r, sep="\n")