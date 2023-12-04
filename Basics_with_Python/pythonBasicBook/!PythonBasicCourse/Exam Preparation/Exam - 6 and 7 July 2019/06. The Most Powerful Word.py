flag1 = False
#  word_length = 0
previous_score = 0
winner = ""
while True:
    word = input()
    if word == "End of words":
        break
    word_lower_case = word.lower()
    word_length = len(word_lower_case)
    score = 0
    for index, number in enumerate(word):
        letter = ord(number)
        score += ord(number)
        if index == 0 and (ord(number) == 97 or ord(number) == 101 or ord(number) == 105 or ord(number) == 111 or ord(number) == 117 or ord(number) == 121 or ord(number) == 65 or ord(number) == 69 or ord(number) == 73 or ord(number) == 79 or ord(number) == 85 or ord(number) == 89):
            flag1 = True
    if flag1:
        score *= len(word)
    else:
        score = int((score / len(word)))
    if score > previous_score:
        winner = word
        previous_score = score
        flag1 = False
        score = 0
print(f"The most powerful word is {winner} - {previous_score}")
