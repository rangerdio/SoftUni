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
    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic[0] == 0:
        magic.popleft()
        continue

    # material_current = materials.pop()
    # magic_current = magic.popleft()
    # materials[-1] * magic[0] = material_current * magic_current

    if materials[-1] * magic[0] in requirements.keys():
        crafted[requirements[materials[-1] * magic[0]]] += 1

    elif materials[-1] * magic[0] < 0:
        materials[-1] += magic[0]
        magic.popleft()

    elif materials[-1] * magic[0] > 0:
        materials[-1] += 15
        magic.popleft()

    # print(f' after iteration:')
    # print(f'Materials left: {", ".join([str(x) for x in materials])}')
    # print(f'Magic left: {", ".join([str(x) for x in magic])}')

if crafted['Doll'] > 0 and crafted['Wooden train'] > 0 or crafted['Teddy bear'] > 0 and crafted['Bicycle'] > 0:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magic:
    print(f'Magic left: {", ".join([str(x) for x in magic])}')


for key, value in crafted.items():
    if value > 0:
        print(f'{key}: {value}')