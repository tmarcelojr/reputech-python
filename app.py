from flask import Flask, g
from flask_login import LoginManager
from models import User, DoesNotExist, initialize, DATABASE
from resources.users import users
DEBUG = True
PORT = 8000
app = Flask(__name__)

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

# Users
app.register_blueprint(users, url_prefix='/api/v1/users')

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

if __name__ == '__main__':
	initialize()
	app.run(debug=DEBUG, port=PORT) 