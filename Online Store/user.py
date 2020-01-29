from db import DB

class User:
    def __init__(self, id, email, password, name, adress, phone_number):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.adress = adress
        self.phone_number = phone_number

    def create(self):
        with DB() as db:
            values = (self.email,
                      self.password,
                      self.name,
                      self.adress,
                      self.phone_number)
            db.execute('INSERT INTO USERS (EMAIL, PASSWORD, NAME, ADRESS, \
                PHONE) VALUES (?, ?, ?, ?, ?)', values)
            return self

    @staticmethod
    def find(email):
        with DB() as db:
            row = db.execute('SELECT * FROM USERS WHERE EMAIL = ?',
                             (email, )).fetchone()
            return User(*row)