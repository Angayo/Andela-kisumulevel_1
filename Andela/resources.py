from flask_restful import Resource, reqparse
from models import Register, Token_revokeModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('first_name', help = 'This field cannot be blank', required = True)
parser.add_argument('last_name', help = 'This field cannot be blank', required = True)
parser.add_argument('sur_name', help = 'This field cannot be blank', required = True)
parser.add_argument('email', help = 'This field cannot be blank', required = True)
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)
parser.add_argument('post')


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        
        if Register.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        new_user = Register(
            first_name = data['first_name'],
            last_name = data['last_name'],
            sur_name = data['sur_name'],
            email = data['email'],
            username = data['username'],
            password = Register.generate_hash(data['password'])
        )
        
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500




class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = Register.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if Register.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jt = get_raw_jwt()['jt']
        try:
            revoked_token = RevokedTokenModel(jt = jt)
            revoked_token.add()
            return {'Message': 'Access token has been revoked'}
        except:
            return {'Message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jt = get_raw_jwt()['jt']
        try:
            revoked_token = RevokedTokenModel(jt = jt)
            revoked_token.add()
            return {'Message': 'Refresh token has been revoked'}
        except:
            return {'Message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()
    
    def delete(self):
        return UserModel.delete_all()


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'Message': 'This is your secret'
        }
