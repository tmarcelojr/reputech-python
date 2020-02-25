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

DATABASE = SqliteDatabase('users.sqlite')

# ==============================
# 						MODELS
# ==============================

# User
class User(UserMixin, Model):
	username = CharField(unique=True)
	password = CharField()
	email = CharField()
	about_me = TextField()

	class Meta:
		database = DATABASE

# Company
class Company(Model):
	name = CharField()
	website = CharField()

	class Meta:
		database = DATABASE

# Source
class Source(Model):
	name = CharField()

	class Meta:
		database = DATABASE

# Review
class Review(Model):
	creator = ForeignKeyField(User, backref='reviews')
	stars = IntegerField()
	title = CharField()
	content = CharField()
	company = ForeignKeyField(Company, backref='reviews')

	class Meta:
		database = DATABASE

# Favorite
class Favorite(Model):
	user = ForeignKeyField(User, backref='favorites')


# ==============================
# 					CONNECTION
# ==============================

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User], safe=True)
  print("Connected to DB and created tables if they weren't already there")
  DATABASE.close()