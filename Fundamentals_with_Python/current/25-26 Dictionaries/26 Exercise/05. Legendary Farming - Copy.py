legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_price = 250
legendary_winner = ""

bag = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
flag = False
flag2 = False

while True:
    line = input().split()
    if not line:
        break

    for i in range(0, len(line), 2):
        qty = int(line[i])
        material = line[i + 1].lower()

        if material in legendary.keys():
            bag[material] += qty

            if bag[material] >= legendary_price:
                bag[material] -= legendary_price
                print(f'{legendary[material]} obtained!')

                flag = True
                # flag2 = True
                break
                # if flag2:
                #     break

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
