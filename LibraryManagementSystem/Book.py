class Book:

    def __init__(self, isbn, title, author, year):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._year = year
        self._available = True

    @property
    def get_isbn(self):
        return self._isbn
    
    @property
    def get_title(self):
        return self._title
    
    @property
    def get_author(self):
        return self._author
    
    @property
    def get_year(self):
        return self._year
    
    
    def is_available(self):
        return self._available
    
        