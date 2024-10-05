box = list(int(element) for element in input().split())
rack_capacity = int(input())
capacity = rack_capacity
racks = 1

while box:
    current_cloth = box.pop()
    if current_cloth <= capacity:
        capacity -= current_cloth
    else:
        racks += 1
        capacity = rack_capacity - current_cloth
print(racks)
