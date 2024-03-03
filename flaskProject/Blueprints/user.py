from flask import Blueprint, render_template, request, redirect, url_for, session
from forms import RegisterForm, LoginForm
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from exts import db

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()

            if not user:
                return redirect(url_for('user.login_user'))
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect(url_for('index.index'))
            else:
                return redirect(url_for('user.login_user'))

        else:
            return redirect(url_for('user.login_user'))