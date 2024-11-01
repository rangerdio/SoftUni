from project.album import Album


class Band:
    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str) -> str:
        try:
            my_album = [album for album in self.albums if album.name == album_name][0]
            if my_album.published:
                return f'Album has been published. It cannot be removed.'
            if my_album.name == album_name:
                self.albums.remove(my_album)
                return f'Album {my_album.name} has been removed.'
        except IndexError:
            return f'Album {album_name} is not found.'

    def details(self) -> str:
        band_details = f'Band {self.name}\n'
        return band_details + '\n'.join(album.details() for album in self.albums)
