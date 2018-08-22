import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess_used-if-no-env-SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Signal the application every time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False