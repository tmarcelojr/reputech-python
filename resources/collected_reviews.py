from models import Collected_Review
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# ==============================
# 					BLUEPRINT
# ==============================

collected_reviews = Blueprint('collected_reviews', 'collected_reviews')

# ==============================
# 						ROUTES
# ==============================

# List of collected reviews
@collected_reviews.route('/', methods=['GET'])
def collected_reviews_index():
	collected_reviews_dicts = [model_to_dict(collected_review) for collected_review in Collected_Review]
	return jsonify(
			data=collected_reviews_dicts,
			message=f'Successfully retrieved {len(collected_reviews_dicts)} reviews',
			status=200
		), 200