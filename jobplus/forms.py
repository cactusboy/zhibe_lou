from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import User, db

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    
    def validate_email(self, field):
        if field.data and User.query.filter_by(email=field.data):
            raise ValidationError('邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and user.check_password(filed.data):
            raise ValidationError('密码错误')

class UserRegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(6,24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first:
            raise ValidationError('用户名已存在')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data):
            raise ValidationError('邮箱已存在')


    def create_user(self):
        user = User(name=self.name.data,
            email=self.email.data,
            password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user
        

class EnterpriseRegisterForm(FlaskForm):
    name = StringField('企业名称', validators=[Required(), Length(6,24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first:
            raise ValidationError('企业名称已存在')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data):
            raise ValidationError('邮箱已存在')


    def create_user(self):
        user = User(name=self.name.data,
            email=self.email.data,
            password=self.password.data)
        db.session.add(user)
        db.session.commit()
class PersonalMsg(FlaskForm):
    name = StringField('姓名')
    
