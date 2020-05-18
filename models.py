import os
# Authentication, sessions, & User model
from flask_login import UserMixin
# * imports everything from peewee
from peewee import *
import datetime

# Peewee extension for creating a DB connection from a URL string
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ: # later we will manually add this env var 
                              # in heroku so we can write this code
  DATABASE = connect(os.environ.get('DATABASE_URL')) # heroku will add this 
                                                     # env var for you 
                                                     # when you provision the
                                                     # Heroku Postgres Add-on
else:
  DATABASE = SqliteDatabase('reputech.sqlite')

# ==============================
# 				CREATE DATABASE
# ==============================

DATABASE = SqliteDatabase('reputech.sqlite', pragmas={'foreign_keys': 1})

# ==============================
# 						MODELS
# ==============================

# Base Model
class BaseModel(Model):
	class Meta:
		database = DATABASE

# User
class User(UserMixin, BaseModel):
	username = CharField(unique=True)
	password = CharField()
	email = CharField()

# Company
class Company(BaseModel):
	name = CharField()
	website = CharField()
	website_logo = CharField()

# Source
class Source(BaseModel):
	website_name = CharField()

# Review
class Review(BaseModel):
	creator = ForeignKeyField(User, backref='reviews', on_delete='CASCADE')
	stars = IntegerField()
	title = CharField()
	content = CharField()
	created_on = DateField(default=datetime.date.today, formats=['%Y-%m-%d'])
	company = ForeignKeyField(Company, backref='reviews')

# Favorite
class Favorite(BaseModel):
	user = ForeignKeyField(User, backref='favorites', on_delete='CASCADE')
	company = ForeignKeyField(Company, backref='favorites')


# Collected reviews
class Collected_Review(BaseModel):
	company_rating = DecimalField()
	number_of_company_ratings = IntegerField()
	number_of_salary_ratings= IntegerField()
	number_of_interview_ratings = IntegerField()
	number_of_benefits_ratings = IntegerField()
	source =  ForeignKeyField(Source, backref='collected_reviews')
	company = ForeignKeyField(Company, backref='collected_reviews')

# ==============================
# 					CONNECTION
# ==============================

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Company, Source, Review, Favorite, Collected_Review], safe=True)
  print("Connected to DB and created tables if they weren't already there")
  DATABASE.close()