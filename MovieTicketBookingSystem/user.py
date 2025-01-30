class User:
    def __init__(self,name,email,phone,id):
        self._name = name
        self._email = email
        self._phone = phone
        self._id = id
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_email(self):
        return self._email
    
    @property
    def get_phone(self):
        return self._phone  
    
    @property
    def get_id(self):
        return self._id 
    
