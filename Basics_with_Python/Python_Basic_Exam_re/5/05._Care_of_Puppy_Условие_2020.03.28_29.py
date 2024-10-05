food = float(input())
eaten = 0
food *= 1000

command = input()
while command != "Adopted":
    eaten = int(command)
    food -= eaten
    command = input()
diff = int(abs(food))

if food < 0:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")
