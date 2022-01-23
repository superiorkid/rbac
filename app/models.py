from . import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, index=True)
  email = db.Column(db.String(64), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

  def __repr__(self):
    return f'<Username {self.username}>'

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __init__(self, **kwargs):
    super(User, self).__init__(**kwargs)
    if self.role is None:

      if self.email == current_app.config['IS_ADMIN']:
        self.role = Role.query.filter_by(permissions=0xff).first()

      if self.role is None:
        self.role = Role.query.filter_by(default=True).first()


  def can(self, permissions):
    return self.role is not None and (self.role.permissions & permissions) == permissions

  def is_administrator(self):
    return self.can(Permission.ADMINISTER)

class AnonymouseUser(AnonymousUserMixin):
  def can(self, permissions):
    return False

  def is_administrator(self):
    return False

login_manager.anonymous_user = AnonymouseUser


class Permission:
  FOLLOW = 0x01
  COMMENT = 0x02
  WRITE_ARTICLES = 0x04
  MODERATE_COMMENTS = 0x08
  ADMINISTER = 0x80


class Role(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)
  default = db.Column(db.Boolean, default=False, index=True)
  permissions = db.Column(db.Integer)
  users = db.relationship('User', backref='role', lazy='dynamic')

  def __repr__(self):
    return f'<Role {self.name}>'

  def __init__(self, **kwargs):
    super(Role, self).__init__(**kwargs)
    if self.permissions is None:
      self.permissions = 0

  def add_permission(self, perm):
    if not self.has_permission(perm):
      self.permissions += perm

  def remove_permission(self, perm):
    if self.has_permission(perm):
      self.permissions -= perm

  def reset_permissions(self):
    self.permissions = 0

  def has_permission(self, perm):
    return self.permissions & perm == perm

  @staticmethod
  def insert_roles():
    roles = {
      'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
      'Moderator': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, False),
      'Administrator': (0xff, False)
    }

    for r in roles:
      role = Role.query.filter_by(name=r).first()
      if role is None:
        role = Role(name=r)

      role.permissions = roles[r][0]
      role.default = roles[r][1]
      db.session.add(role)
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

