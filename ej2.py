import re

entrada = input()
r = re.findall("E?[\\-\\ ]?[0-9]{4}[-\\ ]?[A-Z]{3}", entrada)

for e in r:
    print(e.strip())
