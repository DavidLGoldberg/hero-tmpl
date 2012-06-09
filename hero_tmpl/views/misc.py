from flask import current_app, render_template, Blueprint

misc = Blueprint('misc', __name__)

#Routes:
#====================================
@misc.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@misc.route('/')
def index():
    return render_template('index.html', content="Home Page", primary_nav="Home")

@misc.route('/about')
def about():
    return render_template('about.html', primary_nav="About")
