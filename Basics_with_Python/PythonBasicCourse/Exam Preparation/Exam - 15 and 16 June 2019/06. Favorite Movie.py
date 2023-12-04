movie_winner = ""
movie_counter = 0
movie_winner_points = 0
limit = False
movie_name = input()
while movie_name != "STOP":
    name_len = len(movie_name)
    capital_letter_counter = 0
    small_letter_counter = 0
    movie_counter += 1
    if movie_counter >= 7:
        limit = True
        break
    movie_points = 0
    for index, number in enumerate(movie_name):
        letter_points = ord(number)
        movie_points += letter_points
        if 64 < letter_points < 91:
            capital_letter_counter += 1
        elif 96 < letter_points < 123:
            small_letter_counter += 1

    movie_points = movie_points - small_letter_counter * name_len * 2 - capital_letter_counter * name_len
    if movie_points > movie_winner_points:
        movie_winner_points = movie_points
        movie_winner = movie_name

    movie_name = input()

if limit:
    print("The limit is reached.")
print(f"The best movie for you is {movie_winner} with {movie_winner_points} ASCII sum.")
