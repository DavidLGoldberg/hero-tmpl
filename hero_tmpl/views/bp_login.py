from flask import current_app, Blueprint

bp_login = Blueprint('bp_login', __name__)

"""
Code based on the Flask-Login example:
"""

"""
Flask-Login example
===================
This is a small application that provides a trivial demonstration of
Flask-Login, including remember me functionality.

:copyright: (C) 2011 by Matthew Frazier.
:license:   MIT/X11, see LICENSE for more details.
"""

from flask import render_template, request, flash, redirect, url_for
from flask.ext.login import (LoginManager, AnonymousUser, UserMixin,
    login_required, login_user, confirm_login, logout_user, fresh_login_required)

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active

class Anonymous(AnonymousUser):
    name = u"Anonymous"

USERS = {
    1: User(u"Notch@notch.com", 1),
    2: User(u"Steve@steve.com", 2),
    3: User(u"Creeper@creeper.com", 3, False),
}

USER_NAMES = dict((u.name, u) for u in USERS.itervalues())

SECRET_KEY = "yeah, not actually a secret"
DEBUG = True

#TODO: might not need this, or might need it above..
#current_app.config.from_object(__name__)

login_manager = LoginManager()
login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))

print 'b4 setup'
login_manager.setup_app(current_app) #line currently breaks!!!!!!!!!!!
print 'after setup'
#print app.login_manager

#Routes:
#====================================
@bp_login.route("/")
def index():
    print 'hereeeeeeeeeeeeee'
    return render_template("index.html", primary_nav="Home")

@bp_login.route("/secret")
@fresh_login_required
def secret():
    return render_template("secret.html")

@bp_login.route("/login", methods=["GET", "POST"])
def login():
    print 'in login'
    if request.method == "POST":
        print 'in post!'

    if request.method == "POST" and "username" in request.form:
        print 'in post and username'
        username = request.form["username"]
        print username
        if username in USER_NAMES:
            print 'in user_names'
            remember = request.form.get("remember", "no") == "yes"
            if login_user(USER_NAMES[username], remember=remember):
                print 'logged in!'
                flash("Logged in!")
                return redirect(request.args.get("next") or url_for("index"))
            else:
                print 'could not log in!'
                flash("Sorry, but you could not log in.")
        else:
            print 'could not log in!'
            flash(u"Invalid username.")
        
    print 'in login get'
    return render_template("login.html", primary_nav="Home")

@bp_login.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")

@bp_login.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))
