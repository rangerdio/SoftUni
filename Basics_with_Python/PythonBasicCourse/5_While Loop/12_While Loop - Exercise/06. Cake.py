wide = int(input())
length = int(input())
total_peaces = wide * length
taken_peaces = 0

while taken_peaces != "STOP":
    taken_peaces = int(taken_peaces)
    total_peaces -= taken_peaces
    if total_peaces <= 0:
        break
    else:
        taken_peaces = input()

if taken_peaces == "STOP" and total_peaces >= 0:
    print(f"{total_peaces} pieces are left.")
elif total_peaces < 0:
    print(f"No more cake left! You need {abs(total_peaces)} pieces more.")

# wide = int(input())
# length = int(input())
# total_peaces = wide * length
# taken_peaces = 0
#
# while total_peaces > 0:
#     if taken_peaces == "STOP":
#         break
#     else:
#         taken_peaces = int(taken_peaces)
#         total_peaces -= taken_peaces
#         if total_peaces <= 0:
#             break
#         taken_peaces = input()
#
#
# if taken_peaces == "STOP" and total_peaces >= 0:
#     print(f"{total_peaces} pieces are left.")
# elif total_peaces < 0:
#     print(f"No more cake left! You need {abs(total_peaces)} pieces more.")
