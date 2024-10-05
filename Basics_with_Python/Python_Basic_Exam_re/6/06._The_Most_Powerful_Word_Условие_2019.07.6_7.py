import math

winner_word = ""
winner_word_pts = 0
word = input()

while word != "End of words":
    current_pts = 0
    word_length = len(word)
    for index, letter in enumerate(word):
        letter_num = ord(letter)
        current_pts += letter_num
    if ord((word[0]).lower()) in [97, 101, 105, 111, 117, 121]:
        current_pts *= word_length
    else:
        current_pts = math.floor(current_pts / word_length)

    if current_pts >= winner_word_pts:
        winner_word_pts = current_pts
        winner_word = word
    word = input()
print(f"The most powerful word is {winner_word} - {winner_word_pts}")
