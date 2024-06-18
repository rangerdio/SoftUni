import random
from colorama import Fore, Style, Back, init as colorama_init
colorama_init()
computer_number = random.randint(1, 100)
while True:
    player_number = input(f"{Fore.CYAN}Избери число. Търсеното число е в интервала [1 - 100]: {Style.RESET_ALL}")
    if not player_number.isdigit():
        print(f"{Back.RED}Невалиден избор! {Style.RESET_ALL}{Fore.CYAN}\
        Моля изберете число в интервала [1 - 100]!{Style.RESET_ALL}")
        continue
    player_number = int(player_number)
    if player_number == computer_number:
        print(f"{Fore.MAGENTA}Вие познахте числото!{Style.RESET_ALL}")
        break
    elif player_number > computer_number:
        print(f"{Fore.CYAN}Числото е по-ниско от {player_number}.{Style.RESET_ALL}")
        continue
    else:
        print(f"{Fore.CYAN}Числото е по-високо от {player_number}.{Style.RESET_ALL}")
        continue
