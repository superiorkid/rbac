from app import create_app, db
from app.models import User, Role, Permission, AnonymouseUser
from dotenv import load_dotenv

load_dotenv('.env')

app = create_app()

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Role': Role, 'Permission': Permission, 'AnonymousUser': AnonymouseUser}
