# pseudo code
import sys
from flask import render_template, redirect, url_for, request, abort
from models.User import User
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def index():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if not user:
            return redirect(url_for('auth_bp.index'))
        elif not check_password_hash(user.password, password):
            return redirect(url_for('auth_bp.index'))
        
        login_user(user)
        return redirect('/news')

def logout():
    logout_user()
    return redirect(url_for('auth_bp.index'))
    
def create():
    pass
def insert():
    pass