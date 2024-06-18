bag = {}
command_list = []
while True:
    line = input()
    if line == "stop":
        break
    command_list.append(line)

for i in range(0, len(command_list), 2):
    if command_list[i] not in bag.keys():
        bag[command_list[i]] = int(command_list[i + 1])
    else:
        bag[command_list[i]] += int(command_list[i + 1])
for resource, quantity in bag.items():
    print(f"{resource} -> {quantity}")
