wide = int(input())
length = int(input())
height = int(input())
available_volume = wide * length * height
moved = input()

while True:
    if moved != "Done":
        moved = int(moved)
        available_volume -= moved
        if available_volume <= 0:
            break
        moved = input()
    elif moved == "Done":
        break

if moved == "Done":
    print(f"{available_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(available_volume)} Cubic meters more.")


# wide = int(input())
# length = int(input())
# height = int(input())
# available_volume = wide * length * height
# moved = input()
#
# while moved != "Done":
#     moved = int(moved)
#     available_volume -= moved
#     if available_volume <= 0:
#         break
#     moved = input()
#
# if moved == "Done":
#     print(f"{available_volume} Cubic meters left.")
# else:
#     print(f"No more free space! You need {abs(available_volume)} Cubic meters more.")


# wide = int(input())
# length = int(input())
# height = int(input())
# moved = 0
# available_volume = wide * length * height
# while available_volume > 0:
#     if moved == "Done":
#         break
#     else:
#         moved = int(moved)
#         available_volume -= moved
#         if available_volume <= 0:
#             break
#         moved = input()
# if moved == "Done":
#     print(f"{available_volume} Cubic meters left.")
# else:
#     print(f"No more free space! You need {abs(available_volume)} Cubic meters more.")
