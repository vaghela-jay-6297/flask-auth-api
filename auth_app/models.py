# User_app/models.py
from app import db, bcrypt    # get db, bcrypt variables from app file

class BaseModel(db.Model):
    __abstract__ = True
    # Fix columns
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    is_delete = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)


class User(BaseModel):
    __tablename__ = 'user'  # table name
    
    # New Columns with BaseModel Columns
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(20))
    password_hash = db.Column(db.String(128), nullable=False)
    
    def __repr__(self):
        return f'<User {self.name} ({self.email})>'
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):   # to set password
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):    # to verify password
        return bcrypt.check_password_hash(self.password_hash, password) 