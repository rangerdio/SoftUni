def accommodate(*args, **kwargs):
    groups = list(args)
    rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))
    # print(groups, rooms)
    accommodated = {}
    total_needed = sum(groups)
    for group in groups:
        for room_name, room_capacity in rooms:
            if group == room_capacity:
                accommodated[room_name] = group
    # print(groups, rooms)
    # print(groups)
    # print(accommodated)

    for room_name, room_capacity in accommodated.items():
        if (room_name, room_capacity) in rooms:
            rooms.remove((room_name, room_capacity))
            # print(rooms)
            groups.remove(room_capacity)
            #print(groups, rooms)
    # for room_name, room_capacity in accommodated.items():
    #     rooms.remove((room_name, room_capacity))
    #     groups.remove(room_capacity)
    # print(accommodated)
    # print(groups, rooms)

    # print(f'acc {accommodated}')
    for group in groups:
        for room_name, room_capacity in rooms:
            if group < room_capacity:
                accommodated[room_name] = group

    # print(rooms)
    # print(groups)
    for room_name, room_capacity in accommodated.items():
        # print(room_name, room_capacity)
        for room in rooms:
            if room_name in room:
                rooms.remove(room)
                # groups.remove(room_capacity)
                # print(rooms)
                # print(groups)

    accommodated_sorted = sorted(accommodated.items(), key=lambda x: x[0])
    result = ''
    if accommodated:
        result += f'A total of {len(accommodated)} accommodations were completed!\n'
        for room_name, group_size in accommodated_sorted:
            result += f'<Room {room_name} accommodates {group_size} guests>\n'
    else:
        result += 'No accommodations were completed!\n'

    accommodated_guests = sum(accommodated.values())

    if total_needed - accommodated_guests > 0:
        result += f'Guests with no accommodation: {total_needed - accommodated_guests}\n'
    if rooms:
        result += f'Empty rooms: {len(rooms)}'

    return result


# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print(accommodate(10, 9, 8, room_307=6, room_802=5))
# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
