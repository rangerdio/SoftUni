def get_materials(materials_, legendary_, current_material_, current_value_):
    materials_[current_material_] += current_value_
    # mark_ = False
    # while materials_[current_material_] >= 250:
    #     materials_[current_material_] -= 250
    #     mark_ = True
    # if mark_:
    if materials_[current_material_] >= 250:
        materials_[current_material_] -= 250
        print(f"{legendary_[current_material_]} obtained!")
        return [materials_, True]
    return [materials_, False]


def get_junk(junks_, current_material_, current_value_):
    if current_material_ not in junks_.keys():
        junks_[current_material_] = current_value_
    else:
        junks_[current_material_] += current_value_
    return junks_


materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary = {"motes": "Dragonwrath", "fragments": "Valanyr", "shards": "Shadowmourne"}
junks = {}

mark = False
while True:

    materials_list = input().lower().split()

    for index in range(1, len(materials_list), 2):
        current_material = materials_list[index]
        current_value = int(materials_list[index - 1])

        if current_material == "motes" or current_material == "fragments" or current_material == "shards":
            gathered_materials_result = get_materials(materials, legendary, current_material, current_value)
            materials = gathered_materials_result[0]
            if gathered_materials_result[1]:
                mark = True
                break

        else:   # its junk
            update_junks = get_junk(junks, current_material, current_value)
            junks = update_junks
    if mark:
        break

for element in materials.keys():
    print(f"{element}: {materials[element]}")
for element in junks.keys():
    print(f"{element}: {junks[element]}")