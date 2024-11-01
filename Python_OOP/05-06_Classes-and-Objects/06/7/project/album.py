from project.song import Song


class Album:
    def __init__(self, name: str, *args: Song) -> None:
        self.name = name
        self.published: bool = False
        self.songs: list[Song] = list(args)

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return 'Cannot remove songs. Album is published.'
        try:
            song = [el for el in self.songs if song_name == el.name][0]
            self.songs.remove(song)
            return f'Removed song {song_name} from album {self.name}.'
        except IndexError:
            return 'Song is not in the album.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self) -> str:
        details = f'Album {self.name}\n'
        song_info = [f'== {song.get_info()}' for song in self.songs]
        return details + '\n'.join(song_info)
