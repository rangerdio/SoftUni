def make_italic(function):
    def wrapper(*args, **kwargs):
        return f"<i>{function(*args, **kwargs)}</i>"
    return wrapper


def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"
    return wrapper


def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function(*args, **kwargs)}</b>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
