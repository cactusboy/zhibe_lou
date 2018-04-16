from flask import Blueprint, redirect, flash, url_for, render_template
from flask_login import login_required, current_user
from jobplus.forms import CompanyMsgForm

company = Blueprint('company',__name__, url_prefix='/company')

@company.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('你不是企业用户','warning')
        return redirect(url_for('front.index'))
    form = CompanyMsgForm(obj=current_user.company)
    form.name.data = current_user.name
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('更新企业信息成功!', 'success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)
