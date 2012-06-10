from flask import current_app, render_template, Blueprint

misc = Blueprint('misc', __name__)

#Routes:
#====================================
@misc.route('/')
def index():
    return render_template('index.html', content="Home Page", primary_nav="Home")

@misc.route('/about')
def about():
    return render_template('about.html', primary_nav="About")
