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
    real_name = db.Column(db.String(32))
    name = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    phone = db.Column(db.String(11))
    work_years = db.Column(db.SmallInteger)
    resume_url = db.Column(db.String(128))
    

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
        return 'User {}'.format(self.name)

class Enterprise(Base):
    __tablename__ = 'enterprise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    logo = db.Column(db.String(512), unique=True, nullable=False)
    website = db.Column(db.String(512), nullable=False)
    oneword_profile = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    position_number = db.Column(db.Integer, nullable=False)
    enterprise_description = db.Column(db.String(1024), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='SET NULL'))
    user = db.relationship('User', uselist=False, backref=db.backref('enterprise', uselist=False))

    def __repr__(self):
        return 'Enterprise {}'.format(self.name)

class Job(Base):
    __tablename__  = 'job'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    salary_min = db.Column(db.Integer, nullable=False)
    salary_max = db.Column(db.Integer, nullable=False)
    experience_requirement = db.Column(db.String(1024) , nullable=False)
    location = db.Column(db.String(64), nullable=False)
    enterprise_msg = db.Column(db.String(1024))
    enterprise_id = db.Column(db.Integer, db.ForeignKey('enterprise.id', ondelete='CASCADE'))
    enterprise = db.relationship('Enterprise', uselist=False, backref=('jobs'))
    job_requirement = db.Column(db.String(1024))
    job_description = db.Column(db.String(1024))
    job_number = db.Column(db.Integer)

    def __repr__(self):
        return '<Job {}>'.format(self.name)
    
