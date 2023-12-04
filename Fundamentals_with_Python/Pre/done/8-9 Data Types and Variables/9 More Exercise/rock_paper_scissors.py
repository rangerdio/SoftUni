# project under :  C:\Users\vladi\PycharmProjects\rock_paper_scissors\rock_paper_scissors
# public on GitHub

import random
from colorama import Fore, Style, Back
from colorama import init as colorama_init
colorama_init()
rock = "Камък"
paper = "Хартия"
scissors = "Ножица"

player_move = input(f"{Fore.CYAN}Изберете {Style.RESET_ALL}{Fore.MAGENTA}[к]{Style.RESET_ALL}{Fore.CYAN}амък, \
{Style.RESET_ALL}{Fore.MAGENTA}[н]{Style.RESET_ALL}{Fore.CYAN}ожица или \
{Style.RESET_ALL}{Fore.MAGENTA}[х]{Style.RESET_ALL}{Fore.CYAN}артия: {Style.RESET_ALL}")

if player_move == "к":
    player_move = rock
elif player_move == "х":
    player_move = paper
elif player_move == "н":
    player_move = scissors
else:
    raise SystemExit(f"{Back.RED}Невалиден Вход. Опитайте Отново...{Style.RESET_ALL}g")

bot_move = random.randint(1, 3)
if bot_move == 1:
    bot_move = rock
elif bot_move == 2:
    bot_move = paper
else:
    bot_move = scissors
print(f"{Fore.CYAN}Вие избрахте {player_move}{Style.RESET_ALL}")
print(f"{Fore.CYAN}Компютъра избра {bot_move}{Style.RESET_ALL}")

if player_move == rock and bot_move == scissors or \
        player_move == paper and bot_move == rock or \
        player_move == scissors and bot_move == paper:
    print(f"{Fore.CYAN}Вие печелихте играта!{Style.RESET_ALL}")
elif player_move == bot_move:
    print(f"{Fore.CYAN}Завършихте наравно!{Style.RESET_ALL}")
else:
    print(f"{Back.RED}Вие захубихте играта!{Style.RESET_ALL}")


# import random
#
#
# rock = "Rock"
# paper = "Paper"
# scissors = "Scissors"
#
# player_move = input("Choose [r]ock, p[aper] or [s]cissors: ")
#
# if player_move == "r":
#     player_move = rock
# elif player_move == "p":
#     player_move = paper
# elif player_move == "s":
#     player_move = scissors
# else:
#     raise SystemExit("Invalid Input. Try again...")
#
# bot_move = random.randint(1, 3)
# if bot_move == 1:
#     bot_move = rock
# elif bot_move == 2:
#     bot_move = paper
# else:
#     bot_move = scissors
#
# print(f"The computer chose {bot_move}")
#
# if player_move == rock and bot_move == scissors or \
#         player_move == paper and bot_move == rock or \
#         player_move == scissors and bot_move == paper:
#     print("You win!")
# elif player_move == bot_move:
#     print("Draw!")
# else:
#     print("You lose!")
