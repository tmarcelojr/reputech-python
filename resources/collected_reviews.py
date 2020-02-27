from models import Collected_Review;
from flask import Blueprint, request, jsonify;
from playhouse.shortcuts import model_to_dict;

# ==============================
# 		 IMPORT DATA COLLECTED
# ==============================

from sources.glassdoor import *

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
	print(company_ratings) # prints 80, 81, 147 in order of companies
	print(company_ratings[1]) # 81
	print(company_ratings[2]) #147
	print(company_ratings[0]) #80
	return jsonify(
		data=collected_reviews_dicts,
		message=f'Successfully retrieved {len(collected_reviews_dicts)} reviews',
		status=200
	), 200

# Add data to table
@collected_reviews.route('/<source_id>/<company_id>', methods=['POST'])
def add_collected_data(source_id, company_id):
	payload = request.get_json()
	# int() since params is str obj # -1 due to list indexes.
	# using company_id since list values and companies are created in order of indexes
		# ratings_list (0, 1, 2) companies_list (company1, company2, company3)
	collected_review = Collected_Review.create(
		number_of_company_ratings=company_ratings[int(company_id) - 1],
		number_of_salary_ratings=salary_ratings[int(company_id) - 1],
		number_of_benefits_ratings=benefits_ratings[int(company_id) - 1],
		number_of_interview_ratings=interview_ratings[int(company_id) - 1],
		source=source_id,
		company=company_id
	)

	collected_review_dict = model_to_dict(collected_review)
	return jsonify(
		data=collected_review_dict,
		message=f"Successfully added ratings about company id: {company_id} source id: {source_id}",
		status=201
	), 201





