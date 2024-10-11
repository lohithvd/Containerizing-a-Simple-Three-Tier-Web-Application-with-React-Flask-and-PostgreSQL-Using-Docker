from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://user:password@db/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

# REST API endpoint for frontend1
@app.route('/api/frontend1', methods=['GET'])
def frontend1_data():
    users = User.query.all()
    users_data = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(users=users_data)

# REST API endpoint for frontend2
@app.route('/api/frontend2', methods=['GET'])
def frontend2_data():
    users = User.query.all()
    users_data = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(users=users_data)

if __name__ == "__main__":
    db.create_all()  # Create database tables
    app.run(host='0.0.0.0', port=5000)
