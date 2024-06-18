def calculate_time(efficiency_, total_students_):
    time = 0
    for hour in range(1, total_students_):
        if hour % 4 == 0:
            continue
        total_students_ -= efficiency_per_hour
        if total_students_ <= 0:
            time = hour
            break
    return f"Time needed: {time}h."


efficiency = [int(input()), int(input()), int(input())]
total_students = int(input())
efficiency_per_hour = 0
for element in efficiency:
    efficiency_per_hour += element

print(calculate_time(efficiency, total_students))

# efficiency = [int(input()), int(input()), int(input())]
# total_students = int(input())
# efficiency_per_hour = 0
# time = 0
# for element in efficiency:
#     efficiency_per_hour += element
#
# for hour in range(1, total_students):
#     if hour % 4 == 0:
#         continue
#     total_students -= efficiency_per_hour
#     if total_students <= 0:
#         time = hour
#         break
#
# print(f"Time needed: {time}h.")
