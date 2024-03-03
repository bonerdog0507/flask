import wtforms
from wtforms.validators import Length, Email, EqualTo, ValidationError
from models import User


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=4, max=20, message='Username error')])
    password = wtforms.StringField(validators=[Length(min=4, max=20, message='Password error')])
    # confirm_password = wtforms.StringField(validators=[EqualTo('password', message='confirm passwords must match')])

    def validate_username(self,filled):
        username = filled.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message='That username is taken. Please')


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=4, max=20, message='Username error')])
    password = wtforms.StringField(validators=[Length(min=4, max=20, message='Password error')])