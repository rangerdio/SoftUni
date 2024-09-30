






from collections import deque
eat_capacity = deque([int(x) for x in input().split()])
pie_pieces = [int(x) for x in input().split()]

while eat_capacity and pie_pieces:

    if eat_capacity[0] >= pie_pieces[-1]:
        eat_capacity[0] -= pie_pieces[-1]
        pie_pieces.pop()
        if eat_capacity[0] == 0:
            eat_capacity.popleft()
        else:
            eat_capacity.append(eat_capacity.popleft())
    else:
        pie_pieces[-1] -= eat_capacity[0]
        if pie_pieces[-1] == 1 and len(pie_pieces) > 1:
            to_remove = pie_pieces.pop()
            pie_pieces[-1] += to_remove
        eat_capacity.popleft()

if not pie_pieces and eat_capacity:
    print('We will have to wait for more pies to be baked!')
    print('Contestants left:', ', '.join(str(x) for x in eat_capacity))
elif not pie_pieces and not eat_capacity:
    print('We have a champion!')
else:
    print('Our contestants need to rest!')
    print('Pies left:',', '.join(str(x) for x in pie_pieces))
