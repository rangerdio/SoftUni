from collections import deque
strings = deque([x for x in input().split()])
# strings = deque(['d', 'yel', 'blu', 'e', 'low', 'redd',])
# strings = deque(['r', 'ue', 'nge', 'ora', 'bl', 'ed'])
# strings = deque(['re', 'ple', 'blu', 'pop', 'e', 'pur', 'd'])

available_colors = ("red", "yellow", "blue", "orange", "purple", "green")
colors = []

while strings:

    # if only one element
    if len(strings) == 1:
        substring = strings.pop()
        if substring in available_colors:
            colors.append(substring)
        else:
            substring_cut = substring[0:-1:]
            if len(substring_cut) != 0:
                strings.append(substring_cut)
    else:
        # concatenate, check and append the lists
        first_substring = strings.popleft()
        second_substring = strings.pop()
        concatenate = first_substring + second_substring
        concatenate_2 = second_substring + first_substring

        if concatenate in available_colors:
            colors.append(concatenate)
        elif concatenate_2 in available_colors:
            colors.append(concatenate_2)
        else:
            first_substring_cut = first_substring[0:-1:]
            second_substring_cut = second_substring[0:-1:]

            if first_substring_cut:
                strings.insert(len(strings) // 2, first_substring_cut)
            if second_substring_cut:
                strings.insert(len(strings) // 2, second_substring_cut)

# color_map = {
#     'orange': ['red', 'yellow'],
#     'purple': ['red', 'blue'],
#     'green': ['yellow', 'blue'],
# }
# secondary = ['orange', 'purple', 'green']
#
# # print(colors)
# for color in secondary:
#     if color in colors:
#         needed_colors = color_map[color]
#         primary_color_1 = needed_colors[0]
#         primary_color_2 = needed_colors[1]
#
#         if primary_color_1 not in colors or primary_color_2 not in colors:
#             colors.remove(color)

for _ in range(len(colors)):    # checking if multiple times one collor is found to remove properly
    if 'orange' in colors:
        if 'red' not in colors or 'yellow' not in colors:
            colors.remove('orange')
    if 'purple' in colors:
        if 'red' not in colors or 'blue' not in colors:
            colors.remove('purple')
    if 'green' in colors:
        if 'yellow' not in colors or 'blue' not in colors:
            colors.remove('green')

print(colors)
