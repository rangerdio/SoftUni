from collections import deque
packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])
total_weight = 0

while packages and couriers:
    current_package = packages.pop()
    current_courier = couriers.popleft()

    if current_courier < current_package:
        current_package -= current_courier
        packages.append(current_package)
    else:
        if current_courier > current_package:
            current_courier -= 2 * current_package
            if current_courier > 0:
                couriers.append(current_courier)
    total_weight += current_package

print(f'Total weight: {total_weight} kg')
if not packages and not couriers:
    print('Congratulations, all packages were delivered successfully by the couriers today.')
elif not couriers:
    print(f'Unfortunately, there are no more available couriers to deliver the following packages: '
          f'{", ".join(str(x) for x in packages)}')
else:
    print(f'Couriers are still on duty: '
          f'{", ".join(str(x) for x in couriers)} but there are no more packages to deliver.')
