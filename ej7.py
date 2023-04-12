import re

entrada = input()
patron = r".*  ([A-Z]+).* --- \[(.*)\] .*\.([A-Z]\w+) *: (.*)"
r = re.findall(patron, entrada)
for i in range(len(r)):
    j = 0
    while j < len(r[i])-1:
        print('"'+r[i][j]+'"', end=",")
        j += 1
    print('"'+r[i][j]+'"')

