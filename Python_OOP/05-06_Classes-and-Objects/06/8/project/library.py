from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        # the two conditions here per how the description is written are that the book is either rented, or not
        # it doesnt look that the book is not exist
        try:
            found_book = [book_name for author, books in self.books_available.items() if book_name in books][0]
        except IndexError:
            return 's'

    def return_book(self, param, param1, user):
        pass