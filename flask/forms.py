from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User



class RegisterForm(FlaskForm):
    username = StringField('用戶名', validators=[DataRequired(message='請輸入用戶名')])
    email = StringField('信箱', validators=[DataRequired(message='請輸入信箱'), Email(message='信箱格式錯誤')])
    password = PasswordField('密碼', validators=[DataRequired(message='請輸入密碼'), Length(min=4,message='請輸入至少4位')])
    confirm_password = PasswordField('確認密碼', validators=[DataRequired(message='請輸入密碼'), EqualTo('password', message='輸入與密碼不同')])
    submit = SubmitField('register')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('信箱已被註冊')





class LoginForm(FlaskForm):
    username = StringField('用戶名', validators=[DataRequired(message='請輸入用戶名')])
    password = PasswordField('密碼', validators=[DataRequired(message='請輸入密碼')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
