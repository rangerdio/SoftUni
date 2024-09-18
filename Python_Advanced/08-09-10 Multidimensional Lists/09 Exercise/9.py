from collections import deque
# n = int(input())
# movement = input().split()
# field = [[x for x in input().split()] for row in range(n)]
n = 5
movement = deque(['up', 'right', 'right', 'up', 'right'])
field = [['*', '*', '*', 'c', '*'],
         ['*', '*', '*', 'e', '*'],
         ['*', '*', 'c', '*', '*'],
         ['s', '*', '*', 'c', '*'],
         ['*', '*', 'c', '*', '*']]

while movement:
    command = movement.popleft()
