force = {}

while True:
    data = input()
    if data == "Lumpawaroo":
        break
    elif " | " in data:
        current_user, current_side = data.split(" | ")[1], data.split(" | ")[0]
        if current_user not in force:
            force[current_user] = current_side
        elif force[current_user] != current_side:
            previous_side = force[current_user]
            force[current_user] = current_side
            if previous_side in force:
                force[previous_side].remove(current_user)

    elif " -> " in data:
        current_user, current_side = data.split(" -> ")[0], data.split(" -> ")[1]
        if current_user not in force:
            force[current_user] = current_side
            print(f"{current_user} joins the {current_side} side!")
        else:
            print(f"{current_user} joins the {current_side} side!")
            previous_side = force[current_user]
            force[current_user] = current_side
            if previous_side in force:
                force[previous_side].remove(current_user)

sides = {}
for user, side in force.items():
    sides.setdefault(side, []).append(user)

for side, users in sides.items():
    print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f"! {user}")
