from models import Review, DoesNotExist
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict
from resources.crossdomain import crossdomain

# ==============================
# 					BLUEPRINT
# ==============================

reviews = Blueprint('reviews', 'reviews')

# ==============================
# 						ROUTES
# ==============================

# Index
@reviews.route('/', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
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
	print("hit ADD REVIEW")
	payload = request.get_json()
	print("PAYLOAD:", payload)
	review = Review.create(
		title=payload['title'],
		creator=current_user.id,
		stars=payload['stars'],
		content=payload['content'],
		company=company_id
	)
	review_dict = model_to_dict(review)
	print('our review dict', review_dict);
	review_dict['creator'].pop('password')
	return jsonify(
		data=review_dict,
		message=f"Successfully added review {payload['title']}.",
		status=201
	), 201

# Delete review
@reviews.route('/<id>', methods=['Delete'])
@login_required
def delete_review(id):
	review_to_delete = Review.get_by_id(id)
	if current_user.id == Review.creator.id:
		review_to_delete.delete_instance()
		return jsonify(
      data={}, 
      message=f'Successfully deleted review with id {review_to_delete.creator .id}',
      status=200
    ), 200
	else:
		return jsonify(
				data={'Error: Forbidden'},
				message='Penguins can only delete their own baby penguins.',
				status=403
			), 403


# Update review
@reviews.route('/<id>', methods=['PUT'])
@login_required
def update_review(id):
	payload = request.get_json()
	review = Review.get_by_id(id)
	if current_user.id == review.creator.id:
		review.title = payload['title'] if 'title' in payload else None
		review.stars = payload['stars'] if 'stars' in payload else None
		review.content = payload['content'] if 'content' in payload else None
	
		review.save()
		review_dict = model_to_dict(review)
		return jsonify(
				data=review_dict,
				message=f'Successfully updated review with id {review.id}.',
				status=200
			), 200
	else:
		return jsonify(
				data='Error: Forbidden',
				message='Reviews can only be updated their creator.',
				status=403
			), 403

