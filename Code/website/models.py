
from flask_login import UserMixin

class User():
    def __init__(self,email,first_name,password=0):
        self.id=email
        self.first_name = first_name
        self.password=password

    def is_active(self):
        """True, as all users are active."""
        return True
    def get_fname(self):
        return self.first_name

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False