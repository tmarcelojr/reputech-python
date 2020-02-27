from models import Company
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# This should only be accessible to admin user.

# ==============================
# 		 IMPORT DATA COLLECTED
# ==============================

from resources.companies_list import companies_list

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



# Seed companies list data
@companies.route('/seed_data', methods=['POST'])
def add_companies():
	payload = request.get_json()
	for idx, company in enumerate(companies_list):
		company = Company.create(
			name=companies_list[idx]['name'],
			website=companies_list[idx]['website'],
		)
		company_dict = model_to_dict(company)
	return jsonify(
		data=company_dict,
		message='Successfully added companies.',
		status=201
	), 201







