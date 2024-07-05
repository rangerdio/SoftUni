from collections import deque


def calculate_time(start_time_data_: list, seconds_: int):
    calc = start_time_data_[0] * 3600 + start_time_data_[1] * 60 + start_time_data_[2] + seconds_
    end_h = calc // 3600
    end_m = (calc % 3600) // 60
    end_s = (calc % 3600) % 60
    return f'[{end_h:02}:{end_m:02}:{end_s:02}]'


robots_data = input().split(";")
robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0] for robot in robots_data}
start_time_data = [int(element) for element in input().split(":")]
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)


cnt = 0
while products:
    cnt += 1
    current_time = calculate_time(start_time_data, cnt)
    current_product = products.popleft()
    free_robots = []
    print(free_robots)

    for robot_name, data in robots.items():
        if data[1] != 0:
            robots[robot_name][1] -= 1
        if data[1] == 0:
            free_robots.append([robot_name, data])

    if not free_robots:
        products.append(current_product)
        continue

    rob_name, value = free_robots[0]
    robots[rob_name][1] = value[0]

    print(f"{rob_name} - {current_product} {current_time}")
