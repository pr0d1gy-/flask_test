from flask import redirect, url_for
from flask.views import MethodView


class LogoutView(MethodView):

    @staticmethod
    def get():
        return redirect(url_for('profile.login'))
