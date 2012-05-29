Example:
=============
* Demo: http://hero-tmpl.com
* Code: https://github.com/DavidLGoldberg/hero-tmpl-site

Install Steps:
=============
* ensure:
    sudo apt-get install python-dev libevent-dev lessc
* ensure:
    sudo gem install watchr
* ensure:
    heroku plugins:install git://github.com/ddollar/heroku-config.git
* run:
    virtualenv venv --distribute
* run:
    source venv/bin/activate
* run:
    heroku create --stack cedar
* run:
    cp ./sample_env ./.env
* run:
    heroku config:push --overwrite --interactive
* run:
    heroku config
* verify:
    all config values are as desired for production
* Add titles
* Adjust humans.txt

After launch:
==============
* index.html: remove NOINDEX, NOFOLLOW
* robots.txt: remove disallow /

TODO:
==============
* make a few things configurable:
    - contact us address
