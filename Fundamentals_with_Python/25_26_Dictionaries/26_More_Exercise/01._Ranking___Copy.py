# def get_input(contests_: dict, submissions_: dict, delimiter: str, end_contests: str, end_submissions: str):
#     while True:
#         line_ = input()
#         if line == end_contests:
#             break
#         if ":" in line_:
#             contest_, password_ = line_.split(":")
#             contests_[contest_] = password_
#         else:
#             contest_, password_, username_, points_ = line_.split("=>")
#     return 1
def isvalid(contests_: dict, contest_: str, password_: str):
    if contest_ not in contests_.keys():
        return False
    if password_ == contests_[contest_]:
        return True
    return False


contests = {}
submissions = {}


while True:
    line = input().split(":")
    if line[0] == "end of contests":
        break
    contests[line[0]] = line[1]

while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, username, points = line.split("=>")
    points = int(points)
    if isvalid(contests, contest, password):
        #  save the user with the contest they take part in
        if username not in submissions.keys():
            submissions[username] = {contest: points}
        else:
            if contest not in submissions[username].keys():
                submissions[username][contest] = points
            else:
                if points > submissions[username][contest]:
                    submissions[username][contest] = points

sorted_submissions_by_user = dict(sorted(submissions.items()))      # sort alphabet

for username, contests in sorted_submissions_by_user.items():       # sort inside on points
    sorted_contests = dict(sorted(contests.items(), key=lambda item: item[1], reverse=True))
    sorted_submissions_by_user[username] = sorted_contests
sorted_fully = sorted_submissions_by_user

winner_dict = {}
for name in sorted_fully.keys():
    for contest in sorted_fully[name]:
        winner_dict[name] = sum(sorted_fully[name].values())
sorted_winner_dict = dict(sorted(winner_dict.items(), key=lambda item: item[1], reverse=True))

first_key = list(sorted_winner_dict.keys())[0]
print(f'Best candidate is {first_key} with total {sorted_winner_dict[first_key]} points.')

print('Ranking:')
for submission in sorted_fully.keys():
    print(f'{submission}')
    for contest in sorted_fully[submission]:
        print(f'#  {contest} -> {submissions[submission][contest]}')
# print(sorted_fully)
