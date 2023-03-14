university = {}
course = ''
while True:
    command = input()
    if ":" not in command:
        course = command.replace("_", ' ')
        break

    name, number, discipline = command.split(':')
    if discipline not in university:
        university[discipline] = []
    university[discipline].append(f'{name} - {number}')

print(*university[course], sep='\n')

