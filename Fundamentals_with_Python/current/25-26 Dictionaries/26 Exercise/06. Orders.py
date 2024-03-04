mark = False
materials = {"motes": 5, "fragments": 0, "shards": 260}
for element in materials.keys():
    if materials[element] >= 250:
        mark = True
        break
if mark:
    print("asd")
