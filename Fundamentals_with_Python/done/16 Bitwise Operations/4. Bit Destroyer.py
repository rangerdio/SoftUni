number = int(input())
target_position = int(input())


mask = 1 << target_position
mask = ~mask
result = mask & number
print(result)




