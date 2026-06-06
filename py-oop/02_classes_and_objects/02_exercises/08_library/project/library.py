from project.user import User

class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {} #{key(author:str): val(books: list[str])}
        self.rented_books = {}    #{key(username:str): {key(book_name), val(days_to_return: int)}}

    def is_rented_by(self, book_name: str):
        '''
        Helper func that iterates through all users and checks if they rented the book, if they did return the days otherwise None
        because days never get updated anyway, this would lead to corrupted code if val could be 0
        :param book_name: str
        :return: days_to_return : int | None
        '''
        for _, value in self.rented_books.items():
            for book, days_to_return in value.items():
                if book_name == book:

                    return days_to_return

        return None


    def get_book(self, author: str, book_name: str, days_to_return: str, user: User):
        rented_days = self.is_rented_by(book_name)
        if rented_days:

            return f'The book "{book_name}" is already rented and will be available in {rented_days} days!'

        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}

            self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:

            return f"{user.username} doesn't have this book in his/her records!"

        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
