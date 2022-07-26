from datetime import datetime
from enum import Flag
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models.User import News, User, db
from werkzeug.security import generate_password_hash
from faker import Faker

db = SQLAlchemy()
engine = create_engine('mysql://root@localhost/db_sample')
connection = engine.raw_connection()

def index():
    pass
   


def create():
    try:
        # create tables if not exists.
        db.create_all()
        db.session.commit()
        return '==================TABLES CREATED=================='

    except Exception as e:
        print(e)
        return '==================TABLES NOT CREATED!!!=================='



# insert data into table.
def insert():
    import hashlib
    
    username='admin'
    password='admin123'
    write_api='admin123+write_4p1'
    read_api='admin123_read_4p1'

    example = User(username=username,
                       password=generate_password_hash(password, method='sha256'),
                       write_api=hashlib.md5(write_api.encode()).hexdigest(),
                       read_api=hashlib.md5(read_api.encode()).hexdigest(),
                       status=True)
    
    db.session.add(example)
    db.session.commit()


    fake_data = Faker()
    for _ in range(100):
        none = News(title=fake_data.title(),
                    content=fake_data.content(),
                    datetime=fake_data.datetime(),
                    created_by=fake_data.created_by(),
                    updated_by=fake_data.updated_by())

    db.session.add(none)
    db.session.commit() 

    return '==================DATA INSERTED=================='

def news():
    db = SQLAlchemy()
    cursor = connection.cursor()
    #SELECT
    query = "SELECT news_id, title, content, datetime FROM news"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return jsonify(result)

def show(news_id):
    db = SQLAlchemy()
    cursor = connection.cursor()
    #SELECT
    query = "SELECT news_id, title, content, datetime FROM news WHERE news_id = %s"
    cursor.execute(query, [news_id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return jsonify(result)

def update():
    pass

def delete():
    pass