from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Float)
    orbital_period = db.Column(db.Float)
    gravity = db.Column(db.Float)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.Float)
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    created_by_id = db.Column(
    db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_by = db.relationship('User')

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_by": self.created_by.serialize()
        }


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    # homeworld_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    # homeworld = db.relationship('Planet')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship(User)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            # "homeworld_id": self.homeworld_id,
            # "homeworld": self.homeworld,
            "created_by_id": self.created_by_id,
            "created_by": self.created_by.serialize()
        }



class Films(db.Model):
    __tablename__ = "films"
    id = db.Column(db.Integer, primary_key=True)
    # characters= db.Column()       
    director = db.Column(db.String(120))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    episode_id = db.Column(db.Integer)
    opening_crawl = db.Column(db.String(120))
    # planets= db.Column()
    producer = db.Column(db.String(120))
    release_date = db.Column(db.Date)
    # species= db.Column()
    # starships= db.Column()
    title = db.Column(db.String(120))
    # url= db.Column()
    # vehicles= db.Column()

    def __repr__(self):
        return '<Film %r>' % self.title

    def serialize(self):
        return {
        "director":self.director, 
        "created":self.created,
        "edited":self.edited,
        "episode_id":self.episode_id,
        "opening_crawl":self.opening_crawl,
        # planets
        "producer":self.producer,
        "release_date":self.release_date,
        # species
        # starships
        "title":self.title,
        }

class Starships(db.Model):
    __tablename__ = "starships"
    id = db.Column(db.Integer, primary_key=True)
    MGLT = db.Column(db.String(120))  
    cargo_capacity = db.Column(db.Integer)  
    consumables = db.Column(db.String(120)) 
    cost_in_credits = db.Column(db.Integer)  
    created = db.Column(db.DateTime)  
    crew = db.Column(db.Integer) 
    edited = db.Column(db.DateTime) 
    hyperdrive_rating = db.Column(db.String())  
    length = db.Column(db.Integer)  
    manufacturer = db.Column(db.String(120))
    max_atmosphering_speed = db.Column(db.Integer)
    model = db.Column(db.String(120))
    name = db.Column(db.String(120))
    passengers = db.Column(db.Integer)
    # films= db.Column()
    # pilots= db.Column()
    # ": "Deep Space Mobile Battlestation",
    starship_class = db.Column(db.String(120))
    # url= db.Column()

    def __repr__():
        return '<Starship %r>' % self.name

    def serialize(self):
        return {
        "MGLT": self.MGLT,
        "cargo_capacity": self.cargo_capacity,
        "consumables": self.consumables,
        "cost_in_credits": self.cost_in_credits,
        "created": self.created,
        "crew": self.crew,
        "edited": self.edited,
        "hyperdrive_rating": self.hyperdrive_rating,
        "length": self.length,
        "manufacturer": self.manufacturer,
        "max_atmosphering_speed": self.max_atmosphering_speed,
        "model": self.model,
        "name": self.name,
        "passengers": self.passengers,
        # "films": self.films,
        # "pilots": self.pilots,
        "starship_class": self.starship_class
        # "url": self.url
        }



class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(120))
    cost_in_credits = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    crew = db.Column(db.Integer)
    edited = db.Column(db.DateTime())
    length = db.Column(db.Integer)
    manufacturer = db.Column(db.String(120))
    max_atmosphering_speed = db.Column(db.Integer)
    model = db.Column(db.String(120))
    name = db.Column(db.String(120))
    passengers = db.Column(db.Integer)
    # pilots=db.Column()
    # films=db.Column()
    # url=db.Column()
    vehicle_class = db.Column(db.String(120))

    def serialize(self):
        return {
        "cargo_capacity": self.cargo_capacity,
        "consumables": self.consumables,
        "cost_in_credits": self.cost_in_credits,
        "created": self.created,
        "crew": self.crew,
        "edited": self.edited,
        "length": self.length,
        "manufacturer": self.manufacturer,
        "max_atmosphering_speed": self.max_atmosphering_speed,
        "model": self.model,
        "name": self.name,
        "passengers": self.passengers,
        "vehicle_class": self.vehicle_class
        }


class Species(db.Model):
    __tablename__ = "species"
    id = db.Column(db.Integer, primary_key=True)
    average_height = db.Column(db.Integer)
    average_lifespan = db.Column(db.Integer)
    classification = db.Column(db.String(120))
    created = db.Column(db.DateTime)
    designation = db.Column(db.String(120))
    edited = db.Column(db.DateTime)
    eye_colors = db.Column(db.String(120))
    hair_colors = db.Column(db.String(120))  
    #homeworld = db.Column(db.String(120))
    language = db.Column(db.String(120))
    name = db.Column(db.String(120))
    #people = db.Column(db.String(120))
    #films = db.Column(db.String(120))
    skin_colors = db.Column(db.String(120))
    #url = db.Column(db.String(120))

    def serialize(self):
        return {
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
            "classification": self.classification,
            "created": self.created.strftime("%Y-%m-%d %H:%M:%S"),
            "designation": self.designation,
            "edited": self.edited.strftime("%Y-%m-%d %H:%M:%S"),
            "eye_colors": self.eye_colors,
            "hair_colors": self.hair_colors,
            "language": self.language,
            "name": self.name,
            "skin_colors": self.skin_colors,
        }


class Favorites_Planets(db.Model):
    '''Favorites Planets'''
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet')


class Favorites_Characters(db.Model):
    '''Favorites Characters'''
    __tablename__ = 'favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    planet_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet = db.relationship('Character')


class Favorites_Vehicles(db.Model):
    '''Favorites Vehicles'''
    __tablename__ = 'favorites_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicle = db.relationship('Vehicles')


class Favorites_Species(db.Model):
    '''Favorites Species'''
    __tablename__ = 'favorites_species'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species = db.relationship('Species')

class Favorites_Films(db.Model):
    '''Favorites Films'''
    __tablename__ = 'favorites_films'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film = db.relationship('Films')

class Favorites_Starships(db.Model):
    '''Favorites Starships'''
    __tablename__ = 'favorites_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship = db.relationship('Starships')
