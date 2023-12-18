numbers = map(float, input().split())
new_list = []
for num in numbers:
    new_list.append(abs(num))
print(new_list)
