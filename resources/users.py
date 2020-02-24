from models import User
from flask import Blueprint

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