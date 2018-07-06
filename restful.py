from flask import Flask, jsonify, session, redirect, url_for, render_template, request

app=Flask(__name__)

app.secret_key="amoth"

details = {}#this is user details is stored in form of dictionary 
user_commentsdb =[] # user comments are stored in the database in form of list 


@app.route('/', methods=['POST', 'GET'])
def index():
    '''This is place where the user will be directed 
    homepage of the system'''
    return jsonify({"Homepage": "Welcome to Andela Library"})

@app.route('/login',methods=['POST','GET'])
def login():
    ''' Here at the login section the user has
    to enter username password and it is checked to see if his/her
    details is in the system so as to be accepted in the system'''
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    if session[username]:
        return jsonify({"message": "You are logged in"})
    else:
        if username in details:
            if password == details[username]["password"]:
                session[username]=True
                return jsonify({"message": "Login successful"})
            else:
                return jsonify({"message": "Login unsuccessful"})
        else:
            return jsonify({"message": "Login unsuccessful wrong username"})

@app.route ('/register',methods=['POST'])
def register():
    '''Here the user has to register by filling all the
    registration fields so he can be able to login'''
    first_name=request.get_json()["first_name"]
    last_name =request.get_json()["last_name"]
    sur_name = request.get_json()["sur_name"]
    email=request.get_json()["email"]
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    details.update({username:{"first_name":first_name,"last_name":last_name,"sur_name":sur_name,"email":email,"password":password}})
    return jsonify({'message' : 'you are succesfully registered'})


@app.route ('/comments_post',methods=['POST'])
def comments_post():
        comment=request.get_json()["comment"]
        user_commentsdb.append(comment)
        return jsonify({'message': 'comments posted'})

@app.route ('/view_comments', methods=['GET'])
def view_comments():
    '''Here the comments can be viewed by users where its 
    been stored in the database'''
    display = {}
    for each in user_commentsdb:
        display.update({user_commentsdb.index(each):each})
        '''this method updates the comments database each and every time
        and stores them and so it can be retrieved well so that it can be seen
        by a user in session'''
    return jsonify(display)

@app.route('/remove_comment/<int:comment>', methods=['DELETE'])
def remove_comment(comment):
    '''This function is for deleting the comments that 
    have been stored in the database'''
    del user_commentsdb[comment]
    return jsonify({"message": "One comment Deleted"})

@app.route ('/account', methods=['GET'])
def account():
    username = request.get_json()["username"]
    if username in details:
        '''If the user is in session it will bring his/her details
         and if not he will be told to login or register'''
        if session[username]:
            return jsonify(details[username])
        else:
            return jsonify("check again")
    return jsonify("Register First")

if __name__=='__main__':
    app.run(port=3000,debug=True)
