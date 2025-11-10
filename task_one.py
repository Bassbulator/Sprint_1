string = '1h 45m,360s,25m,30m 120s,2h 60s'

replaced_string = (string.replace('1h 45m', '105m')
                   .replace('360s', '6m')
                   .replace('30m 120s', '32m')
                   .replace('2h 60s', '121m'))

minutes = replaced_string.split(',')

total_minutes = [int(m[:-1]) for m in minutes]

print(sum(total_minutes))