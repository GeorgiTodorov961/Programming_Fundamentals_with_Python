companies_dict = {}

while True:
    command = input()
    if command == 'End':
        break
    company, id = command.split(' -> ')
    if company not in companies_dict.keys():
        companies_dict[company] = []
    if id not in companies_dict[company]:
        companies_dict[company].append(id)

for company_name, employees in companies_dict.items():
    print(company_name)
    print('\n'.join(f'-- {employee_id}' for employee_id in employees))


