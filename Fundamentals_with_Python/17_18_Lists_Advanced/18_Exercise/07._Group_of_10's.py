numbers = list(map(int, input().split(", ")))
group = 10
while numbers:
    current_group = [element for element in numbers if element <= group]
    [numbers.remove(element) for element in current_group]
    print(f"Group of {group}'s: {current_group}")
    group += 10

# numbers = list(map(int, input().split(", ")))
# group = 10
# while numbers:
#     current_group = [element for element in numbers if element <= group]
#     for element in current_group:
#         numbers.remove(element)
#     print(f"Group of {group}'s: {current_group}")
#     group += 10
