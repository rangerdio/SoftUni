from collections import deque
# field = []
# my_initial_position = []
# for row in range(5):
#     sublist = input().split()
#     if 'A' in sublist:
#         my_initial_position = [row, sublist.index('A')]
#     field.append(sublist)
field = [['.', '.', '.', '.', '.'],
         ['x', '.', '.', '.', '.'],
         ['.', 'A', '.', '.', '.'],
         ['.', '.', '.', 'x', '.'],
         ['.', 'x', '.', '.', 'x']]
my_initial_position = [2, 1]


def check_coordinates():

    return True


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command_queue = deque([])
n = int(input())
for _ in range(n):
    command_queue.append(input().split())

my_current_position = my_initial_position
while command_queue:
    current_command = command_queue.popleft()
    action = current_command[0]

    is_valid_move = check_coordinates(field, my_current_position)

    if action == "move":
        pass
    elif action == "shoot":
        pass

    # update current possition