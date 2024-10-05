movie_name = input()
counter = 0
points_current_movie = 0
points_best_movie = 0
best_movie = ""
movie_length = 0

while movie_name != "STOP":
    counter += 1
    movie_length = len(movie_name)
    points_current_movie = 0

    for index, symbol in enumerate(movie_name):
        symbol_int = ord(symbol)

        if 97 <= symbol_int <= 122:
            points_current_movie += symbol_int - 2 * movie_length
        elif 65 <= symbol_int <= 90:
            points_current_movie += symbol_int - movie_length
        else:
            points_current_movie += symbol_int

    if points_current_movie > points_best_movie:
        points_best_movie = points_current_movie
        best_movie = movie_name
    if counter == 7:
        break

    movie_name = input()

if movie_name != "STOP":
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {points_best_movie} ASCII sum.")
