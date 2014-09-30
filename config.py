CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' }]
    
import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get("HEROKU") is not None:
    print "nothing here yet"
else: 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None

# pagination
POSTS_PER_PAGE = 3