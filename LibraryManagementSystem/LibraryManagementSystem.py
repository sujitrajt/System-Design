from Book import Book
from Member import Member

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.catalogs = {}
            cls._instance.members = {}
            cls._instance.MAX_BOOKS_ISSUED_TO_A_USER = 5
            cls._instance.MAX_LENDING_DAYS = 10
        return cls._instance
    
    @staticmethod
    def get_instance():
        if Library._instance is None:
            Library()
        return Library._instance
    
    def add_book(self,book):
        self.catalogs[book.get_isbn] = book

    def remoove_book(self,isbn):
        self.catalogs.pop(isbn)

    def get_book(self,isbn):
        return self.catalogs.get(isbn)
    
    def add_member(self,member:Member):
        self.members[member.member_id] = member

    def remove_member(self,member_id):
        self.members.pop(member_id)
    
    def get_member(self,member_id):
        return self.members.get(member_id)
    
    def borrow_books(self,isbn, member_id):
        book = self.get_book(isbn)
        member = self.get_member(member_id)
        if book and member:
            if book.is_available() and len(member.books) < self.MAX_BOOKS_ISSUED_TO_A_USER:
                book._available = False
                member.borrowed_books(book)
                return True
        return False
    
    def return_books(self,isbn,member_id):
        book = self.get_book(isbn)
        member = self.get_member(member_id)
        if book and member:
            if book in member.books:
                book._available = True
                member.return_books(book)
                return True
        return False
    
    def search_by_title(self,title):
        return [book for book in self.catalogs.values() if book.get_title == title]