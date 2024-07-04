from collections import deque


def calculate_time(start_time_data_: list, seconds_: int):
    calc = start_time_data_[0] * 3600 + start_time_data_[1] * 60 + start_time_data_[2] + seconds_
    end_h = calc // 3600
    end_m = (calc % 3600) // 60
    end_s = (calc % 3600) % 60
    return f'{end_h:02}:{end_m:02}:{end_s:02}'


robots = {robot.split("-")[0]: int(robot.split("-")[1]) for robot in input().split(";")}


print(robots)
start_time_data = [int(element) for element in input().split(":")]
print(calculate_time(start_time_data, 3603))


# cnt = 0
# while True:
#     cnt += 1
#     product = input()
#     if product == "End":
#         break
#     data = rob.copy().popleft()
#     if data[1]






