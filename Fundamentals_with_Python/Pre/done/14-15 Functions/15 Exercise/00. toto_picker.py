import random
from datetime import datetime


def toto(picks_: int, top_: int, col: int) -> str:

    #  For loop against the requested colons
    for col_num in range(1, col + 1):

        #  Reset Initial List
        col_init = []
        for i in range(1, top_ + 1):
            col_init.append(i)

        col_result = []
        #  Start while loop for number of picks
        while len(col_result) < picks_:
            random_index_1 = random.randint(0, len(col_init) - 1)
            col_result.append(col_init.pop(random_index_1))

        sorted_col_result = sorted(col_result)
        sorted_col_result_as_string_elements = [str(element) for element in sorted_col_result]
        sorted_col_result_string = ", ".join(sorted_col_result_as_string_elements)
        print(f"Колонка {col_num} =  {sorted_col_result_string}")

        #  Append result to file
        current_date_time = datetime.now()
        formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

        file_name = "bst_picker.log"
        with open(file_name, 'a') as file:
            file.write(f"[{formatted_date_time}]Колонка {col_num} =  {sorted_col_result_string}\n")

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

        command = input(f"Избери игра, в границата [1,{len(menu) - 1}] ")
        if command == str(len(menu) - 1):
            is_exit = True
            print("Наслука!")
            break
        else:
            if not command.isdigit():  # digit is numeric int value that is >= 00
                print(f"\nВалиден номер е цифра в границата [1,{len(menu) - 1}]!\n")
                continue
            else:
                if len(menu) - 1 <= int(command) or int(command) < 1:
                    print(f"\nИзбери валиден номер в границата [1,{len(menu) - 1}] ")
                    continue

        #  Select columns quantity
        while True:
            columns = input("Избери брой колонки в границата [1, 4]: ")
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

        current_date_time = datetime.now()
        formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = "bst_picker.log"
        with open(file_name, 'a') as file:
            file.write(f"\n[{formatted_date_time}]Игра =  {menu[command]}\n")

        print(toto(picks, top, columns))


if __name__ == "__main__":
    main()
