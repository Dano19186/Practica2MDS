import re

regex = r'\b\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+\s+(\S+)\s+\S+\s+---\s+\[(\S+)\]\s+[a-z.]*([A-Z]\S+)\s+:\s+(.*)'

log = input()
match = re.match(regex, log)

if match:
    nivelLog = match.group(1)
    hilo = match.group(2)
    claseResponsable = match.group(3)
    mensaje = match.group(4)

    line = '"'+nivelLog+'","'+hilo+'","'+claseResponsable+'","'+mensaje+'"'
    print(line)

else:
    print(None)
