# from collections import deque
# if_break = False
# no_more_cars = True
# cnt = 0
# # green_light = int(input())
# # free_window = int(input())
# # car_lane = deque()
# # while True:
# #     car = input()
# #     if car == "END":
# #         break
# #     car_lane.append(car)
#
# green_light = 10
# free_window = 5
# car_lane = deque(['Mercedes', 'green', 'Mercedes', 'BMW', 'Skoda', 'green'])
# current_lane = deque([])
# for i in range(len(car_lane)):
#     if car_lane[0] != 'green':
#         current_lane.append(car_lane.popleft())
#         print(current_lane)
#     else:
#         car_lane.popleft()
#         green_free = deque([])
#
#         for j in range(green_light + free_window):
#             green_free.append(j)
#
#
#
#
#         while current_lane and green_free:
#             current_car = deque([x for x in current_lane.popleft()])
#             current_car_var = current_car
#
#             if len(current_lane) == 0:
#                 no_more_cars = True
#
#             while current_car:
#
#                 # print(current_car.popleft())
#                 current_letter = current_car.popleft()
#                 current_index = green_free.popleft()
#                 cnt += 1
#                 if cnt == green_light and no_more_cars:
#                     if not current_car:
#                         print('A crash happened!')
#                         print(f'{current_car_var} was hit at {current_car_var[current_index]}.')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # # not working
# # #
# # #
# # # from collections import deque
# # # green_time = int(input())
# # # free_window = int(input())
# # # cars = deque()
# # #
# # # while True:
# # #     car = input()
# # #     if car == "END":
# # #         break
# # #     cars.append(car)
# # #
# # # time = 0
# # # ext_time = 0
# # # total_cars = 0
# # # current_queue = deque()
# # # while cars:
# # #     is_crash = False
# # #     current_car = cars.popleft()
# # #
# # #     if current_car == "green":
# # #         time = green_time
# # #
# # #         while current_queue:
# # #             time -= 1
# # #             current_model = current_queue.popleft()
# # #             if len(current_model) < time:
# # #                 time -= len(current_model)
# # #                 continue
# # #             elif len(current_model) == time:
# # #                 time -= len(current_model)
# # #                 break
# # #             else:
# # #                 time += ext_time
# # #                 current_char = ""
# # #                 for i in range(time, 0, -1):
# # #                     current_char = current_model[0]
# # #                     current_model = current_model[1:]
# # #                 print('A crash happened!')
# # #                 print(f'{current_car} was hit at {current_char}.')
# # #                 is_crash = True
# # #                 break
# # #     if is_crash:
# # #         break
# # #     current_queue.append(current_car)
# # #     total_cars += 1
# # #
# # # if not cars:
# # #     print(f'Everyone is safe.')
# # #     print(f'{total_cars} total cars passed the crossroads.')
# #
# #
# # from collections import deque
# #
# # green_light_duration = int(input())
# # free_window_duration = int(input())
# #
# # car_lane = deque()
# # while True:
# #     car = input()
# #     if car == "END":
# #         break
# #     car_lane.append(car)
# #
# # # print(car_lane)
# #
# # cars = deque()
# # current_queue = deque()
# # while car_lane:
# #     current_car = car_lane.popleft()
# #     current_queue.append(current_car)
# #
# #     if current_car == "green":
# #         cars.append(current_queue)
# #         current_queue = deque()
# #         continue
# #
# #     if not car_lane:
# #         cars.append(current_queue)
# #
# # print(cars)
# #
# # while cars:
# #     current_loop = cars.popleft()
# #
# #     light_queue = deque()
# #     while current_loop:
# #
# #         current_car = cars.popleft()
# #
# #         if current_car == "green":
# #
# #             green_counter = 0
# #             while light_queue:
# #                 car = light_queue.popleft()
# #                 while car:
# #                     green_counter += 1
# #
# #                     if green_counter < green_light_duration:
# #                         symbol = car.popleft()
# #                     else:
# #                         pass
# #
# #         else:
# #             light_queue.append(current_car)
