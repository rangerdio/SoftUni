class Article:

    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        pass

    def change_author(self, new_author: str):
        pass

    def rename(self, new_title: str):
        pass

    def __repr__(self):
        pass

