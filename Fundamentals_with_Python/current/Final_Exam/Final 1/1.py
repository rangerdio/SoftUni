message = "ivanivanov"
index = 4
letter = message[index - 1]
message = message.replace(letter, letter + " ", 1)
print(message)
