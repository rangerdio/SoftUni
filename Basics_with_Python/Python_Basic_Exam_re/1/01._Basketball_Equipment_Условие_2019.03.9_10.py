yearly_tax = int(input())

boots = yearly_tax * 0.60
outfit = boots * 0.80
ball = outfit / 4
accessories = ball / 5

total = yearly_tax + boots + outfit + ball + accessories

print(f"{total:.2f}")
