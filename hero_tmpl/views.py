from flask import render_template
from hero_tmpl import app

#Routes:
#====================================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html', primary_nav="Home")

@app.route('/about')
def about():
    return render_template('about.html', primary_nav="About")
