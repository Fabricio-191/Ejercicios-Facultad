from os import path

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.dirname(__file__) + '/src/datos.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False