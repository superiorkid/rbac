from . import auth
from .forms import LoginForm
from flask import render_template, flash, redirect, url_for, request
from ..models import User
from flask_login import login_user, logout_user, login_required

@auth.post('/login')
@auth.get('/login')
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user is None or not user.verify_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('auth.login'))

    login_user(user, remember=form.remember_me.data)
    next = request.args.get('next')

    if next is None or not next.startswith('/'):
      next = url_for('main.index')

    return redirect(next)

  return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logged out')
  return redirect(url_for('main.index'))
