from flask_wtf import FlaskForm

from wtforms import PasswordField, StringField, validators


class RegistrationForm(FlaskForm):

    username = StringField(
        'Username',
        [
            validators.DataRequired(),
            validators.Length(min=3, max=50)
        ],
        render_kw={
            'required': 'required'
        }
    )

    password = PasswordField(
        'Password',
        [
            validators.DataRequired(),
            validators.Length(min=6, max=50)
        ],
        render_kw={
            'required': 'required'
        }
    )

    password_confirm = PasswordField(
        'Password confirmation',
        [
            validators.DataRequired(),
            validators.Length(min=6, max=50),
            validators.EqualTo('password')
        ],
        render_kw={
            'required': 'required'
        }
    )
