legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_price = 250

bag = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
flag = False
flag2 = False

while True:
    line = input().lower().split()

    for i in range(1, len(line), 2):
        material = line[i]
        qty = int(line[i - 1])

        if material in legendary.keys():
            bag[material] += qty

            if bag[material] >= legendary_price:
                bag[material] -= legendary_price
                print(f'{legendary[material]} obtained!')

                flag = True
                # flag2 = True
                break

        else:
            if material not in junk.keys():
                bag[material] = qty
            else:
                bag[material] += qty
    if flag:
        break

for key in bag.keys():
    print(f'{key}: {bag[key]}')
for key in junk.keys():
    print(f'{key}: {junk[key]}')
