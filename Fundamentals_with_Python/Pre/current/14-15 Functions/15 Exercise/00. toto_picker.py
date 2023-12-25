def toto_649():
    return


def toto_642():
    return


def toto_535():
    return


def main():
    is_exit = False
    print("Toto Picker")
    menu = list("Меню://Тото 6/49//Тото 6/42//Тото 5/35//Изход".split("//"))

    while True:
        print()
        for index in range(len(menu)):
            if index == 0:
                print(f"{menu[index]}")
            else:
                print(f"{index}. {menu[index]}")
        print()

        command = input(f"Избери опция в инвервал [1,{len(menu) - 1}] ")
        if command == str(len(menu) - 1):
            is_exit = True
            print("Наслука!")
            break
        else:
            if not command.isdigit():  # digit is numeric int value that is >= 0
                print(f"\nВалидна опция е цифра в интервал [1,{len(menu) - 1}]!\n")
                continue
            else:
                command = int(command)
                if len(menu) - 1 <= command:
                    print(f"\nИзбери валидна опция в интервал [1,{len(menu) - 1}] ")
                    continue
                break  # test

    if not is_exit:
        # Function Calling section
        if command == 1:
            toto_649()
        elif command == 2:
            toto_642()
        elif command == 3:
            toto_642()


if __name__ == "__main__":
    main()
