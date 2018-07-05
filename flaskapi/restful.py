from flask import Flask, jsonify, session, redirect, url_for, render_template, request
import jwt

app=Flask(__name__)

app.secret_key="amoth"

details = {}
store =[]

def encode_auth_token(self, user_id):
	try:
        payload = {
            'expiry': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'subject': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e

@staticmethod
def decode_auth_token(auth_token):
	try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
@app.route('/', methods=['POST', 'GET'])
def index():
    return jsonify({"Homepage": "Welcome to Andela Library"})

@app.route ('/register',methods=['POST'])
def register():
    name=request.get_json()["name"]
    username=request.get_json()["username"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    details.update({username:{"name":name,"email":email,"password":password}})
    return jsonify({'meassage' : 'you are succesfully registered'})

def login_pass(username, password):
    if username in details:
        if password == details[username]["password"]:
            return True
    return False

@app.route('/login',methods=['POST','GET'])
def login():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    if loginpass(username, password):
        return jsonify({'meassage' : 'you are succesfully logged in'})
    else:
        return jsonify({'meassage' : 'you are not succesfully logged in'})

@app.route ('/comments_post',methods=['POST'])
def comments_post():
    comment=request.get_json()["comment"]
    store.append(comment)
    return jsonify({'meassage' : 'comments posted'})

@app.route ('/view_comments', methods=['GET'])
def view_comments():
    return jsonify(store)
	
@app.route('/remove_On/<int:commentID>', methods=['DELETE'])
def remove_On(commentID):
    del store[commentID]
    return jsonify({"message": "One comment Deleted"})

@app.route ('/account', methods=['GET'])
def account():
    return jsonify(details)

if __name__=='__main__':
    app.run(port=3000,debug=True)
