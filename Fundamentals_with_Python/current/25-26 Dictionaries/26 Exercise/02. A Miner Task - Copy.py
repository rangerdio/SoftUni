bag = {}
command_list = []
while True:
    line = input()
    if line == "stop":
        break
    if line.isnumeric():
        line = int(line)
    command_list.append(line)
# print(command_list)

for i in range(0, len(command_list), 2):
    if command_list[i] not in bag.keys():
        bag[command_list[i]] = command_list[i + 1]
    else:
        bag[command_list[i]] += command_list[i + 1]
for resource, quantity in bag.items():
    print(f"{resource} -> {quantity}")
