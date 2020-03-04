from models import Collected_Review;
from flask import Blueprint, request, jsonify;
from playhouse.shortcuts import model_to_dict;
import simplejson as json
import math
import sqlite3
# con = sqlite3.connect('reputech.sqlite')
# c = con.cursor()

# ratings = c.execute('SELECT company_id, avg(company_rating) FROM collected_review GROUP BY company_id;')

# average_ratings = []
# for row in ratings:
# 	average_ratings.append(row)

# # print(average_ratings)




# ==============================
# 		 IMPORT DATA COLLECTED
# ==============================

# Only import when seeding or will run everytime.
# from sources.glassdoor import *
# from sources.indeed import *

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
	con = sqlite3.connect('reputech.sqlite')
	c = con.cursor()

	ratings = c.execute('SELECT company_id, avg(company_rating) FROM collected_review GROUP BY company_id;')

	average_ratings = []
	for row in ratings:
		average_ratings.append(row)

	return jsonify(
		data=average_ratings,
		message=f'Successfully retrieved reviews',
		status=200
	), 200

# Add data to table
@collected_reviews.route('/seed_data', methods=['POST'])
def seed_data():
	collected_reviews_data = []
	sources = []
	total_company_ratings = []
	total_salary_ratings = []
	total_benefits_ratings = []
	total_interview_ratings = []
	all_company_ratings = []

	# Ratings are stored in order to keep modularity.
	# Since the structure of each website source is different each source has their own sets of list ratings. 
	# Each set of list ratings from each source are appended to empty lists to iterate over all data collected.

	# Source Glassdoor lists
	sources.append(glassdoor_company_links)
	total_company_ratings.append(glassdoor_company_ratings)
	total_salary_ratings.append(glassdoor_salary_ratings)
	total_benefits_ratings.append(glassdoor_benefits_ratings)
	total_interview_ratings.append(glassdoor_interview_ratings)
	all_company_ratings.append(glassdoor_rating)

	# Source Indeed lists
	sources.append(indeed_company_links)
	total_company_ratings.append(indeed_company_ratings)
	total_salary_ratings.append(indeed_salary_ratings)
	total_benefits_ratings.append(indeed_benefits_ratings)
	total_interview_ratings.append(indeed_interview_ratings)
	all_company_ratings.append(indeed_rating)

	for source_idx in range(len(sources_list)):
		for company_idx, company in enumerate(sources[source_idx]):
			collected_review = Collected_Review.create(
				# Nested loop based on how many sources and run each company for each source. 
				company_rating=all_company_ratings[source_idx][company_idx],
				number_of_company_ratings=total_company_ratings[source_idx][company_idx],
				number_of_salary_ratings=total_salary_ratings[source_idx][company_idx],
				number_of_benefits_ratings=total_benefits_ratings[source_idx][company_idx],
				number_of_interview_ratings=total_interview_ratings[source_idx][company_idx],
				# Assigning foreign keys. 
				# List index starts at 0 we add +1 since 'id' starts at 1. This will give Integrity Foreign Key error if left at 0. 
				source=source_idx + 1,
				company=company_idx + 1
			)
			collected_review_dict = model_to_dict(collected_review)
			collected_reviews_data.append(collected_review_dict)
			# print('!!!!!!!!!!!!!!!!!!!!!!!!!')
			# print(collected_reviews_data)
	return jsonify(
		data=collected_reviews_data,
		message=f"Successfully seeded data.",
		status=201
	), 201

