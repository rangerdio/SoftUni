# force_users = []
# force_sides = []
force = {}

while True:
    data = input()
    if data == "Lumpawaroo":
        break
    elif " | " in data:
        current_user, current_side = data.split(" | ")[1], data.split(" | ")[0]
        if current_side in force.keys():
            isExist = False
            for side in force.keys():
                if current_user in force[side]:
                    isExist = True
            if isExist:
                continue

        elif current_user not in force.values() and current_side not in force.keys():
            force[current_side] = [current_user]

        elif current_side in force.keys() and current_user not in force.values():
            force[current_side].append(current_user)
        
    elif " -> " in data:
        current_user, current_side = data.split(" -> ")[0], data.split(" -> ")[1]

        if current_side not in force.keys():    # no such force side and # no such force user (3rd option)
            notExist = True
            for side in force.keys():
                if current_user in force[side]:
                    notExist = False
            if notExist:
                force[current_side] = [current_user]
                print(f"{current_user} joins the {current_side} side!")

        elif current_side in force.keys():  # there is such force side existing
            notExist = True
            for side in force.keys():
                if current_user in force[side]:
                    notExist = False

            if notExist:  # but not such force user in any side
                force[current_side].append(current_user)
                print(f"{current_user} joins the {current_side} side!")
            else:   # but user exists
                # print("we come here???")
                side_to_remove = ""
                side_to_add = ""
                for side in force.keys():
                    if current_user not in force[side]:
                        side_to_add = side
                for side in force.keys():
                    if current_user in force[side]:
                        side_to_remove = side
                force[side_to_remove].remove(current_user)
                force[side_to_add].append(current_user)
                print(f"{current_user} joins the {side_to_add} side!")

    #  print(f"Current force:  {force}")

for side in force.keys():
    if force[side]:
        print(f"Side: {side}, Members: {len(force[side])}")
        for user in force[side]:
            print(f"! {user}")
