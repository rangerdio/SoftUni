from collections import deque


def list_manipulator(nums, action, location,  *args):
    nums = deque(nums)
    args = deque(args)
    if action == 'add' and location == 'beginning':
        while args:
            current_arg = args.pop()
            nums.appendleft(current_arg)
    elif action == 'add' and location == 'end':
        while args:
            current_arg = args.popleft()
            nums.append(current_arg)
    elif action == 'remove' and location == 'beginning':
        if not args:
            nums.popleft()
        else:
            for arg in args:
                for i in range(arg):
                    nums.popleft()

    elif action == 'remove' and location == 'end':
        if not args:
            nums.pop()
        else:
            for arg in args:
                for i in range(arg):
                    nums.pop()
    return list(nums)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
