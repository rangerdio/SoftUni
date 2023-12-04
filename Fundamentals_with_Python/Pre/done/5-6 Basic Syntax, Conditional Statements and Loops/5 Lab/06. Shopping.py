budged = int(input())

command = input()
while command != "End":
    price = int(command)
    budged -= price
    if budged < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
