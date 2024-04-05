def populate_dictionary(results: dict, submissions: dict, user: str, lang: str, pts: int):
    if user not in results.keys():      # user have no results
        results[user] = pts

        if lang not in submissions:             # language have no submissions
            submissions[lang] = 1
        else:                                   # language already have some submissions
            submissions[lang] += 1
    else:                               # user already have some results
        if pts > results[user]:
            results[user] = pts

        if lang not in submissions:             # language have no submissions
            submissions[lang] = 1
        else:                                   # language already have some submissions
            submissions[lang] += 1
    return results, submissions


user_results = {}
submissions_ = {}

while True:
    line = input().split("-")
    if line[0] == "exam finished":
        break
    if line[1] == "banned":
        del user_results[line[0]]
    else:
        username, language, points = line[0], line[1], int(line[2])
        user_results, submissions_ = populate_dictionary(user_results, submissions_, username, language, points)

print("Results:")
for username, points in user_results.items():
    print(f'{username} | {points}')
print('Submissions:')
for language, submission_count in submissions_.items():
    print(f'{language} - {submission_count}')
