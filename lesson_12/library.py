class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        self.__books_count = len(self.books)

    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        self.__books_count = len(self.books)
        return new_book
    
    def __repr__(self):
        return "'{}', books: {}".format(self.name, self.books_count)
    
    def __str__(self):
        return "'{}', books: {}".format(self.name, self.books_count)
    
    def group_by_author(self, author):
        author_books = [book for book in self.books if book.author == author]
        return author_books

    def group_by_year(self, year):
        books_years = [book for book in self.books if book.year == year]
        return book_years

    def get_books_count(self):
        return self.__books_count

class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return "'{}', year: {}, auth: {}".format(self.name, self.year, self.author)
    
    def __str__(self):
        return "'{}', year: {}, auth: {}".format(self.name, self.year, self.author)

class Author:
    def __init__(self, name, country, books=[]):
        self.name = name
        self.country = country
        self.books = []
        
    def __str__(self):
        return "{}, {}".format(self.name, self.country)
    
    def __repr__(self):
        return "{}, {}".format(self.name, self.country)
        
library = Library('Boston')
author = Author('John', 1980)
library.new_book('Physics', 1996, author)
library.new_book('Astronomics', 1997, author)

author2 = Author('Freud', 1970)
library.new_book('Psychology', 1996, author2)
library.new_book('Psychology 2', 1977, author2)


freud_books = library.group_by_author(author2)
print('freud_books')
for book in freud_books:
    print(book)

