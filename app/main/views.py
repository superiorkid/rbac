from flask import render_template, abort, url_for, redirect, flash
from . import main
from flask_login import login_required, current_user
from ..decorators import admin_required, permission_required
from ..models import Permission, User, Role
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db

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


@main.route('/user/<username>')
def user(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    abort(404)

  return render_template('user.html', user=user, title='Profile')


@main.get('/edit-profile')
@main.post('/edit-profile')
@login_required
def edit_profile():
  form = EditProfileForm()

  if form.validate_on_submit():
    current_user.name = form.name.data
    current_user.location = form.location.data
    current_user.about_me = form.about_me.data
    db.session.commit()
    flash('Your changes have been saved.')
    return redirect(url_for('.user', username=current_user.username))

  form.name.data = current_user.name
  form.location.data = current_user.location
  form.about_me.data = current_user.about_me
  return render_template('edit_profile.html', form=form, title="Edit Profile")


@main.post('/edit-profile/<int:id>')
@main.get('/edit-profile/<int:id>')
@login_required
@admin_required
def edit_profile_admin(id):
  user = User.query.get_or_404(id)
  form = EditProfileAdminForm(user=user)

  if form.validate_on_submit():
    user.email = form.email.data
    user.username = form.username.data
    user.role = Role.query.get(form.role.data)
    user.name = form.name.data
    user.location = form.location.data
    user.about_me = form.about_me.data
    db.session.commit()
    flash('The profile has been updated.')
    return redirect(url_for('.user', username=user.username))

  form.email.data = user.email
  form.username.data = user.username
  form.role.data = user.role_id
  form.name.data = user.name
  form.location.data = user.location
  form.about_me.data = user.about_me
  return render_template('edit_profile.html', form=form, user=user, title='Edit Profile [Admin]')
