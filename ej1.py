import re

entrada = input()
r = re.findall("[\w]*\d{4}[\w]*", entrada)
print(*r)
