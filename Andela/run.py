from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:postgres:angayo@localhost/myproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'amoth'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_SECRET_KEY'] = 'tokensecretkey'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jt = decrypted_token['jt']
    return models.RevokedTokenModel.is_jti_blacklisted(jt)

import view, models, resources

api.add_resource(resources.UserRegistration, '/register')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.Comment, '/comment')
api.add_resource(resources.AllComments, '/post')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')



if __name__ == '__main__':
	app.run(debug=True,port=3000)
