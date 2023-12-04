import math
magnolia = int(input())
zumbul = int(input())
roses = int(input())
cactus = int(input())
gift_amount = float(input())
total = (magnolia * 3.25 + zumbul * 4 + roses * 3.50 + cactus * 8) * 0.95
difference = abs(total - gift_amount)
if total >= gift_amount:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")