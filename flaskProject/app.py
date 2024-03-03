from flask import Flask, session, g
from exts import db,mail
from flask_migrate import Migrate
from Blueprints.user import bp as bp_user
from Blueprints.index import bp as bp_index
from models import User
import config



app = Flask(__name__)


app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

app.register_blueprint(bp_index)
app.register_blueprint(bp_user)
migrate = Migrate(app, db)

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {'user': g.user}




if __name__ == '__main__':
    app.run()
