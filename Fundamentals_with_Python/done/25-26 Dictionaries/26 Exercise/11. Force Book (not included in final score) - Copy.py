def pipe(database: dict, user: str, side: str):
    if user in sum(database.values(), []):  # 3rd condition
        return database

    elif user not in sum(database.values(), []) and side not in database.keys():  # 1st condition
        database[side] = [user]

    elif user not in sum(database.values(), []) and side in database.keys():  # 2nd condition
        database[side].append(user)
    return database


def arrow(database: dict, user: str, side: str):
    if side not in database.keys() and all(user not in users for users in database.values()):  # 3rd condition
        database[side] = []
        database[side].append(user)

    elif user not in database.values() and side in database.keys():  # 2nd condition
        database[side].append(user)
        print(f'{user} joins the {side} side!')

    elif user in sum(database.values(), []):  # 1st condition
        for side in database.keys():
            if user not in database[side]:
                database[side].append(user)
                print(f'{user} joins the {side} side!')
            else:
                database[side].remove(user)
    return database


db = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        command = command.split(" | ")
        force_user, force_side = command[1], command[0]
        new_db = pipe(db, force_user, force_side)
        db = new_db
    else:
        command = command.split(" -> ")
        force_user, force_side = command[0], command[1]
        new_db = arrow(db, force_user, force_side)
        db = new_db

