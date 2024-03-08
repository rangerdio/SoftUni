def ban(database_: dict, username_: str, banned_: list):
    database_.pop(username_)
    banned_.append(username_)


database = {}
language_submissions = {}

banned = []
while True:
    data = input()
    if data == "exam finished":
        break
    elif "-banned" in data:
        banned_user = data.split("-")[0]
        ban(database, banned_user, banned)
    else:
        username, language, points = data.split("-")
        points = int(points)

        if username not in database:
            database[username] = {}

        if language not in database[username] or points > database[username][language]:
            database[username][language] = points

        #  language_submissions[language] = language_submissions.get(language, 0) + 1
        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1

print("Results:")
for user, submissions in database.items():
    max_points = max(submissions.values())
    print(f"{user} | {max_points}")

print("Submissions:")
for language, count in language_submissions.items():
    print(f"{language} - {count}")
