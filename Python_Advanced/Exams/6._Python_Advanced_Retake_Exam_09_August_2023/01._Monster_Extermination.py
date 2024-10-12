from collections import deque
monsters = deque([int(x) for x in input().split(',')])
attacks = [int(x) for x in input().split(',')]
killed_monsters = 0

while monsters and attacks:
    monster = monsters.popleft()
    attack = attacks.pop()

    if attack >= monster:
        killed_monsters += 1
        attack -= monster
        if attack == 0:
            continue
        else:
            if len(attacks) > 0:
                attacks[-1] += attack
            else:
                attacks.append(attack)
    else:
        monsters.append(monster - attack)
if not monsters:
    print('All monsters have been killed!')
if not attacks:
    print('The soldier has been defeated.')
print(f'Total monsters killed: {killed_monsters}')
