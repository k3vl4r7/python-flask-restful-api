from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define your SQLAlchemy models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Example route to check database creation
@app.route('/')
def index():
    return jsonify({'message': 'Flask App Running!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

