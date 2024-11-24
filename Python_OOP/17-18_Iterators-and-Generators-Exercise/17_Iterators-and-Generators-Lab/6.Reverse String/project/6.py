def reverse_text(text: str):
    reversed_text = text[::-1]
    return reversed_text


for char in reverse_text("step"):
    print(char, end='')
