from flask import Blueprint
from controllers.UserController import index, create, insert, show, update, delete, news

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(news)
user_bp.route('/create', methods=['GET'])(create)
user_bp.route('/insert', methods=['GET'])(insert)
user_bp.route('/<int:news_id>', methods=['GET'])(show)
user_bp.route('/<int:news_id>/edit', methods=['POST'])(update)
user_bp.route('/<int:news_id>', methods=['DELETE'])(delete)