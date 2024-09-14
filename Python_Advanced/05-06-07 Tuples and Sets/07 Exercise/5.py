from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

requirements = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted = {
    'Bicycle': 0,
    'Doll': 0,
    'Teddy bear': 0,
    'Wooden train': 0,
}

while materials and magic:
    material_current = materials.pop()
    magic_current = magic.popleft()
    total_magic = material_current * magic_current

    if total_magic in requirements.keys():
        crafted[requirements[total_magic]] += 1

    elif total_magic < 0:
        materials.append(material_current + magic_current)

    elif total_magic > 0:
        materials.append(material_current + 15)

    elif material_current == 0 and magic_current == 0:
        pass
    elif material_current == 0:
        magic.insert(0, magic_current)

    elif magic_current == 0:
        materials.append(material_current)

if crafted['Doll'] > 0 and crafted['Wooden train'] > 0 or crafted['Teddy bear'] > 0 and crafted['Bicycle'] > 0:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magic:
    print(f'Magic left: {", ".join([str(x) for x in magic])}')

for key, value in crafted.items():
    if value > 0:
        print(f'{key}: {value}')
