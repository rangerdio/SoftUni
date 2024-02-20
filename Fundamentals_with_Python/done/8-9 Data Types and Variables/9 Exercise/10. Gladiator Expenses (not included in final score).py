lost_fight_count = int(input())
helmed_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
costs = 0
shield_count = 0
for lost in range(1, lost_fight_count + 1):
    if lost % 2 == 0:
        costs += helmed_price
    if lost % 3 == 0:
        costs += sword_price
        if lost % 2 == 0:
            costs += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                costs += armor_price
print(f"Gladiator expenses: {costs:.2f} aureus")
