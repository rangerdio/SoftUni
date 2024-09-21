n = int(input())
matrix = []
bunny_pos = []
for row in range(n):
    sublist = input().split()
    if "B" in sublist:
        bunny_pos = [row, sublist.index("B")]
    matrix.append(sublist)


left_direction = {'direction': 'left', 'coordinates': []}
right_direction = {'direction': 'right', 'coordinates': []}
up_direction = {'direction': 'up', 'coordinates': []}
down_direction = {'direction': 'down', 'coordinates': []}


current_bunny_row,  current_bunny_col = bunny_pos
while True:  # left
    direction = - 1
    next_bunny_row, next_bunny_col = current_bunny_row, current_bunny_col + direction
    if 0 <= next_bunny_col < n:
        if matrix[next_bunny_row][next_bunny_col] == 'X':
            break
        if 'sum' not in left_direction.keys():
            left_direction['sum'] = int(matrix[next_bunny_row][next_bunny_col])
        else:
            left_direction['sum'] += int(matrix[next_bunny_row][next_bunny_col])
        left_direction['coordinates'].append([next_bunny_row, next_bunny_col])
        current_bunny_row, current_bunny_col = next_bunny_row, next_bunny_col
    else:
        break

current_bunny_row,  current_bunny_col = bunny_pos
while True:  # right
    direction = 1
    next_bunny_row, next_bunny_col = current_bunny_row, current_bunny_col + direction
    if 0 <= next_bunny_col < n:
        if matrix[next_bunny_row][next_bunny_col] == 'X':
            break
        if 'sum' not in right_direction.keys():
            right_direction['sum'] = int(matrix[next_bunny_row][next_bunny_col])
        else:
            right_direction['sum'] += int(matrix[next_bunny_row][next_bunny_col])
        right_direction['coordinates'].append([next_bunny_row, next_bunny_col])
        current_bunny_row, current_bunny_col = next_bunny_row, next_bunny_col
    else:
        break

current_bunny_row,  current_bunny_col = bunny_pos
while True:  # up
    direction = - 1
    next_bunny_row, next_bunny_col = current_bunny_row + direction, current_bunny_col
    if 0 <= next_bunny_row < n:
        if matrix[next_bunny_row][next_bunny_col] == 'X':
            break
        if 'sum' not in up_direction.keys():
            up_direction['sum'] = int(matrix[next_bunny_row][next_bunny_col])
        else:
            up_direction['sum'] += int(matrix[next_bunny_row][next_bunny_col])
        up_direction['coordinates'].append([next_bunny_row, next_bunny_col])
        current_bunny_row, current_bunny_col = next_bunny_row, next_bunny_col
    else:
        break

current_bunny_row,  current_bunny_col = bunny_pos
while True:  # down
    direction = 1
    next_bunny_row, next_bunny_col = current_bunny_row + direction, current_bunny_col
    if 0 <= next_bunny_row < n:
        if matrix[next_bunny_row][next_bunny_col] == 'X':
            break
        if 'sum' not in down_direction.keys():
            down_direction['sum'] = int(matrix[next_bunny_row][next_bunny_col])
        else:
            down_direction['sum'] += int(matrix[next_bunny_row][next_bunny_col])
        down_direction['coordinates'].append([next_bunny_row, next_bunny_col])
        current_bunny_row, current_bunny_col = next_bunny_row, next_bunny_col
    else:
        break

data = [left_direction, right_direction, up_direction, down_direction]

for element in data:
    if 'sum' not in element.keys():
        data.remove(element)

max_sum = float('-inf')
max_element = 'None'

for item in data:
    sum_value = item.get('sum', None)
    if sum_value is not None and sum_value != 'none' and sum_value > max_sum:
        max_sum = sum_value
        max_element = item

direction_ = max_element['direction']
sum_ = max_element['sum']
locations = max_element['coordinates']
print(direction_)
print(*locations, sep='\n')
print(sum_)
