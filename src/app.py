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
from models import db, User, Character, Planet, Species, Vehicles, Starships, Films


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

################ Characters Routes ################

@app.route('/characters')
def get_characters():
    characters = Character.query.all()
    response_body = list(map(lambda c: c.serialize(), characters))
    return jsonify(response_body)

@app.route('/characters/<int:id>')
def get_character(id):
    character = Character.query.get(id).serialize()
    return jsonify(character)


################ Planets Routes ################

@app.route('/planets')
def get_planets():
    limit = request.args.get("limit", 10 ,type=int)
    offset = request.args.get("offset", 0 ,type=int)

    planets = Planet.query.offset(offset).limit(limit).all()
    response_body = list(map(lambda p: p.serialize(), planets))
    return jsonify(response_body)

@app.route('/planets/<int:id>')
def get_planet(id):
    planet = Planet.query.get(id).serialize()
    if planet is None:
        return jsonify({"msg":"planet not found"}), 404
    return jsonify(planet), 200

@app.route("/planets", methods=['POST'])
def create_planet():
    name = request.json.get('name')
    gravity = request.json.get('gravity')
    created_by_id = request.json.get("created_by_id")
    new_planet = Planet(name = name, gravity = gravity, created_by_id = created_by_id)
    db.session.add(new_planet)
    db.session.commit()
    return "ok" , 201

@app.route("/planets/<int:id>", methods = ['PATCH'])
def update_planet(id):
    planet = Planet.query.get(id)
    if planet is None:
        return jsonify({"msg":"planet not found"}), 404
    if request.json.get('name') is not None:
        planet.name = request.json.get('name')
    if request.json.get('gravity') is not None:
        planet.gravity = request.json.get("gravity")
    if request.json.get('grcreated_by_idavity') is not None:
        planet.created_by_id = request.json.get("created_by_id")

    db.session.add(planet)
    db.session.commit()

    return jsonify(planet.serialize()), 200

@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    if planet is None:
        return jsonify({"msg":"planet not found"}), 404
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg":"Planet deleted"})

################ Films Routes ################

@app.route('/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    film = Films.query.get(film_id)
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    return jsonify(film.serialize())

################ Starships Routes ################

@app.route('/starships/<int:id>', methods=['GET'])
def get_starship_by_id(id):
    starship = Starships.query.get(id)
    if not starship:
        return jsonify({'message': 'Starship not found'}), 404
    return jsonify(starship.serialize())

################ Vehicles Routes ################

@app.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicles.query.get(id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404
    return jsonify(vehicle.serialize())



################ Species Routes ################

@app.route('/species/<int:id>', methods=['GET'])
def get_species(id):
    species = Species.query.get(id)
    if not species:
        return jsonify({'message': 'Species not found'}), 404
    return jsonify(species.serialize())

################ Users Routes ################

@app.route('/users')
def get_users():
    users = User.query.all()
    response_body = list(map(lambda u: u.serialize(), users))
    return jsonify(response_body)

@app.route("/users/favorites")
def get_favorites():
    return 'Favorites', 200

@app.route("/favorite/planet/<int:planet_id>", methods= ["POST"])
def add_favorite_planet():
    '''Add favorite planet'''

@app.route("/favorite/character/<int:planet_id>", methods= ["POST"])
def add_favorite_character():
    '''Add Favorite Character'''

@app.route("/favorite/planet/<int:planet_id>", methods= ["DELETE"])
def delete_favorite_planet():
    '''Delete Favorite Planet'''

@app.route("/favorite/character/<int:planet_id>", methods= ["DELETE"])
def delete_favorite_character():
    '''Delete Favorite Character'''
    









# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
