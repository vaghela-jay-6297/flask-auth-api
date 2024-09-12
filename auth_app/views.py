# User_app/views.py
from flask import request, jsonify
from marshmallow import ValidationError
from auth_app import user_auth
from app import db
from .models import User
from .schemas import UserSerializer

@user_auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()   # get data 
        validated_data = UserSerializer().load(data)  # check data validation
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = User(**validated_data)   # add dict data into User table

    db.session.add(user)    # add data into db
    db.session.commit()     # save changes

    return jsonify({'message': 'User Registartion success.', 
                    'data': UserSerializer().dump(user)}), 201  # return success msg response with convert in into json


@user_auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=data.get('email')).first()
    if (not user) or (not user.check_password(data.get('password'))):
        return jsonify({"error": "Invalid Credentials, please try again!"}), 401

    # access_token = create_access_token(identity=user.id)    # generate JWT token
    return jsonify({"message": "Login successful.",
                    "user": UserSerializer().dump(user)}), 200
