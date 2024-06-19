from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def create_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return jsonify({'message': 'Flask App Running!'})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email
                }
        user_list.append(user_data)
    return jsonify({'users': user_list})

if __name__ == '__main__':
    app.run(debug=True)

