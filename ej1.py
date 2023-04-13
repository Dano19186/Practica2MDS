import re

entrada = input()
r = re.findall("\\b\\d{4}\\b", entrada)
for year in r:
    print(year)
