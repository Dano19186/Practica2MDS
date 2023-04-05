import re

regex = r'^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+)\s+(\S+)\s+(\S+)\s+---\s+\[(\S+)\]\s+(\S+)\s+:\s+(.*)$'

csv = 'logs.csv'

logs = []
log = input()
logs.append(log)

with open(csv, 'w') as csv_file:
    if csv_file.tell() == 0:
        csv_file.write('"Nivel de log","Hilo","Clase responsable","Mensaje de log"\n')

    for log in logs:
        match = re.match(regex, log)
        if match:
            nivelLog = match.group(2)
            hilo = match.group(4)
            claseResponsable = match.group(5).split('.')[0]
            mensaje = match.group(6)

            csv_file.write(f'"{nivelLog}","{hilo}","{claseResponsable}","{mensaje}"\n')

