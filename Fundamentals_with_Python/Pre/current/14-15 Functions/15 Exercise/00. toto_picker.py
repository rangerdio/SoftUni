def toto(picks_, top_, col):
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    for i in range(1, top_ + 1):
        col_1.append(i)
        col_2.append(i)
        col_3.append(i)
        col_4.append(i)
    print(f"{col_1}\n{col_2}\n{col_3}\n{col_4}")

    return "Наслука!"


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
                print(f"\nВашият избор е {columns} колонкa за Игра {menu[int(command)]}:\n")
                break
            elif 0 < int(columns) < 5:
                print(f"\nВашият избор е {columns} колонки за Игра {menu[int(command)]}:\n")
                break
            else:
                continue

        break  # test

    if not is_exit:
        # Function calling
        # input data is
        picks = 0
        top = 0
        columns = int(columns)
        command = int(command)
        if command == menu.index("Тото 6/49"):
            picks = 6
            top = 49
        elif command == menu.index("Тото 6/42"):
            picks = 6
            top = 42
        elif command == menu.index("Тото 5/35"):
            picks = 5
            top = 35
        print(toto(picks, top, columns))



if __name__ == "__main__":
    main()
