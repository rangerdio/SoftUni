keys = [int(key) for key in input().split()]
# print(keys)
messages = []
while True:
    command = input()
    if command == "find":
        break
    line_list = [letter for letter in command]
    # print(line_list)
    if len(keys) < len(line_list):
        multiplier = int(len(line_list) / len(keys)) + 1
        keys *= multiplier
        # print(keys)

    for index in range(len(line_list)):
        line_list[index] = chr(ord(line_list[index]) - keys[index])
    messages.append("".join(line_list))
# print(messages)
for message in messages:
    treasure_indexes, location_indexes = [], []
    message_list = message.split("&")
    treasure = message_list[1]

    location_indexes.append(message.index("<"))
    location_indexes.append(message.index(">"))
    print(f"Found {treasure} at {message[location_indexes[0] + 1: location_indexes[1]]}")
