from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(";")
robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0] for robot in robots_data}
time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    time += timedelta(0, 1)
    current_product = products.popleft()

    free_robots = []

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

    print(f"{rob_name} - {current_product} [{time.strftime('%H:%M:%S')}]")
