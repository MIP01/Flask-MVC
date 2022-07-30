# Importing the necessary modules and libraries
from ast import Index
from flask import Flask, render_template
from flask_migrate import Migrate
from routes.user_bp import user_bp
from routes.auth_bp import auth_bp
from models.User import db
from flask_login import LoginManager


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix='/news')
app.register_blueprint(auth_bp, url_prefix='/auth')

login_manager = LoginManager()
login_manager.login_view='auth_bp.index'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from models.User import User
    user = User.query.filter_by(id=user_id).first()
    return user

@app.route('/')
def index():
    return render_template('home/home.html')



if __name__ == '__main__':
    app.debug = True
    app.run()