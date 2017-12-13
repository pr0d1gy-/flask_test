import os
from flask import Blueprint
from settings import TEMPLATES_FOLDER, STATIC_FOLDER
from weather.routes import register_routes


weather_blueprint = Blueprint(
    'weather',
    __name__,
    template_folder=os.path.join(TEMPLATES_FOLDER, 'weather'),
    static_folder=os.path.join(STATIC_FOLDER, 'weather'),
    url_prefix='/weather'
)


register_routes(weather_blueprint)
