import os
from flask import Blueprint
from settings import TEMPLATES_FOLDER, STATIC_FOLDER
from common.routes import register_routes


common_blueprint = Blueprint(
    'common',
    __name__,
    template_folder=os.path.join(TEMPLATES_FOLDER, 'common'),
    static_folder=os.path.join(STATIC_FOLDER, 'common'),
    url_prefix='/'
)


register_routes(common_blueprint)
