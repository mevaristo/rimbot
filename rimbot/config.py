import os

db_dir = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'data'
    )

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') \
        or os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        or os.path.join('sqlite:///' + db_dir, "rimbot.db") 
    SQLALCHEMY_TRACK_MODIFICATIONS = False