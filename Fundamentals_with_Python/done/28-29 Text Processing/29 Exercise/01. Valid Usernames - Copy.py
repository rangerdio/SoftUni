valid_len = []
valid_usernames = []
usernames = input().split(", ")
for username in usernames:
    if not (len(username) < 3 or len(username) > 16):
        valid_len.append(username)

for username in valid_len:
    isvalid = True
    for ch in username:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            isvalid = False
    if isvalid:
        valid_usernames.append(username)

for asd in valid_usernames:
    print(asd)
