# fire_data_string = "High = 89#Low = 28#Medium = 77#Low = 23"
fire_data_list = input().split("#")
water = int(input())
effort = 0
cells_out = []
fire = 0

count = 0
for element in range(len(fire_data_list)):
    current_element_list = fire_data_list[element].split(" = ")

    is_valid = False
    if current_element_list[0] == "High":
        if 81 <= int(current_element_list[1]) <= 125:
            is_valid = True
    elif current_element_list[0] == "Medium":
        if 51 <= int(current_element_list[1]) <= 80:
            is_valid = True
    elif current_element_list[0] == "Low":
        if 1 <= int(current_element_list[1]) <= 50:
            is_valid = True

    if is_valid and water >= int(current_element_list[1]):
        water -= int(current_element_list[1])
        cells_out.append(current_element_list[1])
        effort += int(current_element_list[1]) / 4

for index in range(len(cells_out)):
    fire += int(cells_out[index])

for index in range(len(cells_out)):
    cells_out[index] = " - " + cells_out[index]

cells_out.insert(0, "Cells:")
for index in range(len(cells_out)):
    print(cells_out[index])
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")
