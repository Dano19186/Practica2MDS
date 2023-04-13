import re

entrada = input()
patron = r"\b\d{4}\b"
r = re.findall(patron, entrada)
for year in r:
    print(year)
