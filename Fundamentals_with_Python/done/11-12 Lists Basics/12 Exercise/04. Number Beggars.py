money_string = input()
money_list = money_string.split(", ")
money_list_int = [int(current_money) for current_money in money_list]
beggars_qty = int(input())

beggars_money = []
for start_index in range(beggars_qty):
    current_beggar = 0
    for money_slice_index in range(start_index, len(money_list_int), beggars_qty):
        current_beggar += money_list_int[money_slice_index]
    beggars_money.append(current_beggar)
    start_index += 1
print(beggars_money)
