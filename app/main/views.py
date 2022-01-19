from flask import render_template
from . import main
from flask_login import login_required, current_user
from ..decorators import admin_required, permission_required
from ..models import Permission

@main.route('/')
@login_required
def index():
  return render_template('main/index.html', title="Index")


@main.route('/admin')
@login_required
@admin_required
def for_admin():
  return 'for administrator'


@main.route('/users')
@login_required
@permission_required(Permission.COMMENT)
def for_user():
  return 'for USER'
