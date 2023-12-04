capacity = float(input())
flag = False
counter = 0
while True:
    suitcase = input()
    if suitcase == "End":
        flag = True
        break
    suitcase = float(suitcase)
    if capacity < suitcase:
        print("No more space!")
        break

    counter += 1
    if counter % 3 == 0:
        suitcase *= 1.1

    capacity -= suitcase

if flag:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {counter} suitcases loaded.")