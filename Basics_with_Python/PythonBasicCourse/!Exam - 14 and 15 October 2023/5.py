start_height = 5364
target = 8848
day = 1
current_height = start_height
flag1 = False
flag2 = False

while True:
    #day += 1
    if day > 5:
        flag2 = True
        break

    command = input()
    if current_height < target and day > 5:
        #flag2 = True
        break
    if command == "END":
        break
    if command == "No":
        climbed_meters = float(input())
        current_height += climbed_meters
        current_height = int(current_height)
        if current_height >= target:
            flag1 = True
            break
    elif command == "Yes":
        day += 1
        climbed_meters = float(input())
        current_height += climbed_meters
        current_height = int(current_height)
        if current_height >= target:
            flag1 = True
            break

if current_height >= target and day < 6:
    print(f"Goal reached for {day} days!")
elif current_height < target or day > 5:
    print(f"Failed!")
    print(f"{current_height}")



# command_rest = input()
# while command_rest != "END":
#     climbed_meters = float(input())
#     current_height += climbed_meters
#     if current_height >= target:
#         flag1 = True
#         break
#     elif current_height < target and day > 5:
#         flag2 = True
#         break
#     if command_rest == "Yes":
#         day += 1
#     elif command_rest == "No":
#         command_rest = input()
# if flag1:
#     print(f"Goal reached for {day} days!")
# elif flag2:
#     print(f"Failed!")
#     print(f"{current_height}")
# if current_height >= target and day < 6:
#     print(f"Goal reached for {day} days!")
# elif current_height < target or day > 5:
#     print(f"Failed!")
#     print(f"{current_height}")
#
