# Authentication, sessions, & User model
from flask_login import UserMixin
# * imports everything from peewee
from peewee import *
import datetime

# Peewee extension for creating a DB connection from a URL string
from playhouse.db_url import connect

# ==============================
# 				CREATE DATABASE
# ==============================

DATABASE = SqliteDatabase('reputech.sqlite')

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
	about_me = TextField()

# Company
class Company(BaseModel):
	name = CharField()
	website = CharField()

# Source
class Source(BaseModel):
	website_name = CharField()

# Review
class Review(BaseModel):
	creator = ForeignKeyField(User, backref='reviews')
	stars = IntegerField()
	title = CharField()
	content = CharField()
	company = ForeignKeyField(Company, backref='reviews')

# Favorite
class Favorite(BaseModel):
	user = ForeignKeyField(User, backref='favorites')
	company = ForeignKeyField(Company, backref='favorites')


# Collected reviews
class Collected_Review(BaseModel):
	number_of_company_ratings = IntegerField()
	number_of_salary_ratings= IntegerField()
	number_of_benefits_ratings = IntegerField() 
	number_of_interview_ratings = IntegerField()
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