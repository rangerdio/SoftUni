def toto(picks_, top_, columns):
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
            if not command.isdigit():  # digit is numeric int value that is >= 00
                print(f"\nВалидна опция е цифра в интервал [1,{len(menu) - 1}]!\n")
                continue
            else:
                if len(menu) - 1 <= int(command) or int(command) < 1:
                    print(f"\nИзбери валидна опция в интервал [1,{len(menu) - 1}] ")
                    continue

        #  Select columns quantity
        while True:
            columns = input("Изберере брой колонки в интервал [1, 4]: ")
            if not columns.isdigit():
                continue
            elif int(columns) == 1:
                print(f"\nВашият избор е {columns} колонкa на {menu[int(command)]}:\n")
                break
            elif 0 < int(columns) < 5:
                print(f"\nВашият избор е {columns} колонки на {menu[int(command)]}:\n")
                break
            else:
                continue

        break  # test

    if not is_exit:
        # Function calling
        # input data is
        if command == menu[1]:
            picks = 6
            top = 49
        elif command == menu[2]:
            picks = 6
            top = 42
        elif command == menu[3]:
            picks = 5
            top = 35
        print()



if __name__ == "__main__":
    main()
