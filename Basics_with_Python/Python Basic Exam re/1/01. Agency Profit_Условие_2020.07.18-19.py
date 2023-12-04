avio_name = input()
tickets_adults = int(input())
tickets_kids = int(input())
adult_ticket_price = float(input())
kids_ticket_price = adult_ticket_price * 0.3
tax = float(input())
adult_ticket_price += tax
kids_ticket_price += tax

total = tickets_kids * kids_ticket_price + tickets_adults * adult_ticket_price
profit = total * 0.20

print(f"The profit of your agency from {avio_name} tickets is {profit:.2f} lv.")
