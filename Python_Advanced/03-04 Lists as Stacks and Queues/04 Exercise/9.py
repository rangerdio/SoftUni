from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(list(map(int, input().split())))
locks = deque(list(map(int, input().split())))
intelligence = int(input())

money_spend = 0
bullet_counter = 0

while bullets and locks:
    current_bullet = bullets.pop()
    bullet_counter += 1
    money_spend += bullet_price

    current_lock = locks.copy().popleft()

    if current_lock >= current_bullet:
        locks.remove(current_lock)
        print("Bang!")
    else:
        print("Ping!")

    if bullets and bullet_counter == barrel_size:
        bullet_counter = 0
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - money_spend}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
