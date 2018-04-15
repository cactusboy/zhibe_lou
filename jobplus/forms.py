from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,EqualTo
from wtforms import ValidationError

class LoginForm(Form):        #登录页面的内容  
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

#    def validate_email(self,field):
#        if field.data and not User.query.filter_by(email=field.data).first()
#            raise ValidationError('')
#还差检测密码的，暂时看不懂怎么写


class PersonalRegister(Form):    #求职者注册页面内容
    username = StringField('用户名',validators=[Required(),Length(1,64)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repear_password = PasswordField('重复密码',validators=[Requried(),Length(6,24),EqualTo('password',message = '密码要一致')])
    submit = SubmitField('注册')

#等数据库的名称确定好才用，这里默认数据库的用户表叫user
#    def validate_email(self,field):
#        if User.query.filter_by(email=field.data).first()
#            raise ValidationError('邮箱已经被注册')
#
#    def validate_username(self,field):
#        if User.query.filter_by(username=field.data).first()
#            raise ValidationError('用户名已经被注册')

class CompanyRegister(Form):
    companyname = StringField('公司名称',validators=[Required(),Length(1,64)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),Length(6,24),EqualTo('password',message = '密码要一致')])
    submit = SubmitField('注册')

#    def validate_email(self,field):
#        if Company.query.filter_by(email=field.data).first()
#            raise ValidationError('邮箱已经被注册')
#
#    def validate_companyname(self,field):
#        if Company.query.filter_by(companyname=field.data).first()
#            raise ValidationError('公司名称已经被注册')
