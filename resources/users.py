from models import User, DoesNotExist
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user
from playhouse.shortcuts import model_to_dict

# ==============================
# 					BLUEPRINT
# ==============================

users = Blueprint('users', 'users')

# ==============================
# 						ROUTES
# ==============================

# Index
@users.route('/', methods=['GET'])
def test_user_resource():
	return "We have a resource for users!"

# Register User
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	payload['email'] = payload['email'].lower()
	try:
		User.get(User.username == payload['username'])
		return jsonify(
			data={},
			message='Username is already taken.',
			status=401
		), 401

	except DoesNotExist:
		created_user = User.create(
				username=payload['username'],
				password=generate_password_hash(payload['password']),
				email=payload['email'],
				about_me=payload['about_me']
			)
		login_user(created_user)
		user_dict = model_to_dict(created_user)
		# Do not return password
		user_dict.pop('password')
		return jsonify(
				data=user_dict,
				message=f"Successfully registered {user_dict['username']}.",
				status=201
			), 201






















