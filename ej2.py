import re

entrada = input()
r = re.findall("(E |E-)?\\-?\\d{4}\\ ?\\-?[A-Z]{3}", entrada)
print(*r)

