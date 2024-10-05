from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])
total_weight = 0

while packages and couriers:
    # current_package = packages.pop()
    # current_courier = couriers.popleft()
    if couriers[0] >= packages[-1]:    # delivery occur
        if couriers[0] > packages[-1]:
            couriers[0] -= packages[-1] * 2
            if couriers[0] > 0:
                couriers.append(couriers.popleft())
            else:
                couriers.popleft()
        elif couriers[0] == packages[-1]:
            couriers.popleft()
        total_weight += packages.pop()

    else:
        delivered_portion = couriers.popleft()
        packages[-1] -= delivered_portion
        total_weight += delivered_portion

print(f'Total weight: {total_weight} kg')

if not packages:
    if not couriers:
        print('Congratulations, all packages were delivered successfully by the couriers today.')
    else:
        print('Couriers are still on duty: ', end='')
        print(', '.join(str(x) for x in couriers))
else:
    print('Unfortunately, there are no more available couriers to deliver the following packages: ', end='')
    print(', '.join(str(x) for x in packages))
