phonebook_dict = {}

command = input()
while '-' in command:
    name, number = command.split('-')
    phonebook_dict[name] = number
    command = input()

loop_range = int(command)
for search in range(loop_range):
    name = input()
    if name not in phonebook_dict.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook_dict[name]}")



