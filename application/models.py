import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

'''
class Admin(db.Document):
    # pylint: disable=no-member
    admin_id     =   db.IntField(unique=True)
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True)
    password    =   db.StringField()
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def get_password(self, password):
        return check_password_hash(self.password, password)  

'''

class User(db.Document):
    # pylint: disable=no-member
    user_id     =   db.IntField(unique=True)
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True)
    password    =   db.StringField()
    Year = db.StringField()
    branch = db.StringField()


    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def get_password(self, password):
        return check_password_hash(self.password, password)  

    def set_tgid(self, password):
        self.password = generate_password_hash(password)

    def get_tgid(self, password):
        return check_password_hash(self.password, password)  
            
'''
class Staff(db.Document):
    # pylint: disable=no-member
    staff_id     =   db.IntField(unique=True)
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True)
    password    =   db.StringField()

    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def get_password(self, password):
        return check_password_hash(self.password, password)  
'''

class Books(db.Document):
     # pylint: disable=no-member
    BookId   =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    publication =   db.StringField( max_length=255 )
    author     =   db.StringField()
    No_of_Copies       =   db.IntField( max_length=10 )
    Year =   db.StringField( max_length=5 )

class Issue(db.Document):
     # pylint: disable=no-member
    user_id     =   db.IntField() 
    BookId   =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    publication =   db.StringField( max_length=255 )
    author     =   db.StringField()
    Issue_date = db.DateField()
    Return_date = db.DateField()
    Year =   db.StringField( max_length=5)
    branch = db.StringField( max_length=25)
    fees = db.IntField( max_length=25)
    paid = db.StringField( max_length=4)
    pending = db.StringField( max_length=4)
    