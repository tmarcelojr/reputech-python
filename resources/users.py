from models import User, DoesNotExist
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
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
	return 'We have a resource for users!'

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

# Login
@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	try:
		user = User.get(User.username == payload['username'])
		user_dict = model_to_dict(user)
		password_is_good = check_password_hash(user_dict['password'], payload['password'])
		if password_is_good:
			login_user(user, remember=True) # Creates a cookie for the user to remain logged in
			user_dict.pop('password')
			return jsonify(
					data=user_dict,
	  			message=f"Successfully logged in as {user_dict['username']}",
	  			status=200
  			), 200
		else:
  		# This means password is not correct.
			return jsonify(
      	data={},
        message='Username or password is incorrect',
        status=401
      	), 401
	except DoesNotExist:
	# Username not correct
		return jsonify(
        data={},
        message='Username or password is incorrect',
        status=401
      ), 401

# Check current user
@users.route('/logged_in', methods=['GET'])
def get_logged_in_user():
  if not current_user.is_authenticated:
    return jsonify(
      data={},
      message='No user is currently logged in',
      status=401
    ), 401
  else:
    user_dict = model_to_dict(current_user)
    user_dict.pop('password')
    return jsonify(
      data=user_dict,
      message=f"Current user is {user_dict['username']}", 
      status=200
    ), 200

# Logout
@users.route('/logout', methods=['GET'])
def logout():
  logout_user()
  return jsonify(
    data={},
    message='Successfully logged out',
    status=200
  ), 200

# Delete
# Save this for later when we have reviews behind added. So we can do cascading deletion.

















