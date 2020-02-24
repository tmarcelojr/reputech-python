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

	class Meta:
		database = DATABASE


# ==============================
# 					CONNECTION
# ==============================

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User], safe=True)
  print("Connected to DB and created tables if they weren't already there")
  DATABASE.close()