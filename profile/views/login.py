from flask import render_template
from flask.views import MethodView

from profile.forms import LoginForm


class LoginView(MethodView):

    @staticmethod
    def get():
        form = LoginForm()
        return render_template('profile/login.html', form=form)

    @staticmethod
    def post():
        form = LoginForm()
        if form.validate_on_submit():
            pass
        return render_template('profile/login.html', form=form)
