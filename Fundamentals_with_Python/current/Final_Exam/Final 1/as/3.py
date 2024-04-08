def add(concert_: dict, band_name_: str, member_list_: list):
    # print(concert_)
    # print(band_name_)
    # print(member_list_)
    if band_name_ not in concert_.keys():
        concert[band_name_] = member_list_
    else:
        for member in member_list_:
            if member not in concert_[band_name_]:
                concert_[band_name_].append(member)
    # print(concert_)
    return concert_


def play(concert_, band_name_, time_):

    return concert_


concert = {}
while True:

    line = input()
    if line == "Start!":
        break
    line = line.split("; ")
    command = line[0]

    if command == "Add":
        member_list = line
        band_name = member_list[1]
        member_list.remove("Add")
        member_list.remove(band_name)
        # print(band_name)
        # print(member_list)
        concert = add(concert, band_name, member_list)

    else:  # Play
        member_list = line
        band_name = member_list[1]
        time = int(member_list[2])
        concert = play(concert, band_name, time)
