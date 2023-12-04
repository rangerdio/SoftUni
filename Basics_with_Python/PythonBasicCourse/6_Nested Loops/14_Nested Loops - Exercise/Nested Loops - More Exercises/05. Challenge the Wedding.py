men = int(input())
women = int(input())
max_tables = int(input())
no_tables = False
for num1 in range(1, men + 1):
    for num2 in range(1, women + 1):
        print(f"({num1} <-> {num2})", end=" ")
        max_tables -= 1
        if max_tables == 0:
            no_tables = True
            break
    if no_tables:
        break
