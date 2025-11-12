string = '1h 45m,360s,25m,30m 120s,2h 60s'

splited_string = string.split(',')

total_minutes = 0

for min in splited_string:
    min = min.replace(' ', '')

    if 'h' in min:
        parts = min.split('h')
        hours = int(parts[0])
        total_minutes += hours * 60
        min = parts[1]

    if 'm' in min:
        parts = min.split('m')
        minutes = int(parts[0])
        total_minutes += minutes
        min = parts[1]

    if 's' in min:
        parts = min.split('s')
        seconds = int(parts[0])
        total_minutes += seconds // 60

print(total_minutes)