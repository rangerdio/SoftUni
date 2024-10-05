city = input()
sells = float(input())
error = False
commission = 0
if city == "Sofia":
    if 0 <= sells <= 500:
        commission = sells * 0.05
    elif 500 < sells <= 1000:
        commission = sells * 0.07
    elif 1000 < sells <= 10000:
        commission = sells * 0.08
    elif sells > 10000:
        commission = sells * 0.12
    else:
        error = True
elif city == "Varna":
    if 0 <= sells <= 500:
        commission = sells * 0.045
    elif 500 < sells <= 1000:
        commission = sells * 0.075
    elif 1000 < sells <= 10000:
        commission = sells * 0.10
    elif sells > 10000:
        commission = sells * 0.13
    else:
        error = True
elif city == "Plovdiv":
    if 0 <= sells <= 500:
        commission = sells * 0.055
    elif 500 < sells <= 1000:
        commission = sells * 0.08
    elif 1000 < sells <= 10000:
        commission = sells * 0.12
    elif sells > 10000:
        commission = sells * 0.145
    else:
        error = True
else:
    error = True

if error:
    print("error")
else:
    print(f"{commission:.2f}")
