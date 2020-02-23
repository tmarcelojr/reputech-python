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

Review = {
	user fk
	content
	title
	stars
}

ScrapedReview = {
	stars = IntegerField()
	salary = IntegerField()
	benefits = IntegerField() # how good they are
	overall interview process = IntegerField()
	review_comment = CharField()
	source -- fk
	company -- fk
}

Source = {
	website_name = CharField()
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
GET | /api/v1/users/favorites | list of saved company favorites |
DELETE | /api/v1/users/favorites | delete a favorite |

### Reviews
   VERB 		 | 		  PATH 		 |  	 DESCRIPTION
------------ | ------------- | -------------------
GET | /api/v1/reviews/ | index of reviews |
GET | /api/v1/reviews/company_id | show page for selected company |

### Companies
   VERB 		 | 		  PATH 		 |  	 DESCRIPTION
------------ | ------------- | -------------------
GET | /api/v1/companies/ | index of tech companies used |





## Stretch Goals
* Search through reviews by filters from User input or choose from a list of popular key words.
* Users will be able to see a list of the most favorited companies by registered Users 
* Users can leave comments about companies - comments will be CRUDable
* Users can like companies
* Users can view most liked companies
* Page for Users to add companies not listed
* Number of job postings

Ideas

metric 
