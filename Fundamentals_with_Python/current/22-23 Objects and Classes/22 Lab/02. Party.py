class Party:
    counter = 0
    def __init__(self):
        self.people = []


party = Party()
name = input()
while name != "End":
    party.people.append(name)
    Party.counter += 1
    name = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {Party.counter}")
