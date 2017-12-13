from flask import render_template
from flask.views import MethodView

from profile.forms import RegistrationForm
from profile.models import User


class RegistrationView(MethodView):

    @staticmethod
    def get():
        form = RegistrationForm()
        return render_template('profile/registration.html', form=form)

    @staticmethod
    def post():
        form = RegistrationForm()
        if form.validate_on_submit():
            pass
        return render_template('profile/registration.html', form=form)
