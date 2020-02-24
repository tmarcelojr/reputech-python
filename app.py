from flask import Flask 
from models import User, initialize
DEBUG = True
PORT = 8000
app = Flask(__name__)

# ==============================
# 			REGISTER BLUEPRINTS
# ==============================

# Users
# app.register_blueprint(users, url_prefix='/api/v1/users')

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