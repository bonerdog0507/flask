from flask import Flask, render_template, request, redirect,flash, url_for
import config
from forms import LoginForm, RegisterForm
from exts import db, migrate, login_manager
from models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__)


app.config.from_object(config)
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

login_manager.login_view = 'login'
login_manager.login_message = '請先登入'


@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        password = generate_password_hash(form.password.data)
        user = User(username=form.username.data,email=form.email.data,password=password)
        db.session.add(user)
        db.session.commit()
        flash("註冊成功")
        return redirect(url_for('index'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('錯誤用戶名或密碼')

        return render_template('login.html',form=form)

    return render_template('login.html', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/test')
@login_required
def test():
    return 'test'


if __name__ == '__main__':
    app.run()
