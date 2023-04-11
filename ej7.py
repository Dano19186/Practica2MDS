import re

entrada = input()
patron = r".*  ([A-Z]+).* --- \[(.*)\] .*\.([A-Z]\w+) *: (.*)"
r = re.findall(patron, entrada)
print(r[0], sep=",")

