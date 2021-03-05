from models import User, DoesNotExist
from flask import Blueprint, request, jsonify, session
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS, cross_origin

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
				email=payload['email']
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
		print(user)
		user_dict = model_to_dict(user)
		password_is_good = check_password_hash(user_dict['password'], payload['password'])
		if password_is_good:
			login_user(user, remember=True) # Creates a cookie for the user to remain logged in
			user_dict.pop('password')
			print(f'successful login, {user_dict}')
			session['username'] = user_dict['username']
			print(session['username'])

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

# Update user
@users.route('/<id>', methods=['PUT'])
@login_required
def update_user(id):
  payload = request.get_json()
  user = User.get_by_id(id)
  if current_user.id == user.id:
    user.username = payload['username'] if 'username' in payload else None
    user.password = generate_password_hash(payload['password']) if 'password' in payload else None
    user.email = payload['email'] if 'email' in payload else None
    user.about_me = payload['about_me'] if 'about_me' in payload else None
    user.save()
    user_dict = model_to_dict(user)
    user_dict.pop('password')
    return jsonify(
      data=user_dict,
      message=f"Successfully updated user with id {user.id}",
      status=200
    ), 200
  else:
    return jsonify(
      data="Error: Forbidden",
      message=f"User can only update their own profiles. Owner id doesn't match current user id.",
      status=403
    ), 403


# Logout
@users.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  return jsonify(
    data={},
    message='Successfully logged out',
    status=200
  ), 200

# Delete
@users.route('/<id>', methods=['Delete'])
@login_required
def delete_user(id):
	user_to_delete = User.get_by_id(id)
	user_to_delete.delete_instance()
	return jsonify(
		data={}, 
    message='Successfully deleted User.',
    status=200
  ), 200

# Check current user
@users.route('/logged_in', methods=['GET'])
def get_logged_in_user():
	if not current_user.is_authenticated:
		user = session.get('username')
		print(f'we are logged in {session['username']}')
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

















