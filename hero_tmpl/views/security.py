from flask import current_app, Blueprint

security = Blueprint('security', __name__)

from flask import render_template
from flask.ext.security import LoginForm, login_required, \
    roles_required, roles_accepted

@security.route('/login')
def login():
    return render_template('login.html', content='Login Page', form=LoginForm())

@security.route('/')
@login_required
def home():
    return render_template('index.html', content='Home Page', primary_nav="Home")

@security.route('/admin')
@roles_required('admin')
def admin():
    return render_template('admin.html', content='Admin Page')
