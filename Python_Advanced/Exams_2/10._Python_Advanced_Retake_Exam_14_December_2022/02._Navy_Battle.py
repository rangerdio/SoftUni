size = int(input())
field, row, col = [], None, None

for r in range(size):
    line = list(input())
    if 'S' in line:
        row, col = r, line.index('S')
    field.append(line)

