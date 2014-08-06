from app import app, db

from auth import *
from admin import admin
from api import api
from models import *
from views import *
from flask_rum.main import rum
import flask_rum.rum_config as rum_config


admin.setup()
api.setup()

app.config.from_object(rum_config)
# Sample override of Theme
app.config.THEME_FOLDER='rum/banana/'

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Message.create_table(fail_silently=True)
    Relationship.create_table(fail_silently=True)
    app.register_blueprint(rum)
    app.run()
