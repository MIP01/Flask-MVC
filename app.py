# Importing the necessary modules and libraries
from ast import Index
from flask import Flask, jsonify
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
    return {'status': 'OK',
            'localhost:5000/auth': 'authenticate user',
            'localhost:5000/news/create': 'Create table in mysql database',
            'localhost:5000/news/insert': 'Insert data in mysql database table(news)',
            'localhost:5000/news/<int:news_id>': 'select data in mysql database table(news)'}


if __name__ == '__main__':
    app.debug = True
    app.run()