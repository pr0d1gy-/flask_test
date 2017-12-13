import os
from flask import Blueprint
from settings import TEMPLATES_FOLDER, STATIC_FOLDER
from profile.routes import register_routes


profile_blueprint = Blueprint(
    'profile',
    __name__,
    template_folder=os.path.join(TEMPLATES_FOLDER, 'profile'),
    static_folder=os.path.join(STATIC_FOLDER, 'profile'),
    url_prefix='/profile'
)


register_routes(profile_blueprint)
