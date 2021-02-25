import os
from flask import Flask, g, jsonify
from flask_login import LoginManager
from flask_cors import CORS, cross_origin
from models import User, DoesNotExist, initialize, DATABASE
from resources.users import users
from resources.companies import companies
from resources.reviews import reviews
from resources.sources import sources
from resources.favorites import favorites
from resources.collected_reviews import collected_reviews

DEBUG = True
PORT = 8000
app = Flask(__name__)
api_v1 = Blueprint('API_v1', __name__)
CORS(app, api_v1, origins=['http://localhost:3000', 'https://reputech-chicago.herokuapp.com', 'https://reputech-chicago.web.app/'], supports_credentials=True)

# ==============================
# 				LOGIN MANAGER
# ==============================
app.secret_key = 'This is our user club.'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
  try:
    return User.get(User.id == userid)
  except DoesNotExist:
    return None

@login_manager.unauthorized_handler
def unauthorized():
  return jsonify(
    data={"error": "User not logged in"},
    message="User must be logged in to access that resource",
    status=401
  ), 401

# ==============================
# 			REGISTER BLUEPRINTS
# ==============================

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(reviews, url_prefix='/api/v1/reviews')
app.register_blueprint(companies, url_prefix='/api/v1/companies')
app.register_blueprint(sources, url_prefix='/api/v1/sources')
app.register_blueprint(favorites, url_prefix='/api/v1/favorites')
app.register_blueprint(collected_reviews, url_prefix='/api/v1/collected_reviews')

# ==============================
# 			DATABASE CONNECTION
# ==============================

@app.before_request
def before_request():
  g.db = DATABASE
  g.db.connect()


@app.after_request
def after_request(response):
  g.db.close()
  return response

# ==============================
# 						ROUTES
# ==============================

# Index
@app.route('/')
def index():
	return 'Hello, Chi Tech Reviews!'

# ==============================
# 			CONNECTION TO SERVER
# ==============================

if 'ON_HEROKU' in os.environ: 
  print('\non heroku!')
  initialize()

if __name__ == '__main__':
	initialize()
	app.run(debug=DEBUG, port=PORT) 