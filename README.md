# Chicago Tech Companies Reviews 

## Description

API will be created using python. Scraping will be completed with beautiful soup. Scraped results will be distributed to appropiate fields in Company Card. 

## Models
```
User = {
	username = CharField(unique=True)
	password = CharField()
	email = CharField()
	about_me = TextField()
}

Company = {
	company_name = CharField() 
	company_website = CharField()
}

Source = {
	website_name = CharField()
}

Review = {
	creator = ForeignKeyField(User, backref='reviews')
	content = CharField()
	title = CharField()
	stars = IntegerField()
	company = fk
}

Scraped_Reviews = {
	number_of_salary_reported= IntegerField()
	number_of_benefits_reported = IntegerField() 
	number_of_interview = IntegerField()
	review = fk
	source =  fk
	company = fk
}

Favorite = {
	user = ForeignKeyField(User, backref='favorites')
	company fk
}
```
## Routes

### User
   VERB 		 | 		  PATH 		 |  	 DESCRIPTION
------------ | ------------- | -------------------
POST | /api/v1/users/register | register User |
POST | /api/v1/users/login | login User |
GET | /api/v1/users/logout | logout User |
GET | /api/v1/users/id | show User profile|
PUT | /api/v1/users/id | update User |
DELETE | /api/v1/users/id | delete User |

### Companies
   VERB 		 | 		  PATH 		 |  	 DESCRIPTION
------------ | ------------- | -------------------
GET | /api/v1/companies/ | index of tech companies used |


### Favorites
GET | /api/v1/favorites | list of saved company favorites |
DELETE | /api/v1/favorites/fave_id | delete a favorite |

### Reviews
   VERB 		 | 		  PATH 		 |  	 DESCRIPTION
------------ | ------------- | -------------------
GET | /api/v1/reviews/ | index of reviews |
GET | /api/v1/reviews/company_id | show page for selected company |
POST | /api/v1/reviews/company_id/ | add a review |
PUT | /api/v1/reviews/company_id/review_id | edit/update a review |
DELETE | /api/v1/reviews/company_id/review_id | delete review |


## Stretch Goals
* Users will be able to see a list of the most favorited companies by registered Users 
* Users can like companies
* Users can view most liked companies
* Number of job postings
