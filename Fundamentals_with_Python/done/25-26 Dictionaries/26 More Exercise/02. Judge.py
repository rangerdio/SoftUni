database = {}
user_totals = {}

while True:
    data = input()
    if data == "no more time":
        break
    username, contest, points = data.split(" -> ")
    points = int(points)

    if contest not in database.keys():                  # otherwise save data
        database[contest] = {username: points}
    else:                                              # user participated contest
        if username not in database[contest] or points > database[contest][username]:
            database[contest][username] = points

    # user_totals[username] = user_totals.get(username, 0) + points       # same as bellow commented

    # if username in database[contest]:
    #     user_totals[username] = max(user_totals.get(username, 0), points)

    # if username not in user_totals.keys():
    #     user_totals[username] = points
    # else:
    #     if username == "Peter":
    #         print(username)
    #         print(database[contest][username])
    #         print(user_totals[username])
    #         print(database)
    #
    #     if not database[contest][username]:
    #         user_totals[username] += points
    #     else:
    #         if points > user_totals[username]:
    #             user_totals[username] = points

# print(database)
# getting totals
for exam, tots in database.items():
    for user, pts in tots.items():
        user_totals[user] = user_totals.get(user, 0) + pts

database_inner_sorted = {}
database_sorted = {}
for exam in database.keys():
    # inner_sorted_ = dict(sorted(database[exam].items(), key=lambda item: (item[1], item[0]), reverse=True))
    inner_sorted_ = dict(sorted(database[exam].items(), key=lambda item: (-item[1], item[0])))
    database_inner_sorted[exam] = inner_sorted_
# print(database_inner_sorted)
# database_sorted = dict(sorted(database_inner_sorted))



for exam in database_inner_sorted.keys():
    print(f'{exam}: {len(database_inner_sorted[exam])} participants')
    counter = 0
    for user, points in database_inner_sorted[exam].items():
        counter += 1
        print(f'{counter}. {user} <::> {points}')


user_totals_sorted = dict(sorted(user_totals.items(), key=lambda item: (-item[1], item[0])))

print('Individual standings:')
counter = 0
for user, points in user_totals_sorted.items():
    counter += 1
    print(f'{counter}. {user} -> {points}')
