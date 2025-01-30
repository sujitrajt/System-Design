from Book import Book

class Member:
    def __init__(self,name,member_id,contact_info):
        self._name = name
        self._member_id = member_id
        self._contact_info = contact_info
        self._books = []

    @property
    def member_id(self):
        return self._member_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def contact_info(self):
        return self._contact_info
    
    @property
    def books(self):
        return self._books
    
    def borrowed_books(self,book):
        return self._books.append(book)
    
    def return_books(self,book):
        return self._books.remove(book)