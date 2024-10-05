w = float(input())
h = float(input())

w = w * 100
h = h * 100
coridor = 100
columns = (h - coridor) // 70
rows = w // 120
seats = columns * rows - 3
print(int(seats))
