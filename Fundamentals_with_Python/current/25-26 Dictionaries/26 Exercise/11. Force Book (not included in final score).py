# force_users = []
# force_sides = []
force = {}

while True:
    data = input()
    if data == "Lumpawaroo":
        break
    elif " | " in data:
        current_user, current_side = data.split(" | ")[1], data.split(" | ")[0]
        # if current_side in force.keys() and current_user in force.values():
        #     continue
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



    print(f"Current force:  {force}")

for side in force.keys():
    if force[side]:
        print(f"Side: {side}, Members: {len(force[side])}")
        for user in force[side]:
            print(f"! {user}")
