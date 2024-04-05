legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_price = 250

bag = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
flag = False
flag2 = False

while True:
    line = input().lower().split()

    for i in range(1, len(line), 2):
        current_material = line[i]
        qty = int(line[i - 1])

        if current_material in legendary.keys():
            bag[current_material] += qty

            if bag[current_material] >= legendary_price:
                bag[current_material] -= legendary_price
                print(f'{legendary[current_material]} obtained!')

                flag = True
                # flag2 = True
                break

        else:
            if current_material not in junk.keys():
                bag[current_material] = qty
            else:
                bag[current_material] += qty
    if flag:
        break

for key in bag.keys():
    print(f'{key}: {bag[key]}')
for key in junk.keys():
    print(f'{key}: {junk[key]}')
