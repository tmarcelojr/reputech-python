from models import Company
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# This should only be accessible to admin user.

# ==============================
# 		 IMPORT DATA COLLECTED
# ==============================

# from sources.companies_list import companies_list
from sources.scrape_companies import *

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
	print(payload)
	company = Company.create(
		name=payload['name'],
		website=payload['website'],
		website_logo=payload['website_logo']
	)

	company_dict = model_to_dict(company)
	return jsonify(
		data=company_dict,
		message=f'Successfully added company.',
		status=201
	), 201

# Show company
@companies.route('/<id>', methods=['GET'])
def show_company():
	return jsonify(
		data={},
		message='Succesfully displaying company show page.',
		status=200
	), 200

# Seed companies list data
@companies.route('/seed_data', methods=['POST'])
def add_companies():
	for idx, company in enumerate(company_names):
		company = Company.create(
			name=company_names[idx],
			website=company_websites[idx],
			website_logo=company_website_logos[idx]
		)
		company_dict = model_to_dict(company)
	return jsonify(
		data=company_dict,
		message='Successfully added companies.',
		status=201
	), 201




