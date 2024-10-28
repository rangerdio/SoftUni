from project.song import Song


class Album:
    def __init__(self, name: str, *args: tuple[Song]) -> None:
        self.name = name
        self.published: bool = False
        self.songs = list(args)
