from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

# Models go here!

class DataUser(db.Model, SerializerMixin):
    __tablename__ = 'data_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.Text, nullable=False)
    internal = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    favorites = db.relationship('Favorite', back_populates='data_user')
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError('password is private')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    data_user_id = db.Column(db.Integer, db.ForeignKey('data_users.id'))
    widget_id = db.Column(db.Integer)

    data_user = db.relationship('DataUser', back_populates='favorites')


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    industry = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    last_login = db.Column(db.Date)

    bookings = db.relationship('Booking', back_populates='user')


class Business(db.Model, SerializerMixin):
    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    space_type = db.Column(db.String)
    city = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    listings = db.relationship('Listing', back_populates='business')


class Listing(db.Model, SerializerMixin):
    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    listing_type = db.Column(db.String, nullable=False)
    space_type = db.Column(db.String)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    price = db.Column(db.DECIMAL)

    business = db.relationship('Business', back_populates='listings')
    bookings = db.relationship('Booking', back_populates='listing')
    reviews = db.relationship('Review', back_populates='listing')


class Booking(db.Model, SerializerMixin):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    booking_type = db.Column(db.String, nullable=False)
    price = db.Column(db.DECIMAL)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    user = db.relationship('User', back_populates='bookings')
    listing = db.relationship('Listing', back_populates='bookings')


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    overall = db.Column(db.Integer)
    wifi = db.Column(db.Integer)
    outlet = db.Column(db.Integer)
    food = db.Column(db.Integer)
    great = db.Column(db.Text)
    better = db.Column(db.Text)
    created_at = db.Column(db.Date)

    listing = db.relationship('Listing', back_populates='reviews')