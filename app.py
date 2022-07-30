# Importing the necessary modules and libraries
from ast import Index
from flask import Flask, jsonify
from flask_migrate import Migrate
from routes.user_bp import user_bp
from routes.auth_bp import auth_bp
from models.User import db
from flask_login import LoginManager, login_required


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
            'localhost:5000/auth' : 'authenticate user',
            'localhost:5000/auth/logout' : 'logout user',
            'localhost:5000/news' : 'view content list(need login)',
            'localhost:5000/news/create' : 'Create table in mysql database',
            'localhost:5000/news/insert' : 'Auto generate user and news in mysql database',
            'localhost:5000/news [POST]' : 'insert news(need login)',
            'localhost:5000/news/<int:news_id> [GET]' : 'get news by id(need login)',
            'localhost:5000/news/<int:news_id> [PUT]' : 'update news by id(need login)',
            'localhost:5000/news/<int:news_id> [PATCH]' : 'patch news by id(need login)',
            'localhost:5000/news/<int:news_id> [DELETE]' : 'delete news by id(need login)',
            'registered user' : 'password',  
            'admin' : 'admin123',
            'user' : 'user123'}



if __name__ == '__main__':
    app.debug = True
    app.run()