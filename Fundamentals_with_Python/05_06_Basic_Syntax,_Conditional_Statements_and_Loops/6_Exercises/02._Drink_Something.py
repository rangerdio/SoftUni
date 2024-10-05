age = int(input())
drink = ""
if age <= 14:
    drink = "toddy"
elif 18 >= age > 14:
    drink = "coke"
elif 21 >= age > 18:
    drink = "beer"
elif age > 21:
    drink = "whisky"
print("drink " + drink)
