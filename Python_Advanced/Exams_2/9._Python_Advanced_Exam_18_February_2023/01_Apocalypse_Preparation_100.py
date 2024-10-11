from collections import deque

textlines = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100
}
items_created = {}
med_kit = items['MedKit']

while textlines and medicaments:
    current_textline = textlines.popleft()
    current_medi = medicaments.pop()
    result = current_textline + current_medi
    if result in items.values():
        key = ""
        for item, value in items.items():
            if value == result:
                key = item
                break
        if key not in items_created:
            items_created[key] = 0
        items_created[key] += 1
    elif result > med_kit:
        if 'MedKit' not in items_created:
            items_created['MedKit'] = 0
        items_created['MedKit'] += 1
        medicaments[-1] += result - med_kit
    else:
        current_medi += 10
        medicaments.append(current_medi)

if not textlines and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textlines:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')

items_created_sorted = sorted(items_created.items(), key=lambda x: (-x[1], x[0]))
for item, value in items_created_sorted:
    print(f'{item} - {value}')

if medicaments:
    print(f'Medicaments left: {", ".join(str(x) for x in medicaments[::-1])}')
if textlines:
    print(f'Textiles left: {", ".join(str(x) for x in textlines)}')
