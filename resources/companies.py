from models import Company
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

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
