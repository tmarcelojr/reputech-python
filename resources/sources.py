from models import Source
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# This should only be accessible to admin user.

# ==============================
# 					BLUEPRINT
# ==============================

sources = Blueprint('sources', 'sources')

# ==============================
# 						ROUTES
# ==============================

# Index
@sources.route('/', methods=['GET'])
def sources_index():
	sources_dicts = [model_to_dict(source) for source in Source]
	return jsonify(
		data=sources_dicts,
		message=f'Successfully retrieved {len(sources_dicts)} sources',
		status=200
	), 200

# Add Source
@sources.route('/', methods=['POST'])
def add_source():
	payload = request.get_json()
	source = Source.create(
		website_name=payload['website_name']
	)

	source_dict = model_to_dict(source)
	return jsonify(
		data=source_dict,
		message=f"Successfully added source website: {payload['website_name']}.",
		status=201
	), 201