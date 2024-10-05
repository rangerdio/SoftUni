number_goods = int(input())
mbus_var = 0
bus_var = 0
train_var = 0
mbus = 0
bus = 0
train = 0
total_weight = 0
for number in range(1, number_goods + 1):
    good_weight = int(input())
    if good_weight <= 3:
        mbus += good_weight * 200
        mbus_var += good_weight
    elif 4 <= good_weight <= 11:
        bus += good_weight * 175
        bus_var += good_weight
    elif good_weight >= 12:
        train += good_weight * 120
        train_var += good_weight
total_amount = mbus + bus + train
total_weight = mbus_var + bus_var + train_var
mbus_var = 100 * mbus_var / total_weight
bus_var = 100 * bus_var / total_weight
train_var = 100 * train_var / total_weight
print(f"{(total_amount/total_weight):.2f}")
print(f"{mbus_var:.2f}%")
print(f"{bus_var:.2f}%")
print(f"{train_var:.2f}%")
