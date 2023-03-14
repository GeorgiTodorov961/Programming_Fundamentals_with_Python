from collections import defaultdict

submissions = defaultdict(int)
students = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    input_data = command.split('-')
    name = input_data[0]
    language = input_data[1]

    if language == 'banned':
        for course, student_names in students.items():
            if name in student_names.keys():
                students[course].pop(name)
    else:
        submissions[language] += 1
        points = int(input_data[2])
        if language not in students.keys():
            students[language] = {}
        if name not in students[language]:
            students[language][name] = 0
        if students[language][name] < points:
            students[language][name] = points


print('Results:')
for course, users in students.items():
    for name, score in users.items():
        print(f"{name} | {score}")

print('Submissions:')
print('\n'.join(f'{language} - {count}' for language, count in submissions.items()))


