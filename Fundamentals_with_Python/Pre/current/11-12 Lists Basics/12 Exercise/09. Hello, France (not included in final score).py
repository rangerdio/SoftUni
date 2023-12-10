items_list = input().split("|")
sold_items_list = []
budged = float(input())
new_budged = 0
TICKET = 150
profit = 0

for element_index in range(len(items_list)):
    element = items_list[element_index].split("->")

    if element[0] == "Clothes" and float(element[1]) <= 50.00:
        if budged >= float(element[1]):
            budged -= float(element[1])
            sold_items_list.append(float(element[1]) * 1.4)
            new_budged += float(element[1]) * 1.4
            profit += (float(element[1]) * 1.4 - float(element[1]))
    elif element[0] == "Shoes" and float(element[1]) <= 35.00:
        if budged >= float(element[1]):
            budged -= float(element[1])
            sold_items_list.append(float(element[1]) * 1.4)
            new_budged += float(element[1]) * 1.4
            profit += (float(element[1]) * 1.4 - float(element[1]))
    elif element[0] == "Accessories" and float(element[1]) <= 20.50:
        if budged >= float(element[1]):
            budged -= float(element[1])
            sold_items_list.append(float(element[1]) * 1.4)
            new_budged += float(element[1]) * 1.4
            profit += (float(element[1]) * 1.4 - float(element[1]))

for index in range(len(sold_items_list)):
    print(f"{float(sold_items_list[index]):.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budged + new_budged >= TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
a