from setuptools import setup

setup(
    name='hero-tmpl',
    version='1.0',
    long_description=__doc__,
    packages=['hero_tmpl'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.8',
        'Jinja2==2.6',
        'Werkzeug==0.8.3',
        'distribute==0.6.24',
        'gevent==0.13.6',
        'greenlet==0.3.4',
        'gunicorn==0.13.4',
        'wsgiref==0.1.2'
    ]
)
