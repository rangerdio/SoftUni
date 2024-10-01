def draw_cards(*args, **kwargs):
    monster_cards = {}
    spell_cards = {}
    for name, card_type in args:
        if card_type == 'monster':
            monster_cards[name] = card_type
        elif card_type == 'spell':
            spell_cards[name] = card_type

    for name, card_type in kwargs.items():
        if card_type == 'monster':
            monster_cards[name] = card_type
        elif card_type == 'spell':
            spell_cards[name] = card_type

    monster_cards_sorted = sorted(monster_cards, key=lambda x: x, reverse=True)
    spell_cards_sorted = sorted(spell_cards, key=lambda x: x)
    result = ''

    if monster_cards:
        result += "Monster cards:\n"
        for card in monster_cards_sorted:
            result += f"***{card}\n"
    if spell_cards:
        result += "Spell cards:\n"
        for card in spell_cards_sorted:
            result += f"$$${card}\n"

    return result


# print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
# print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
