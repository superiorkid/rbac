from flask import render_template, abort, url_for, redirect
from . import main
from flask_login import login_required, current_user
from ..decorators import admin_required, permission_required
from ..models import Permission, User

@main.route('/')
@login_required
def index():
  return render_template('main/index.html', title='Index')

@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
  return 'For admin only'


@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderator_only():
  return 'FOR MODERATOR'


@main.post('/user/<username>')
@main.get('/user/<username>')
def user(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    abort(404)

  return render_template('user.html', user=user)
