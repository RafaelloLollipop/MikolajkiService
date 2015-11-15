class Mikolaj(object):
    def __init__(self,username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username