def isvalid(ticket):
    if len(ticket) == 20:
        return True
    else:
        return False


line = "$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey"
tickets = line.split()
print(tickets)

for element in tickets:
    if not isvalid(element):
        print("invalid ticket")
    else:
        print("valid")


