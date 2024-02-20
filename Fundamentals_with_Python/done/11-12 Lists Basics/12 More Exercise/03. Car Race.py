my_list = input().split()
finish_line = len(my_list) // 2

car_1_list = my_list.copy()[:finish_line]
car_2_list = my_list.copy()[finish_line - 1:]
car_2_list = car_2_list[::-1]
winner = ""
winner_time = 0

car_1_time = 0
car_2_time = 0
for step in range(finish_line):
    step_value_1 = int(car_1_list[step])
    step_value_2 = int(car_2_list[step])

    if step_value_1 == 0:
        car_1_time *= 0.8
    else:
        car_1_time += step_value_1
    winner = "left"
    winner_time = car_1_time
    if step_value_2 == 0:
        car_2_time *= 0.8
    else:
        car_2_time += step_value_2
    if car_2_time < car_1_time:
        winner = "right"
        winner_time = car_2_time
print(f"The winner is {winner} with total time: {winner_time:.1f}")
