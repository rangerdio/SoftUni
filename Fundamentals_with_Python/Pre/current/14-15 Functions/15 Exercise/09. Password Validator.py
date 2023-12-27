def validator(pass_):
    is_valid_1 = False
    is_valid_2 = False
    is_valid_3 = False
    if 6 > len(pass_) or len(pass_) > 10:
        print("Password must be between 6 and 10 characters")
    else:
        is_valid_1 = True

    for index, value in enumerate(pass_):
        if not value.isalpha() and not value.isdigit():
            print("Password must consist only of letters and digits")
            break
        else:
            is_valid_2 = True

    digits = 0
    for index, value in enumerate(pass_):
        if int(value.isdigit()):
            digits += 1
    if digits < 2:
        print("Password must have at least 2 digits")
    else:
        is_valid_3 = True
    if is_valid_1 and is_valid_2 and is_valid_3:
        print("Password is valid")
    return


password = input()
pw_check = validator(password)
