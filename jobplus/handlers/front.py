from flask import render_template,redirect,url_for
from flask_login import login_user,logout_user,login_required
from flask_wtf import Form
from jobplus.forms import LoginForm

@front.route('/login',methods=['GET','POST'])    
def login():
    form = LoginForm
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()  #数据库表名字User，可以改。这里还缺少判断登录人员的类型。
        login_user(user,form.remember_me.data)
        return redirect(url_for('用户简历管理'))
    return render_template('login.html',form=form)

@front.route('/logout')
@login_required    #若没有登录则不能浏览
def logout():
    logout_user()
    return redirect(url_for('登出到首页？index'))


@front.route('/PersonalRegister',methods=['GET','POST'])
def PersonalRegister():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                username=form.username.data,
                password=form.password.data)
        db.session.add(user)    #提交到user表
        db.session.commit()
        return redirect(url_for('front.login'))
    return render_template('PersonalRegister.html',form=f
            
@front.route('/CompanyRegister',methods=['GET','POST'])
def CompanyRegister():
    form = RegistrationForm()
    if form.validate_on_submit():
        company = Company(email=form.email.data,
            username=form.username.data,
            password=form.password.data)    #Company表单信息
        db.session.add(company)    #提交到Company表
        db.session.commit()
        return redirect(url_for('front.login'))
    return render_template('CompanyRegister.html',form=form)

