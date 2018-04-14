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
    email = StringField('邮箱', validators=[Required(), email()])
    password = PasswordField('密码(不填写保持不变)')
    phone = StringField('手机号')
    work_years = IntegerField('工作年限')
    resume_url = StringField('上传简历')
    submit = SubmitField('提交')
    
    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13','15','18') and len(phone) != 11:
            raise ValidationError('请输入有效手机号码')

    def updated_user(self, user):
        user.real_name = self.name.data
        user.email = self.email.data
        user.phone = self.phone.data
        user.work_years = self.work_years.data
        user.resume_url = self.resume_url.data
        if self.password.data:
            user.password = self.password.data
        db.session.add(user)
        db.session.commit()


