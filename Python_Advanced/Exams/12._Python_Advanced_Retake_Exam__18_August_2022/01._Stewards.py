from collections import deque

seats = input().split(', ')
firsts = deque([int(x) for x in input().split(', ')])
seconds = deque([int(x) for x in input().split(', ')])
counter = 0
seated = []

while firsts and seconds:
    counter += 1
    first = firsts.popleft()
    second = seconds.pop()
    char = chr(second + first)
    if str(first) + char in seats or str(second) + char in seats:
        if str(first) + char in seats and str(second) + char not in seated:
            seated.append(str(first) + char)
        if str(second) + char in seats and str(second) + char not in seated:
            seated.append(str(second) + char)
    else:
        firsts.append(first)
        seconds.appendleft(second)
    if counter == 10 or len(seated) == 3:
        break
print(f'Seat matches: {", ".join(seated)}')
print(f'Rotations count: {counter}')
