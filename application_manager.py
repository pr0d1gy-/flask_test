class ApplicationManager(object):

    @classmethod
    def register_applications(cls, app):
        from common import common_blueprint
        from profile import profile_blueprint
        from weather import weather_blueprint

        app.register_blueprint(common_blueprint)
        app.register_blueprint(profile_blueprint)
        app.register_blueprint(weather_blueprint)
