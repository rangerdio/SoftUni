from collections import deque

total_water = int(input())
people = deque()

while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

while people:
    command = input().split()
    if command[0] == "refill":
        total_water += int(command[1])
    else:
        liters = int(command[0])
        if total_water >= liters:
            total_water -= liters
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
print(f"{total_water} liters left")
