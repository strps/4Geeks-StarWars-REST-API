from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
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
    __tablename__="planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable = False, unique = True)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Float)
    orbital_period = db.Column(db.Float)
    gravity = db.Column(db.Float)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.Float)
    created  = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __repr__(self):
        return '<Planet %r>'% self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable = False, unique = True)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))       
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50)) 
    created  = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    homeworld = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet')
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __repr__ (self):
        return '<Character %r>'% self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name
        }

class Favorites_Planets(db.Model):
    '''Favorites Model'''
    __tablename__='favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet')

class Favorites_Characters(db.Model):
    '''Favorites Model'''
    __tablename__='favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    planet_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet = db.relationship('Character')


