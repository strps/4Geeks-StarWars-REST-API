"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/characters')
def get_characters():
    characters = Character.query.all()
    response_body = list(map(lambda c: c.serialize(), characters))
    return jsonify(response_body)

@app.route('/characters/<int:id>')
def get_character(id):
    character = Character.query.get(id).serialize()
    return jsonify(character)

@app.route('/planets')
def get_planets():
    planets = Planet.query.all()
    response_body = list(map(lambda p: p.serialize(), planets))
    return jsonify(response_body)

@app.route('/planets/<int:id>')
def get_planet(id):
    planet = Planet.query.get(id).serialize()
    return jsonify(planet)

@app.route('/users')
def get_users():
    users = User.query.all()
    response_body = list(map(lambda u: u.serialize(), users))
    return jsonify(response_body)

@app.route("/users/favorites")
def get_favorites():
    return 'Favorites'





# @app.route('/favorite/planet/<int:planet_id>', methods=['POST'])

# @app.route('/favorite/characters/<int:characters_id>', methods=['POST'])

# @app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])

# @app.route('/favorite/characters/<int:characters_id>', methods=['DELETE'])





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
