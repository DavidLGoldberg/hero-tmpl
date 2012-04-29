import os
from flask import Flask, render_template
from werkzeug import SharedDataMiddleware

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__,
            static_folder=os.path.join(PROJECT_ROOT, 'public'),
            static_url_path='/public')

app.config.update(os.environ)
app.debug = app.config['DEBUG']

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, 
    {'/': os.path.join(os.path.dirname(__file__), 'public') })

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

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
