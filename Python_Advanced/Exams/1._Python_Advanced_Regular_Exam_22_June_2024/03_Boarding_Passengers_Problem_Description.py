def boarding_passengers(capacity, *args):
    boarded = {}
    boarded_counter = 0

    for group_size, group_name in args:
        if group_size <= capacity:
            capacity -= group_size
            boarded_counter += group_size
            if group_name not in boarded:
                boarded[group_name] = 0
            boarded[group_name] += group_size

    sort_boarded = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))
    total = sum(arg[0] for arg in args)

    result = "Boarding details by benefit plan:\n"

    if boarded_counter == total:
        message = 'All passengers are successfully boarded!'
    elif capacity == 0:
        message = "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        message = f'Partial boarding completed. Available capacity: {capacity}.'

    for group_name, ppl in sort_boarded:
        result += f'## {group_name}: {ppl} guests\n'

    return result + message


# import copy
#
#
# def boarding_passengers(capacity, *args):
#     boarded = {}
#     initial_capacity = capacity
#     args_list = []
#     for element in args:
#         args_list.append(list(element))
#     koko = copy.copy(args_list)
#
#     for group in args_list:
#         if group[0] <= capacity:
#             capacity -= group[0]
#             if group[1] not in boarded.keys():
#                 boarded[group[1]] = 0
#             boarded[group[1]] += group[0]
#             koko.remove(group)
#
#     sort_boarded = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))
#
#     total_shipped = 0
#     message = ''
#     for group, group_size in sort_boarded:
#         total_shipped += group_size
#
#     if capacity == 0 and total_shipped == initial_capacity and len(koko) == 0:
#         message = 'All passengers are successfully boarded!'
#     elif capacity == 0 and len(args_list) > 0:
#         message = "Boarding unsuccessful. Cruise ship at full capacity."
#     elif capacity > 0:
#         message = f'Partial boarding completed. Available capacity: {capacity}.'
#
#     result = 'Boarding details by benefit plan:\n'
#     for group, ppl in sort_boarded:
#         result += f'## {group}: {ppl} guests\n'
#
#     return result + message




# Test input
print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
