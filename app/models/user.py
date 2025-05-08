class User:
    def __init__(self, firstname, lastname, dob, email, mobile, address, age, password_hash):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email
        self.mobile = mobile
        self.address = address
        self.age = age
        self.password_hash = password_hash

    def to_dict(self):
        return self.__dict__
