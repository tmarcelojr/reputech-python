from models import Review, DoesNotExist
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# ==============================
# 					BLUEPRINT
# ==============================

reviews = Blueprint('reviews', 'reviews')

# ==============================
# 						ROUTES
# ==============================

# Index
@reviews.route('/', methods=['GET'])
def reviews_index():
	return 'This will be a list of all our user created reviews.'