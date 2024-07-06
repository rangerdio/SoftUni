from collections import deque
green = int(input())
free_window = int(input())
cars = deque()

while True:
    car = input()
    if car == "END":
        break
    cars.append(car)

time = 0
while cars:
    current_queue = deque()
    current_car = cars.popleft()

    if current_car == "green":
        pass

    current_queue.append(current_car)

