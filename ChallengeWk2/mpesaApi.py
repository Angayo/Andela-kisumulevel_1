import requests
import base64
from datetime import datetime
import json


access_token_path = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials' 
consumer_key="RcHfxBGmrkOPO0bpOoINqGpk2GHJIAf9"
consumer_password="QGIDi4k5zciu9bTa"
response = requests.get(access_token_path, auth=(consumer_key, consumer_password)).text
res=json.loads(response)

access_token =res ['access_token']
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token  }
timestamp = "20180702012250"
shortcode =  "174379"
passPhrase = "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMDEyMjUw"
amount = int(input("enter amount"))
phone = int(input ("Enter your Phone number please: ") ) 

def  generate_pass(self, timestamp):
  string = self.shortcode + self.passPhrase + timestamp
  return base64.b64encode(string)

  password = generate_pass(shortcode + passPhrase + timestamp)

def get_access_token():
        url = self.api_url + self.access_token_path
        response = self.requests.get(url, auth=(self.consumer_key, self.consumer_password))
        if response.status_code == 200:
            data = response.json()
            self.access_token = data['access_token']
            return self.access_token
        else:
            return None
request ={
      "BusinessShortCode": shortcode,
      "Password": passPhrase,
      "Timestamp": timestamp,
      "TransactionType": "CustomerPayBillOnline",
      "Amount": amount,
      "PartyA": phone,
      "PartyB": shortcode,
      "PhoneNumber":phone,
      "CallBackURL": "http://mpesa-requestbin.herokuapp.com/1lurzo81",
      "AccountReference": "test",
      "TransactionDesc": "test"
    }
response = requests.post(api_url, json = request, headers=headers)

print (response.text)