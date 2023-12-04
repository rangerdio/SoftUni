deter_volume = 750
counter = 0
pot_count = 0
plate_count = 0

deter = int(input())
deter_available = deter_volume * deter
dishes = input()
while dishes != "End":
    counter += 1
    dishes = int(dishes)
    if counter % 3 != 0:
        plate_count += dishes
        deter_available -= (dishes * 5)
        # print(f"Error check:  count= {counter} , plates= {dishes} , {dishes}*5= {dishes * 5} , d.left= {deter_available + dishes * 5}-{dishes * 5} {deter_available}")
        if deter_available < 0:
            break
        dishes = input()

    elif counter % 3 == 0:
        pot_count += dishes
        deter_available -= (dishes * 15)
        # print(f"Error check:  count= {counter} , pots= {dishes} , {dishes}*15= {dishes * 15} , d.left= {deter_available + dishes * 15}-{dishes * 15} {deter_available}")
        if deter_available < 0:
            break
        dishes = input()

if deter_available < 0:
    print(f"Not enough detergent, {abs(deter_available)} ml. more necessary!")

elif dishes == "End" or deter_available == 0:
    print(f"Detergent was enough!")
    print(f"{plate_count} dishes and {pot_count} pots were washed.")
    print(f"Leftover detergent {deter_available} ml.")
# # else:
# #    print("Check else error test")


# ////third attempt/////
# deter_volume = 750
# counter = 0
# pot_count = 0
# plate_count = 0
#
# deter = int(input())
# deter_available = deter_volume * deter
#
# while True:
#     dishes = input()
#     counter += 1
#     if dishes == "End":
#         break
#     dishes = int(dishes)
#     if counter % 3 != 0:
#         plate_count += dishes
#         deter_available -= (dishes * 5)
#         # print(f"Error check:  count= {counter} , plates= {dishes} , {dishes}*5= {dishes * 5} , d.left= {deter_available + dishes * 5}-{dishes * 5} {deter_available}")
#         if deter_available < 0:
#             break
#
#     elif counter % 3 == 0:
#         pot_count += dishes
#         deter_available -= (dishes * 15)
#         # print(f"Error check:  count= {counter} , pots= {dishes} , {dishes}*15= {dishes * 15} , d.left= {deter_available + dishes * 15}-{dishes * 15} {deter_available}")
#         if deter_available < 0:
#             break
#
# if deter_available < 0:
#     print(f"Not enough detergent, {abs(deter_available)} ml. more necessary!")
#
# elif dishes == "End" or deter_available == 0:
#     print(f"Detergent was enough!")
#     print(f"{plate_count} dishes and {pot_count} pots were washed.")
#     print(f"Leftover detergent {deter_available} ml.")
# else:
# #    print("Check else error test")


# # ////second attempt/////
# deter_volume = 750
# counter = 0
# pot_count = 0
# plate_count = 0
#
# deter = int(input())
# deter_available = deter_volume * deter
# dishes = input()
# while True:
#     counter += 1
#     if dishes == "End":
#         break
#     dishes = int(dishes)
#     if counter % 3 != 0:
#         plate_count += dishes
#         deter_available -= (dishes * 5)
#         # print(f"Error check:  count= {counter} , plates= {dishes} , {dishes}*5= {dishes * 5} , d.left= {deter_available + dishes * 5}-{dishes * 5} {deter_available}")
#         if deter_available < 0:
#             break
#         dishes = input()
#
#     elif counter % 3 == 0:
#         pot_count += dishes
#         deter_available -= (dishes * 15)
#         # print(f"Error check:  count= {counter} , pots= {dishes} , {dishes}*15= {dishes * 15} , d.left= {deter_available + dishes * 15}-{dishes * 15} {deter_available}")
#         if deter_available < 0:
#             break
#         dishes = input()
#
# if deter_available < 0:
#     print(f"Not enough detergent, {abs(deter_available)} ml. more necessary!")
#
# elif dishes == "End" or deter_available == 0:
#     print(f"Detergent was enough!")
#     print(f"{plate_count} dishes and {pot_count} pots were washed.")
#     print(f"Leftover detergent {deter_available} ml.")
# # else:
# #    print("Check else error test")
