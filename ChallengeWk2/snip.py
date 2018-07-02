import base64
import requests
import hashlib
from datetime import datetime
import json




access_token_path = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
consumer_key = "RcHfxBGmrkOPO0bpOoINqGpk2GHJIAf9"
consumer_password = "QGIDi4k5zciu9bTa" 
response = requests.get(access_token_path, auth=(consumer_key, consumer_password)).text
res=json.loads(response)
access_token =res ['access_token']


api_url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
      "BusinessShortCode": "174379",
      "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMDEyMjUw",
      "Timestamp": "20180702012250",
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "1",
      "PartyA": "254702838079",
      "PartyB": "174379",
      "PhoneNumber": "254702838079",
      "CallBackURL": "http://mpesa-requestbin.herokuapp.com/1lurzo81",
      "AccountReference": "test",
      "TransactionDesc": "test"
    }

def get_access_token():
        url = self.api_url + self.access_token_path
        response = self.requests.get(url, auth=(self.consumer_key, self.consumer_password))
        if response.status_code == 200:
            data = response.json()
            self.access_token = data['access_token']
            return self.access_token
        else:
            return None
response = requests.post(api_url, json = request, headers=headers)

print (response.text)
