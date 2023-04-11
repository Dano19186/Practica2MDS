import re

entrada = input()
patron = "\\b([a-zA-Z]+)\\.([a-zA-Z]+)(\\.([0-9]{4})@alumnos.urjc.es|@urjc.es)\\b"
r = re.findall(patron, entrada)
i = 0
while i < len(r):
    if r[i][2] == "@urjc.es":
        print("profesor "+r[i][0]+" apellido "+r[i][1])
    else:
        print("alumno "+r[i][1]+" matriculado en "+r[i][3])
    i += 1
