from models import Favorite
from flask import Blueprint, request, jsonify
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
