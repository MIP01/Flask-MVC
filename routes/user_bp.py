from flask import Blueprint
from controllers.UserController import index, news, create, insert, get_news, update, insert_news, patch_news, delete

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(news)
user_bp.route('/create', methods=['GET'])(create)
user_bp.route('/insert', methods=['GET'])(insert)
user_bp.route('/<int:news_id>', methods=['GET'])(get_news)
user_bp.route('/<int:news_id>', methods=['PUT'])(update)
user_bp.route('/', methods=['POST'])(insert_news)
user_bp.route('/<int:news_id>', methods=['PATCH'])(patch_news)
user_bp.route('/<int:news_id>', methods=['DELETE'])(delete)