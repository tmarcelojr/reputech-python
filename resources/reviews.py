from models import Review, DoesNotExist
from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
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
	reviews_dicts = [model_to_dict(review) for review in Review]
	return jsonify(
			data=reviews_dicts,
			message=f'Successfully retrieved {len(reviews_dicts)} reviews',
			status=200
		), 200

# Add review
@reviews.route('/<company_id>', methods=['POST'])
@login_required
def add_review(company_id):
	payload = request.get_json()
	review = Review.create(
		title=payload['title'],
		creator=current_user.id,
		stars=payload['stars'],
		content=payload['content'],
		company=company_id
	)

	review_dict = model_to_dict(review)
	review_dict['creator'].pop('password')
	return jsonify(
		data=review_dict,
		message=f"Successfully added review {payload['title']}.",
		status=201
	), 201

