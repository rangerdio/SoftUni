class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


specials = ("@", "*", "&", "%")
while True:
    password = input()
    if password == "Done":
        break
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if " " in password:
        raise PasswordContainsSpacesError("Password cannot contain spaces")
    if not any(char for char in password) in specials:
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character')
    if all(char.isdigit() for char in password) or all(char.isalpha() for char in password) \
            or all(char for char in password) in specials:
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if any(char.isdigit() for char in password) \
            and any(char.isalpha() for char in password) and any(char for char in password) in specials:
        print('Password is valid')
    else:
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
