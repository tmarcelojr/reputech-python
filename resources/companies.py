from models import Company
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# This should only be accessible to admin user.

# ==============================
# 					BLUEPRINT
# ==============================

companies = Blueprint('companies', 'companies')

# ==============================
# 						ROUTES
# ==============================

# Index
@companies.route('/', methods=['GET'])
def reviews_index():
	companies_dicts = [model_to_dict(company) for company in Company]
	return jsonify(
		data=companies_dicts,
		message=f'Successfully retrieved {len(companies_dicts)} companies',
		status=200
	), 200

# Add Company
@companies.route('/', methods=['POST'])
def add_company():
	payload = request.get_json()
	company = Company.create(
		name=payload['name'],
		website=payload['website']
	)

	company_dict = model_to_dict(company)
	return jsonify(
		data=company_dict,
		message=f"Successfully added company {payload['name']}.",
		status=201
	), 201