from collections import defaultdict

course_dict = defaultdict(list)

while True:
    command = input()
    if command == 'end':
        break
    course_name, student_name = command.split(' : ')
    course_dict[course_name].append(student_name)

for course, students in course_dict.items():
    print(f"{course}: {len(students)}")
    print('\n'.join(f"-- {name}" for name in students))


