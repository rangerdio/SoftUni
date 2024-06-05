morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' '}

reversed_morse_dict = {value: key for key, value in morse_dict.items()}

text = input()
words = text.split("|")
# print(words)

new_words = []
for word in words:
    letters = word.split(" ")
    new_word = ""
    for letter in letters:
        if letter in reversed_morse_dict.keys():
            new_word += reversed_morse_dict[letter]
    new_words.append(new_word)
print(" ".join(new_words))
