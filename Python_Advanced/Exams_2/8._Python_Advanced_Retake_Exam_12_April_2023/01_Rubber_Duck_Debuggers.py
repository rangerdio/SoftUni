from collections import deque
times_sequence = deque([int(x) for x in input().split()])
task_numbers_sequence = [int(x) for x in input().split()]

ducks = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,

}
counter = 0
while times_sequence and task_numbers_sequence:
    current_time = times_sequence.popleft()
    current_task = task_numbers_sequence.pop()
    calculation = current_time * current_task
    if calculation > 240:
        current_task -= 2
        task_numbers_sequence.append(current_task)
        times_sequence.append(current_time)
    elif 0 <= calculation <= 60:
        ducks['Darth Vader Ducky'] += 1
        counter += 1
    elif 61 <= calculation <= 120:
        ducks['Thor Ducky'] += 1
        counter += 1
    elif 121 <= calculation <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
        counter += 1
    elif 181 <= calculation <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
        counter += 1

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for duck, count in ducks.items():
    print(f'{duck}: {count}')
