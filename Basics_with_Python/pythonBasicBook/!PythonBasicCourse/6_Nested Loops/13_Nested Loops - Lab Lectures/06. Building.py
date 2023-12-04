floors = int(input())
rooms = int(input())
_f = floors
_r = 0
fl = ""
room = ""
while _f > 0:
    while _r < rooms:
        if _f == floors:
            room = "L" + str(_f) + str(_r)
            fl += (" " + room)
        elif _f % 2 != 0:
            room = "A" + str(_f) + str(_r)
            fl += (" " + room)
        else:
            room = "O" + str(_f) + str(_r)
            fl += (" " + room)
        _r += 1
    _f -= 1
    _r = 0
    print(fl)
    fl = ""
#
# floors = int(input())
# rooms = int(input())
# fl = ""
# room = ""
# for _f in range(floors, 0, -1):
#     for _r in range(rooms):
#         if _f == floors:
#             room = "L" + str(_f) + str(_r)
#             fl += (" " + room)
#         elif _f % 2 != 0:
#             room = "A" + str(_f) + str(_r)
#             fl += (" " + room)
#         else:
#             room = "O" + str(_f) + str(_r)
#             fl += (" " + room)
#     print(fl)
#     fl = ""
#