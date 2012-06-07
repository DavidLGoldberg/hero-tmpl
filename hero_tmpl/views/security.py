from flask import current_app, Blueprint

security = Blueprint('security', __name__)

from flask import render_template
from flask.ext.security import LoginForm, login_required, \
    roles_required, roles_accepted

@security.route('/')
def index():
    return render_template('index.html', content='Home Page')

@security.route('/login')
def login():
    return render_template('login.html', content='Login Page', form=LoginForm())

@security.route('/custom_login')
def custom_login():
    return render_template('login.html', content='Custom Login Page', form=LoginForm())

@security.route('/profile')
@login_required
def profile():
    return render_template('index.html', content='Profile Page')

@security.route('/post_login')
@login_required
def post_login():
    return render_template('index.html', content='Post Login')

@security.route('/post_logout')
def post_logout():
    return render_template('index.html', content='Post Logout')

@security.route('/post_register')
def post_register():
    return render_template('index.html', content='Post Register')

@security.route('/admin')
@roles_required('admin')
def admin():
    return render_template('index.html', content='Admin Page')

@security.route('/admin_or_editor')
@roles_accepted('admin', 'editor')
def admin_or_editor():
    return render_template('index.html', content='Admin or Editor Page')
