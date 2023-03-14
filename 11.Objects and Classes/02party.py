class Party:

    def __init__(self, people=[]):
        self.people = people

    def invited_people(self, human):
        self.people.append(human)

    def going_names(self):
        return f'Going: {", ".join(self.people)}'

    def quantity_people(self):
        return f"Total: {len(self.people)}"


party = Party()

while True:
    command = input()
    if command == 'End':
        break

    name = command
    party.invited_people(name)

print(party.going_names())
print(party.quantity_people())
