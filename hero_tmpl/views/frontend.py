from flask import current_app, render_template, Blueprint
#from hero_tmpl import app

frontend = Blueprint('frontend', __name__)

#Routes:
#====================================
@frontend.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@frontend.route('/')
def index():
    return render_template('index.html', primary_nav="Home")

@frontend.route('/about')
def about():
    return render_template('about.html', primary_nav="About")
