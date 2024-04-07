message = input()

while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break


print(f'You have a new text message: {message}')
