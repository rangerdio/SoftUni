balance = 0
while True:
    n = input()
    if n == "NoMoreMoney":
        break
    if float(n) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(n):.2f}")
    balance += float(n)
print(f"Total: {balance:.2f}")
