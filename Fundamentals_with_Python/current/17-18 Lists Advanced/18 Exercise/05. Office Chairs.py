number_of_rooms = int(input())
free_chairs = 0
for current_room in range(1, number_of_rooms + 1):
    chairs_in_current_room, visitors_in_current_room = input().split()
    difference = len(chairs_in_current_room) - int(visitors_in_current_room)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {current_room}")
        free_chairs += difference
    else:
        free_chairs += difference
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
