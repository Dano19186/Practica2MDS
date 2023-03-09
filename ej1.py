import re

entrada = input()
r = re.findall("\ \d{4}\ ", entrada)
print(*r)
