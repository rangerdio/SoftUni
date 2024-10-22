x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)  # line 3

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)      # line 2
    inner()
    print("outer:", x)      # line 4
    change_global()


print(x)    # line 1
outer()
print(x)    # line 5
