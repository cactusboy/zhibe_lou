from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime 

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_ENTERPRISE = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, set_password):
        self._password = generate_password_hash(set_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)
    @property
    def is_enterprise(self):
        return self.role == self.ROLE_ENTERPRISE

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def __repr__(self):
        return 'user {}'.format(self.name)

class Enterprise(Base):
    __tablename__ = 'enterprise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return 'Enterprise {}'.format(self.name)

class Postion(Base):
    __tablename__  = 'position'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    

    def __repr__(self):
        return '<Postion {}>'.format(self.name)
    
