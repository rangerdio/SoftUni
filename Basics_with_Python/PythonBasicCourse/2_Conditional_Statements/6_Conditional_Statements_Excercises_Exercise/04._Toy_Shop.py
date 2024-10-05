vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
income = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2

if puzzles + dolls + bears + minions + trucks >= 50:
    income = income * 0.75
income = income * 0.9

if vacation_price <= income:
    print(f"Yes! {income - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - income:.2f} lv needed.")