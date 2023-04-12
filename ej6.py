import csv
import re

regex = r'^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+)\s+(\S+)\s+(\S+)\s+---\s+\[(\S+)\]\s+(\S+)\s+:\s+(.*)$'

csv_file = 'logs.csv'

logs = []
log = input()
logs.append(log)
match = re.match(regex, log)

with open(csv_file, 'w') as file:
    for log in logs:
        if match:
            nivelLog = match.group(2)
            hilo = match.group(4)
            claseResponsable = match.group(5).split('.')[1]
            mensaje = match.group(6)

            file.write(f'"{nivelLog}","{hilo}","{claseResponsable}","{mensaje}"\n')
        else:
            print(None)

file.close()

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print('"'+row[0]+'",''"'+row[1]+'",''"'+row[2]+'",''"'+row[3].replace(',',' ')+'"')
