def add_songs(*information):
    result = ''
    songs = {}
    for song_title, lines in information:
        if song_title not in songs:
            songs[song_title] = []
        for line in lines:
            songs[song_title].append(line)

    for song_title, lines in songs.items():
        result += f"- {song_title}\n"
        for line in lines:
            if line:
                result += f"{line}\n"

    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
