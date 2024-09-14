from collections import deque

materials = [int(x) for x in input().split()]
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

    if materials[-1] * magic[0] in requirements.keys():
        crafted[requirements[materials[-1] * magic[0]]] += 1
        materials.pop()
        magic.popleft()

    elif materials[-1] * magic[0] < 0:
        materials[-1] += magic[0]
        ss = materials.pop()
        materials.append(ss)
        magic.popleft()

    elif materials[-1] * magic[0] > 0:
        materials[-1] += 15
        magic.popleft()

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
