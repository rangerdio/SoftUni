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
            force[current_user] = current_side

    elif " -> " in data:
        current_user, current_side = data.split(" -> ")[0], data.split(" -> ")[1]
        if current_user not in force:
            force[current_user] = current_side
            print(f"{current_user} joins the {current_side} side!")
        else:
            print(f"{current_user} joins the {current_side} side!")
            force[current_user] = current_side

# Organize force users into their respective sides
sides = {}
for user, side in force.items():
    if side not in sides:
        sides[side] = []
    sides[side].append(user)

# Print the sides and their members
for side, members in sides.items():
    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")
