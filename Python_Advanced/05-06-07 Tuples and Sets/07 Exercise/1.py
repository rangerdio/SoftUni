from collections import deque

data1_set = set([int(x) for x in input().split()])
data2_set = set([int(x) for x in input().split()])
data1 = list(data1_set)
data2 = list(data2_set)
data22_set = data2_set
data11_set = data1_set

n = int(input())


for _ in range(n):

    command = deque(x for x in input().split())
    outside_command = command.popleft()
    inside_command = command.popleft()
    # print(outside_command, inside_command, command)

    if outside_command == 'Check':
        # data1_set = set(data1)
        # data2_set = set(data2)
        print(True) if data11_set.issubset(data22_set) or data22_set.issubset(data11_set) else print(False)

    elif outside_command == 'Add':
        # print('Adding')
        # print(command)

        if inside_command == 'First':
            # print('First')

            while command:
                to_add = int(command.popleft())
                data1_set.add(to_add)
                # print(f'adding {to_add}')

        elif inside_command == 'Second':
            # print('Second')

            while command:
                to_add = int(command.popleft())
                data2_set.add(to_add)
                # print(f'adding {to_add}')

        # print(data1)
        # print(data2)

    elif outside_command == 'Remove':
        # print('Removing')

        if inside_command == 'First':
            # print('First')
            for number in command:
                if int(number) in data1_set:
                    data1_set.remove(int(number))

        elif inside_command == 'Second':
           # print('Second')
            for number in command:
                if int(number) in data2_set:
                    data2_set.remove(int(number))

        # print(data1)
        # print(data2)

data1 = list(data1_set)
data2 = list(data2_set)
data1.sort()
data2.sort()
print(*data1, sep=', ')
print(*data2, sep=', ')
