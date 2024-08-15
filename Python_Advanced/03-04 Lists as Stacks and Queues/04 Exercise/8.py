# # not working
#
#
# from collections import deque
# green_time = int(input())
# free_window = int(input())
# cars = deque()
#
# while True:
#     car = input()
#     if car == "END":
#         break
#     cars.append(car)
#
# time = 0
# ext_time = 0
# total_cars = 0
# current_queue = deque()
# while cars:
#     is_crash = False
#     current_car = cars.popleft()
#
#     if current_car == "green":
#         time = green_time
#
#         while current_queue:
#             time -= 1
#             current_model = current_queue.popleft()
#             if len(current_model) < time:
#                 time -= len(current_model)
#                 continue
#             elif len(current_model) == time:
#                 time -= len(current_model)
#                 break
#             else:
#                 time += ext_time
#                 current_char = ""
#                 for i in range(time, 0, -1):
#                     current_char = current_model[0]
#                     current_model = current_model[1:]
#                 print('A crash happened!')
#                 print(f'{current_car} was hit at {current_char}.')
#                 is_crash = True
#                 break
#     if is_crash:
#         break
#     current_queue.append(current_car)
#     total_cars += 1
#
# if not cars:
#     print(f'Everyone is safe.')
#     print(f'{total_cars} total cars passed the crossroads.')


from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

car_lane = deque()
while True:
    car = input()
    if car == "END":
        break
    car_lane.append(car)

# print(car_lane)

cars = deque()
current_queue = deque()
while car_lane:
    current_car = car_lane.popleft()
    current_queue.append(current_car)

    if current_car == "green":
        cars.append(current_queue)
        current_queue = deque()
        continue

    if not car_lane:
        cars.append(current_queue)

print(cars)

while cars:
    current_loop = cars.popleft()

    light_queue = deque()
    while current_loop:

        current_car = cars.popleft()

        if current_car == "green":

            green_counter = 0
            while light_queue:
                car = light_queue.popleft()
                while car:
                    green_counter += 1

                    if green_counter < green_light_duration:
                        symbol = car.popleft()
                    else:
                        pass

        else:
            light_queue.append(current_car)
