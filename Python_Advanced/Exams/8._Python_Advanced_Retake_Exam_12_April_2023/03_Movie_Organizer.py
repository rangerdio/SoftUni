def movie_organizer(*movie_data):
    genders = {}
    for movie_name, gender in movie_data:
        if gender not in genders:
            genders[gender] = []
        genders[gender].append(movie_name)
    genders_sorted = sorted(genders.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for gender, movies in genders_sorted:
        result += f"{gender} - {len(movies)}\n"
        movies_sorted = sorted(movies)
        for movie in movies_sorted:
            result += f'* {movie}\n'
    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
