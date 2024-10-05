line = input().split(" ")
bakery = {}
for index in range(0, len(line), 2):
    bakery[line[index]] = int(line[index + 1])
print(bakery)
