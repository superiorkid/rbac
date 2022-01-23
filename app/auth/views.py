from . import auth
from .forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for, request
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse
from .. import db

@auth.post('/login')
@auth.get('/login')
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user is not None and user.verify_password(form.password.data):
      login_user(user, remember=form.remember_me.data)
      next = request.args.get('next')
      if next is None or not next.startswith('/'):
        next = url_for('main.index')

      return redirect(next)

    flash('Invalid username or password')

  return render_template('auth/login.html', form=form, title='Log In')



@auth.get('/register')
@auth.post('/register')
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    user = User(email=form.email.data, username=form.username.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('You can now login')
    return redirect(url_for('auth.login'))

  return render_template('auth/registration.html', form=form)



@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logged out')
  return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
  if current_user.is_authenticated:
    current_user.ping()
    db.session.commit()
