start_index = 2
end_index = 4
pirate_ship = [1, 2, 3, 4, 5]
valid = len(pirate_ship) - 1
valid_list = []
for i in range(len(pirate_ship)):
    valid_list.append(i)


print(valid_list)

if start_index in valid_list and end_index in valid_list:
    print("kokokokok")


