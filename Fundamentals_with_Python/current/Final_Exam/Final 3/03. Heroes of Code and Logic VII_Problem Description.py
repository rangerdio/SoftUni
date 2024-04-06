def cast_spell(heroes_: dict, hero_name_: str, command_value_: int, spell_name: str):
    return heroes_


def take_damage(heroes_: dict, hero_name_: str, command_value_: int, attacker: str):
    return heroes_


def recharge(heroes_: dict, hero_name_: str, command_value_: int):
    return heroes_


def heal(heroes_: dict, hero_name_: str, command_value_: int):
    return heroes_


heroes = {}
n = int(input())
for i in range(n):
    hero_data = input().split()
    name, hp, mp = hero_data[0], int(hero_data[1]), int(hero_data[2])
    heroes[name] = {"hp": hp, "mp": mp}
# print(heroes)

while True:
    line = input().split(" - ")
    if line[0] == "End":
        break

    command, hero_name, command_value = line[0], line[1], line[2]
    if command == "CastSpell":
        cast_spell(heroes, hero_name, int(command_value), line[3])
        pass

    elif command == "TakeDamage":
        take_damage(heroes, hero_name, int(command_value), line[3])
        pass

    elif command == "Recharge":
        recharge(heroes, hero_name, int(command_value))
        pass

    elif command == "Heal":
        heal(heroes, hero_name, int(command_value))
        pass
