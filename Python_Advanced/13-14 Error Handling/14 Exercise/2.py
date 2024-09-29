class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = (".com", ".bg", ".org", ".net")
while True:
    email = input()
    name = email.split("@")[0]
    domain = "." + email.split('.')[1]
    if email == "End":
        break
    elif len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif domain not in domains:
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print('Email is valid')
