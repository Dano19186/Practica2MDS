import re

regex = r'\b\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+\s+(\S+)\s+\S+\s+---\s+\[(\S+)\]\s+[a-z.]*([A-Z]\S+)\s+:\s+(.*)'

csv_file = 'logs.csv'

log = input()
match = re.match(regex, log)

with open(csv_file, 'w') as file:
    if match:
        nivelLog = match.group(1)
        hilo = match.group(2)
        claseResponsable = match.group(3)
        mensaje = match.group(4)

        file.write(f'"{nivelLog}","{hilo}","{claseResponsable}","{mensaje}"\n')

file.close()

if match:
    with open(csv_file, 'r') as file:
        for line in file:
            print(line)
