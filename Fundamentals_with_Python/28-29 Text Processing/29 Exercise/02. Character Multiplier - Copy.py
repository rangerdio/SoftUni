strings = input().split(" ")
if len(strings[1]) < len(strings[0]):
    strings[0], strings[1] = strings[1], strings[0]     # shorter is first
slice_start_index = len(strings[0])
remaining_letters = strings[1][slice_start_index::]

total = 0
for index in range(len(strings[0])):
    total += ord(strings[0][index]) * ord(strings[1][index])

for index in range(len(remaining_letters)):
    total += ord(remaining_letters[index])
print(total)
