koko
from collections import deque

seats = input().split(', ')
firsts = deque([int(x) for x in input().split(', ')])
seconds = [int(x) for x in input().split(', ')]
counter = 0

while firsts and seconds:
    counter += 1
    first = firsts.popleft()
    second = seconds.pop()
    char = chr(second + first)
