himikalki = int(input())
markers = int(input())
preparat = int(input())
discount = int(input())

total = himikalki * 5.8 + markers * 7.2 + preparat * 1.2
print(total * (100 - discount) / 100)
