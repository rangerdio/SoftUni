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

    user_totals[username] = user_totals.get(username, 0) + points       # same as bellow commented
    # if username not in user_totals.keys():
    #     user_totals[username] = points
    # else:
    #     user_totals[username] += points

# print(database)
print(user_totals)


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
    for user, points in database_inner_sorted[exam].items():
        print(f'1. {user} <::> {points}')
