vacation_cost = float(input())
available_money = float(input())
counter_break = 0
counter_total = 0

while True:
    action = input()
    action_sum = float(input())
    counter_total += 1
    if action == "save":
        available_money += action_sum
        counter_break = 0
        if available_money >= vacation_cost:
            print(f"You saved the money for {counter_total} days.")
            break

    elif action == "spend":
        counter_break += 1
        if action_sum <= available_money:
            available_money -= action_sum
        else:
            available_money = 0
    if counter_break == 5:
        print("You can't save the money.")
        print(counter_total)
        break


# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере
# необходимата сума.
# Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева
