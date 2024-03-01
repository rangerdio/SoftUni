foods_list = input().split()
bakery = {}

for i in range(0, len(foods_list), 2):
    bakery[foods_list[i]] = int(foods_list[i+1])

print(bakery)

