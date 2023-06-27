from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='jhvhijghlkbvhjvjkjhvcj'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    avatar = db.Column(db.Text)

    def __repr__(self):
        return f'Users({self.username},{self.email},{self.password},{self.avatar})'

class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    static_pic=db.Column(db.Text)

    def __repr__(self):
            return f'post({self.id},{self.text},{self.static_pic})'
class id(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_picture=db.Column(db.Text)

    def __repr__(self):
            return f'post({self.id_picture})'
class like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_like=db.Column(db.Text)
    post_like=db.Column(db.Text)
    def __repr__(self):
            return f'like({self.id},{self.user_like,self.post_like})'


class comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_comment=db.Column(db.Text)
    text_comment=db.Column(db.Text)
    post_comment=db.Column(db.Text)
    def __repr__(self):
        return f'comment({self.user_comment},{self.text_comment},{self.post_comment})'
class send(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_send=db.Column(db.Text)
    text_send=db.Column(db.Text)
    user_receive=db.Column(db.Text)
    def __repr__(self):
        return f'comment({self.user_send},{self.text_send},{self.user_receive})'