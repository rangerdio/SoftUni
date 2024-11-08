import math


class PhotoAlbum:
    PAGE_SIZE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for page in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(math.ceil(photos_count / cls.PAGE_SIZE))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < self.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        sep = f'{"-" * 11}\n'
        result = sep
        for page in self.photos:
            result += " ".join('[]' for element in page) + "\n"
            result += sep
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
# print(album.photos)



