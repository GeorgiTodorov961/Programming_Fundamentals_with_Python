employes = list(map(int, input().split()))
happy_factor = int(input())
increase_happy = [person * happy_factor for person in employes]
happy_employee = [happy for happy in increase_happy if happy > (sum(increase_happy) / len(increase_happy))]

if len(happy_employee) >= len(employes) // 2:
    print(f"Score: {len(happy_employee)}/{len(employes)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employee)}/{len(employes)}. Employees are not happy!")


