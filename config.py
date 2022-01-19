import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://superiorkid:root@localhost/rbac'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
