from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False) 
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    user_favorite = db.relationship("Favorite_People", backref="user")

    #de manera automática, el nombre de la tabla es el nombre de la clase en minúscula
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "descripcion": self.description
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.Float)
    people_favorite = db.relationship("Favorite_People", backref="people")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass          
        }

class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    #Esta es una tabla pivote para relacionar User y People, relación muchos a muchos

    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "character_name": People.query.get(self.people_id).serialize()['name']          
        } 

class Planets (db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False) 
    diameter = db.Column(db.Float) 
    rotation_Period = db.Column(db.Float)
    orbital_Period = db.Column(db.Float)
    gravity = db.Column(db.String(100))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_Water = db.Column(db.Integer)
    planets_favorite = db.relationship("Favorite_Planets", backref="planet") 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,  
            "diameter": self.diameter,
            "rotation_Period": self.rotation_Period,
            "orbital_Period": self.orbital_Period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_Water": self.surface_Water   
        } 

class Favorite_Planets(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))


    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "planet_name": Planets.query.get(self.planet_id).serialize()['name']   
            "planet_diameter": Planets.query.get(self.planet_id).serialize()['diameter']   
            "planet_rotation_Period": Planets.query.get(self.planet_id).serialize()['rotation_Period']   
            "planet_orbital_Period": Planets.query.get(self.planet_id).serialize()['orbital_Period']   
            "planet_gravity": Planets.query.get(self.planet_id).serialize()['gravity']   
            "planet_population": Planets.query.get(self.planet_id).serialize()['population']   
            "planet_climate": Planets.query.get(self.planet_id).serialize()['climate']   
            "planet_terrain": Planets.query.get(self.planet_id).serialize()['terrain']   
            "planet_surface_Water": Planets.query.get(self.planet_id).serialize()['surface_Water']   
        }    