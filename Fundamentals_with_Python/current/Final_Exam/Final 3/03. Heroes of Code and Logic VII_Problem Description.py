def cast_spell(heroes_: dict, hero_name_: str, command_value_: int, spell_name: str):
    # print(heroes_, hero_name_, command_value_, spell_name)
    hero_current_mp = heroes_[hero_name_]["mp"]
    required_mp = command_value_
    # print(hero_current_mp)
    if hero_current_mp >= required_mp:
        hero_current_mp -= required_mp
        heroes_[hero_name_]["mp"] = hero_current_mp
        print(f'{hero_name_} has successfully cast {spell_name} and now has {hero_current_mp} MP!')
    else:
        print(f'{hero_name_} does not have enough MP to cast {spell_name}!')
    # print(heroes_)
    return heroes_


def take_damage(heroes_: dict, hero_name_: str, command_value_: int, attacker: str):
    # print(heroes_, hero_name_, command_value_, attacker)
    hero_current_hp = heroes_[hero_name_]["hp"]
    damage_to_take = command_value_
    # print(hero_current_hp, damage_to_take)
    old_hp = hero_current_hp
    hero_current_hp -= damage_to_take
    if hero_current_hp <= 0:
        del heroes_[hero_name_]
        print(f'{hero_name_} has been killed by {attacker}!')
    else:
        print(f'{hero_name} was hit for {damage_to_take} HP by {attacker} and now has {hero_current_hp} HP left!')
        heroes_[hero_name_]["hp"] = hero_current_hp
    return heroes_


def recharge(heroes_: dict, hero_name_: str, command_value_: int, max_mp_: int):
    hero_current_mp = heroes_[hero_name_]["mp"]
    mana_potion = command_value_
    old_mp = hero_current_mp
    hero_current_mp += mana_potion
    if hero_current_mp > max_mp_:
        hero_current_mp = max_mp_
        print(f'{hero_name_} recharged for {max_mp_ - old_mp} MP!')
    else:
        print(f'{hero_name_} recharged for {mana_potion} MP!')
    heroes_[hero_name_]["mp"] = hero_current_mp
    return heroes_


def heal(heroes_: dict, hero_name_: str, command_value_: int, max_hp_: int):
    # print(heroes_, hero_name_, command_value_, max_hp_)
    hero_current_hp = heroes_[hero_name_]["hp"]
    healing_amount = command_value_
    # print(hero_current_hp)
    # print(healing_amount)
    old_hp = hero_current_hp
    #  IF ON MAX HEALTH BEFORE THE ATTEMPT, WE MA Y HAVE "0" MESSAGE possible Judge issue #######################
    if hero_current_hp + healing_amount >= max_hp_:
        hero_current_hp = max_hp_
    else:
        hero_current_hp += healing_amount
    heroes_[hero_name_]["hp"] = hero_current_hp
    # print(heroes_, hero_name_, command_value_, max_hp_)
    print(f'{hero_name_} healed for {hero_current_hp - old_hp} HP!')
    return heroes_


max_hp = 100
max_mp = 200
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
        heroes = cast_spell(heroes, hero_name, int(command_value), line[3])

    elif command == "TakeDamage":
        heroes = take_damage(heroes, hero_name, int(command_value), line[3])

    elif command == "Recharge":
        heroes = recharge(heroes, hero_name, int(command_value), max_mp)

    elif command == "Heal":
        heroes = heal(heroes, hero_name, int(command_value), max_hp)

print(heroes)
for hero, hero_data in heroes.items():
    print(hero)
    print(f'  HP: {hero_data["hp"]}')
    print(f'  MP: {hero_data["mp"]}')
