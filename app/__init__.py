from flask import Flask, send_from_directory
from whitenoise import WhiteNoise
app = Flask(__name__)

# Allows the app to identify the static folder
app.static_folder = 'static'
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root='static/',
    prefix='static/')

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

#Configuration of application, see configuration.py, choose one and uncomment.
configuration = 'app.configuration.ProductionConfig'
#configuration = 'app.configuration.DevelopmentConfig'
app.config.from_object(configuration)
print('Running server on ' + app.config['ENV'] + '.')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
print('Running database at', app.config['SQLALCHEMY_DATABASE_URI'])

from app import views, models

db.create_all()