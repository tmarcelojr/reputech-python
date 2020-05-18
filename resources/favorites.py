from models import Favorite
from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

# ==============================
# 					BLUEPRINT
# ==============================

favorites = Blueprint('favorites', 'favorites')

# ==============================
# 						ROUTES
# ==============================

# Index
@favorites.route('/', methods=['GET'])
def favorites_index():
	favorites_dicts = [model_to_dict(favorite) for favorite in Favorite]
	return jsonify(
		data=favorites_dicts,
		message=f'Successfully retrieved {len(favorites_dicts)} favorites',
		status=200
	), 200


# Add Favorite
@favorites.route('/<company_id>', methods=['POST'])
@login_required
def add_favorite(company_id):
	favorite = Favorite.create(
		user=current_user.id,
		company=company_id
	)

	favorite_dict = model_to_dict(favorite)
	return jsonify(
		data=favorite_dict,
		message=f"Successfully added {company_id} to favorite list.",
		status=201
	), 201

# Delete Favorite
@favorites.route('/<company_id>', methods=['Delete'])
@login_required
def delete_favorite(company_id):
	favorite_to_delete = Favorite.get_by_id(company_id)
	if current_user.id == Favorite.user.id:
		favorite_to_delete.delete_instance()
		return jsonify(
			data={},
			message=f'Successfylly removed from favorites list with id {favorite_to_delete.user.id}',
			status= 200
		), 200
	else:
		return jsonify(
			data={'Error: Forbidden'},
			message='Users can only removed their own favorite',
			status=403
		), 403
