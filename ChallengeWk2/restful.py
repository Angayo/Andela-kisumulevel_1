from flask import Flask, jsonify, request
app = Flask(__name__)

app.secret_key="amoth"
info={}
store_comments=[]

@app.route("/register" ,methods=['POST',"GET"])
def register():
    full_name=request.get_json()["Fname"]
    email=request.get_json()["email"]
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    info.update({username:{"first name":full_name,,"email":email,"password":password}})
    return jsonify({"message": "Register successful"})

@app.route("/login",methods=["GET","POST"])
def login():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    if username in info:
        if password==info[username]["password"]:
            session["logged_in"]=True
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"message": "Login unsuccessful"})
    else:
        return jsonify({"message": "Login unsuccessful"})

@app.route("/post_comment",methods=["GET","POST"])
def post_comment():
    comment=request.get_json()["comment"]
    store_comments.append(comment)
    return jsonify({"message": "successful commenting"})

@app.route("/account_details",methods=["GET"])   
def account_details():
    return jsonify(info)


if __name__=='__main__':
	app.run(debug=True)



