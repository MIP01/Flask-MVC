from flask import Blueprint
from controllers.AuthController import index, logout

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/', methods=['GET', 'POST'])(index)
auth_bp.route('/logout', methods=['GET'])(logout)