def is_valid(name: str):
    if len(name) < 3 or len(name) > 16 or name != name.strip():
        return False

    is_val = True
    for letter in name:
        if not (letter == "-" or letter == "_" or letter.isalpha() or letter.isdigit()):
            is_val = False
            break

    if not is_val:
        return False
    else:
        return True


data = {"usernames": input().split(", "), "valid": []}
for username in data["usernames"]:
    if is_valid(username):
        data["valid"].append(username)

print("\n".join(data["valid"]))

