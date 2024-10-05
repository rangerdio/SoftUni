start = int(input())
end = int(input())
magic = int(input())
counter = 0
flag1 = False
for first in range(start, end + 1):
    for second in range(start, end + 1):
        counter += 1
        if magic == first + second:
            first_combination = counter
            flag1 = True
            print(f"Combination N:{first_combination} ({first} + {second} = {magic})")
            break
    if flag1:
        break
if not flag1:
    print(f"{counter} combinations - neither equals {magic}")
