from models import Collected_Review;
from flask import Blueprint, request, jsonify;
from playhouse.shortcuts import model_to_dict;

# ==============================
# 		 IMPORT DATA COLLECTED
# ==============================

from sources.glassdoor import *
from sources.sources_list import sources_list

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

# Add data to table
@collected_reviews.route('/seed_data', methods=['POST'])
def seed_data():
	for company_idx, company in enumerate(glassdoor_company_links):
		print(company_idx, company)
		payload = request.get_json()
		# int() since params is str obj # -1 due to list indexes.
		# using company_id since list values and companies are created in order of indexes
			# ratings_list (0, 1, 2) companies_list (company1, company2, company3)
		collected_review = Collected_Review.create(
			number_of_company_ratings=company_ratings[company_idx],
			number_of_salary_ratings=salary_ratings[company_idx],
			number_of_benefits_ratings=benefits_ratings[company_idx],
			number_of_interview_ratings=interview_ratings[company_idx],
			source=1,
			company=company_idx + 1
		)
		collected_review_dict = model_to_dict(collected_review)
	return jsonify(
		data=collected_review_dict,
		message=f"Successfully added ratings about company id: source id: ",
		status=201
	), 201