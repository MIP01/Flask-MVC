from datetime import datetime
from enum import Flag
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models.User import News, User, db
from werkzeug.security import generate_password_hash
from faker import Faker
from faker_vehicle import VehicleProvider

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


    fake = Faker()
    fake.add_provider(VehicleProvider)
    for _ in range(100):
        none = News(title=fake.vehicle_category(),
                    content=fake.vehicle_make_model(),
                    datetime=fake.vehicle_year(),
                    created_by=fake.name(),
                    updated_by=fake.name(),
                    flag=fake.random_element(elements=('1', '2', '3')))

        db.session.add(none)
    db.session.commit() 

    return '==================DATA INSERTED=================='

#routing
def news():
    db = SQLAlchemy()
    cursor = connection.cursor()
    #SELECT
    query = "SELECT news_id, title, content, datetime, flag FROM news"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return jsonify(result)

def get_news(news_id):
    db = SQLAlchemy()
    cursor = connection.cursor()
    #SELECT
    query = "SELECT news_id, title, content, datetime, flag FROM news WHERE news_id = %s"
    cursor.execute(query, [news_id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return jsonify(result)

def insert_news():
    db = SQLAlchemy()
    cursor = connection.cursor()
    news_details = request.json
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    created_by = news_details['created_by']
    query = "INSERT INTO news(title, content, datetime, flag, created_by) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(query, [title, content, datetime, flag, created_by])
    connection.commit()

    return ('data inserted')

def update(news_id):
    db = SQLAlchemy()
    cursor = connection.cursor()
    news_details = request.json
    news_id = news_details['news_id']
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']
    updated_by = news_details['updated_by']
    query = "UPDATE news SET title = %s, content = %s, datetime = %s, flag = %s, updated_by = %s WHERE news_id = %s"
    cursor.execute(query, [title, content, datetime, flag, updated_by, news_id])
    connection.commit()

    return ("data updated")

def patch_news(news_id):
    db = SQLAlchemy()
    cursor = connection.cursor()
    news_details = request.json
    news_id = news_details['news_id']
    flag = news_details['flag']
    query = "UPDATE news SET flag = %s WHERE news_id = %s"
    cursor.execute(query, [flag, news_id])
    connection.commit()
    
    return ('patched')

def delete(news_id):
    db = SQLAlchemy()
    cursor = connection.cursor()
    query = "DELETE FROM news WHERE news_id = %s"
    cursor.execute(query, [news_id])
    connection.commit()
    return ('deleted')