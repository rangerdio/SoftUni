coins = float(input())
coins = int(coins * 100)
coins_counter = 0
coins_counter += coins // 200
coins %= 200
coins_counter += coins // 100
coins %= 100
coins_counter += coins // 50
coins %= 50
coins_counter += coins // 20
coins %= 20
coins_counter += coins // 10
coins %= 10
coins_counter += coins // 5
coins %= 5
coins_counter += coins // 2
coins %= 2
coins_counter += coins // 1
print(coins_counter)


# ### 19 rows ###
# coins = float(input())
# coins = int(coins * 100)
# two_lv = int(coins // 200)
# one_lv_ost = coins % 200
# one_lv = int(one_lv_ost // 100)
# fifty_ost = one_lv_ost % 100
# fifty = int(fifty_ost // 50)
# twenty_ost = fifty_ost % 50
# twenty = int(twenty_ost // 20)
# ten_ost = twenty_ost % 20
# ten = int(ten_ost // 10)
# five_ost = ten_ost % 10
# five = int(five_ost // 5)
# two_ost = five_ost % 5
# two = int(two_ost // 2)
# one_ost = two_ost % 2
# one = int(one_ost // 1)
# coins_counter = one + two + five + ten + twenty + fifty + one_lv + two_lv
# print(coins_counter)


# #### 29 rows ####
# coins = float(input())
# coins = int(coins * 100)
# coins_counter = 0
# while coins > 0:
#     if coins - 200 >= 0:
#         coins_counter += 1
#         coins -= 200
#     elif coins - 100 >= 0:
#         coins_counter += 1
#         coins -= 100
#     elif coins - 50 >= 0:
#         coins_counter += 1
#         coins -= 50
#     elif coins - 20 >= 0:
#         coins_counter += 1
#         coins -= 20
#     elif coins - 10 >= 0:
#         coins_counter += 1
#         coins -= 10
#     elif coins - 5 >= 0:
#         coins_counter += 1
#         coins -= 5
#     elif coins - 2 >= 0:
#         coins_counter += 1
#         coins -= 2
#     elif coins - 1 >= 0:
#         coins_counter += 1
#         coins -= 200
# print(coins_counter)
