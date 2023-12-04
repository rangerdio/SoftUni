grads = int(input())
daytime = input()
outfit = 0
shoes = 0
if daytime == "Morning":
    if 18 >= grads >= 10:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if 24 >= grads > 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if grads > 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif daytime == "Afternoon":
        if 18 >= grads >= 10:
            outfit = "Shirt"
            shoes = "Moccasins"
        if 24 >= grads > 18:
            outfit = "T-Shirt"
            shoes = "Sandals"
        if grads > 24:
            outfit = "Swim Suit"
            shoes = "Barefoot"
elif daytime == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {grads} degrees, get your {outfit} and {shoes}.")