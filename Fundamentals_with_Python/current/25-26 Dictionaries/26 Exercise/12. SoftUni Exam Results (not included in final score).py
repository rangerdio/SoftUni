def ban(database_: dict, username_: str, banned_: list):
    database_.pop(username_)
    banned_. append(username_)
    return [database_, banned_]


#  storage = {"ivan": {"basics": 100, "fundamentals": 80, "advance": 44}}
database = {}
database_submissions = {}
banned = []
while True:
    data = input()
    if data == "exam finished":
        break
    elif data.split("-")[1] == "banned":
        ban_result = ban(database, data.split("-")[0], banned)
        database = ban_result[0]
        banned = ban_result[1]
    else:
        username, language, points = data.split("-")[0], data.split("-")[1], int(data.split("-")[2])

        if username not in database.keys():  # if username is not in database
            #  database[username][language] = points
            print(username)
            languages = {language: points}
            database[username] = languages
            language_submissions = {language: 1}
            database_submissions[username] = language_submissions
        elif username in database.keys():  # if username in database,
            if language not in database[username].keys():  # but language is not in users langs
                database[username] = {language: points}
                language_submissions = {language: 1}
                database_submissions[username] = language_submissions
            else:  # language is also in the users langs
                database_submissions[username][language] += 1
                if database[username][language] <= points:
                    database[username][language] = points


print(database)
print(database_submissions)
print(banned)

