from collections import deque
num_pumps = int(input())
petrol_amount = 0

pumps = deque()
for _ in range(num_pumps):
    pumps.append([int(data) for data in input().split()])

pumps_copy = pumps.copy()
index = 0
gas = 0

while pumps_copy:

    petrol_amount, distance = pumps_copy.popleft()
    gas += petrol_amount
    if gas >= distance:
        gas -= distance
    else:
        index += 1
        gas = 0
        pumps.rotate(-1)
        pumps_copy = pumps.copy()

print(index)
