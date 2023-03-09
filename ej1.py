import re

entrada = input()
r = re.findall("^|[^0-9](\d{4})[^0-9]|$", entrada)
for
