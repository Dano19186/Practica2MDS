import re

entrada = input()
patron = r"\b([a-zA-Z]{1}\.([a-zA-Z]{2,})\.(\d{4})(@alumnos\.urjc\.es))|(([a-zA-Z]+)\.([a-zA-Z]+)@urjc\.es)\b"
r = re.findall(patron, entrada)
i = 0
while i < len(r):
    if r[i][3] != "@alumnos.urjc.es":
        print("profesor "+r[i][5]+" apellido "+r[i][6])
    else:
        print("alumno "+r[i][1]+" matriculado en "+r[i][2])
    i += 1
