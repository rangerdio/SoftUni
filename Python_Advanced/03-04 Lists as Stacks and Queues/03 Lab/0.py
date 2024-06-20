
"""
STACKS          LIFO    Last In First Out
my_stack = [1, 3, 4, 5]
my_stack.append(12)
print(my_stack)
my_stack.pop()
print(my_stack)
"""

#
# string = list(input())
# stack = []
# for index in range(len(string)):
#     stack.append(string.pop())
#
# print("".join(stack))


# text = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
# start_indexes_stack = []
# for index, letter in enumerate(text):
#     if letter == "(":
#         start_indexes_stack.append(index)
#     elif letter == ")":
#         start_index = start_indexes_stack.pop()
#         print(text[start_index: index + 1])
#

"""
Queues          FIFO    First-In First-Out
Lists can be used, but its slow due to the slow process of working with index(0) - 

For Queue we "from collections import deque"

 
"""
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")  # Terry arrives
# queue.append("Graham")  # Graham arrives
# queue.popleft()  # First leaves: 'Eric'
# queue.popleft()  # Second leaves: 'John'
# print(queue)  # ['Michael', 'Terry', 'Graham']


# from collections import deque
# queue = deque()
#
# while True:
# #     name = input()
# #     if name == "Paid":
# #         while queue:
# #             print(queue.popleft())
# #
# #     elif name == "End":
# #         print(f"{len(queue)}, people remaining.")
# #         break
# #     else:
# #         queue.append(name)

