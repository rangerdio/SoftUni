from functools import reduce


def operate(operator, *args):
    def plus():
        return reduce(lambda x, y: x + y, args)

    def minus():
        return reduce(lambda x, y: x - y, args)

    def multiply():

        return reduce(lambda x, y: x * y, args)

    def divide():

        return reduce(lambda x, y: x / y, args)

    commands = {"+": plus,
                "-": minus,
                "*": multiply,
                '/': divide}

    return commands[operator]()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
