
text = input()
try:
    num = int(input())

except ValueError:
    print("Input must be an integer")

else:
    print(text * num)
