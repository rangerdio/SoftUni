budged = float(input())
category = (input())
members = int(input())
transport = 0
if 1 <= members <= 4:
    transport = budged * 0.75
elif 5 <= members <= 9:
    transport = budged * 0.60
elif 10 <= members <= 24:
    transport = budged * 0.50
elif 25 <= members <= 49:
    transport = budged * 0.40
elif members >= 50:
    transport = budged * 0.25
tickets_budged = budged - transport
tickets = 0

if category == "VIP":
    tickets = 499.99 * members
    if tickets_budged >= tickets:
        print(f"Yes! You have {(tickets_budged - tickets):.2f} leva left.")
    else:
        print(f"Not enough money! You need {(tickets - tickets_budged):.2f} leva.")
elif category == "Normal":
    tickets = 249.99 * members
    if tickets_budged >= tickets:
        print(f"Yes! You have {(tickets_budged - tickets):.2f} leva left.")
    else:
        print(f"Not enough money! You need {(tickets - tickets_budged):.2f} leva.")
