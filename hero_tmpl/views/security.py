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

#@security.route('/post_login')
#@login_required
#def post_login():
    #return render_template('index.html', content='Post Login')

#@security.route('/post_logout')
#def post_logout():
    #return render_template('index.html', content='Post Logout')

#@security.route('/post_register')
#def post_register():
    #return render_template('index.html', content='Post Register')

@security.route('/admin')
@roles_required('admin')
def admin():
    return render_template('admin.html', content='Admin Page')
