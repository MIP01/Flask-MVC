from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class User(db.Model):
    '''Data for ON/OFF should be dumped in this table.'''

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(256))
    write_api = db.Column(db.String(32))
    read_api = db.Column(db.String(32))
    status = db.Column(db.Boolean)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        return True


class News(db.Model):
    __tablename__ = 'news'
    
    news_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(100))
    datetime = db.Column(db.Integer)
    created_by = db.Column(db.String(100))
    updated_by = db.Column(db.String(100))
    flag = db.Column(db.Integer)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        return True