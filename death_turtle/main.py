from app import app, db

from auth import *
from admin import admin
from api import api
from models import *
from views import *

admin.setup()
api.setup()

if __name__ == '__main__':

    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Message.create_table(fail_silently=True)
    Relationship.create_table(fail_silently=True)
    app.run()
