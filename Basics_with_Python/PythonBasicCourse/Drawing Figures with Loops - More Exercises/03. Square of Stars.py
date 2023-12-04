number = int(input())
for i in range(number):
    for j in range(number):
        print("* ", end="") if j < number - 1 else print("*")
