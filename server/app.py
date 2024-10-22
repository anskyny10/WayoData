#!/usr/bin/env python3

from flask_cors import CORS
from flask import request, session, make_response
from flask_restful import Resource
# from flask_bcrypt import Bcrypt

from config import app, db, api
from models import DataUser, Favorite, User, Business, Listing, Booking, Review

CORS(app)

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# bcrypt = Bcrypt(app)

class Signup(Resource):
    def post(self):
        try:
            data = request.get_json()
            new_user = DataUser(username=data.get('username'))
            new_user.password_hash = data.get('password')
            db.session.add(new_user)
            db.session.commit()
            
            session['user_id'] = new_user.id
            return make_response(new_user.to_dict(), 201)
            
        except Exception as e:
            return make_response({'error': str(e)}, 422)
    
    
class CheckSession(Resource):
    def get(self):
        user = DataUser.query.filter(DataUser.id == session.get('user_id')).first()
        if user:
            return make_response(user.to_dict())
        else:
            return make_response({'message': '401: Not Logged In'}, 401)
        
    # def get(self):
    #     user_id = session['user_id']
    #     if user_id:
    #         cur_user = DataUser.query.filter_by(id=user_id).first()
    #         return make_response(cur_user.to_dict(), 200)
    #     return make_response({'message': 'no one is logged in'}, 401)
    

class Login(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = DataUser.query.filter_by(username=username).first()
        print(session.get('user_id'))

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return make_response(user.to_dict(), 200)

        return make_response({'error': 'Invalid username or password'}, 401)

class Logout(Resource):
    def delete(self):
        user_id = session.get('user_id')
        
        if user_id:
            session['user_id'] = None
            return make_response({'message': '204: No Content'}, 204)
        
        return make_response({'error': 'Unauthorized'}, 401)


api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
