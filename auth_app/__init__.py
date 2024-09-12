from flask import Blueprint
user_auth = Blueprint('user-auth', __name__, url_prefix='/')

from auth_app import views, models