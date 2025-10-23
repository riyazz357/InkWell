from flask import render_template,flash,redirect,url_for
from app.auth import bp
from app.auth.forms import LoginForm,RegistrationForm
from app import db
from app.models import User
from flask_login import current_user, login_user, logout_user

@bp.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',title='Register',form=form)

@bp.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('auth.login'))
        flash(f'Welcome back, {user.username}')
        return redirect(url_for('main.index'))
    return render_template('auth/login.html',title='Sign In',form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))