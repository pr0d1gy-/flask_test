import os
import ast


def env(key, default=None, is_required=False):
    try:
        value = os.environ.get(key, None)

        if not value:
            if is_required:
                raise AttributeError(
                    'Setting `{}` is required in that project.'.format(key))
            return default

        return ast.literal_eval(value)

    except AttributeError as e:
        raise e
    except (SyntaxError, ValueError):
        return value


# Additional config for Flask App
class ConfigApp(object):

    SQLALCHEMY_DATABASE_URI = env('DATABASE_URI', is_required=True)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = env('SECRET_KEY', is_required=True)

DEBUG = env('DEBUG', True)

HOST = env('HOST', 'localhost')
PORT = env('PORT', 8000)

TEMPLATES_FOLDER = 'templates'
STATIC_FOLDER = 'static'
