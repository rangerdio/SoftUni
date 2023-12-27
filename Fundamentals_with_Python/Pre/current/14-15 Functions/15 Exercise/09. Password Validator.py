def validator(pass_):
    is_valid = True
    digit_length = ""

    if 6 > len(pass_) or len(pass_) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    for index, value in enumerate(pass_):
        if not value.isalpha() and not value.isdigit():
            print("Password must consist only of letters and digits")
            is_valid = False
            break

    digits = 0
    for index, value in enumerate(pass_):
        if int(value.isdigit()):
            digits += 1
    if digits < 2:
        digit_length = "Password must have at least 2 digits"
        is_valid = False
    if is_valid:
        return "Password is valid"
    else:
        return digit_length


password = input()
print(validator(password))
