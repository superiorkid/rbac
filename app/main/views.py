from flask import render_template
from . import main
from flask_login import login_required, current_user
from ..decorators import admin_required, permission_required
from ..models import Permission

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
